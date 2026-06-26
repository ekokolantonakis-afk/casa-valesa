<?php
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] !== 'POST'){ http_response_code(405); echo json_encode(['ok'=>false,'error'=>'method']); exit; }
function v($k){ return isset($_POST[$k]) ? trim($_POST[$k]) : ''; }
if (v('company') !== ''){ echo json_encode(['ok'=>true]); exit; } // honeypot
$type   = v('type') === 'contact' ? 'contact' : 'booking';
$name   = substr(v('name'),0,120);
$email  = filter_var(v('email'), FILTER_VALIDATE_EMAIL) ? v('email') : '';
$phone  = substr(v('phone'),0,40);
$cin    = preg_match('/^\d{4}-\d{2}-\d{2}$/', v('checkin'))  ? v('checkin')  : '';
$cout   = preg_match('/^\d{4}-\d{2}-\d{2}$/', v('checkout')) ? v('checkout') : '';
$guests = (int) v('guests');
$msg    = substr(v('message'),0,3000);
if ($name==='' || ($email==='' && $phone==='')){ http_response_code(422); echo json_encode(['ok'=>false,'error'=>'missing']); exit; }

// availability virtual-check (booking only)
$available = null; $conflicts = [];
if ($type==='booking' && $cin && $cout){
  $av = @json_decode(@file_get_contents(__DIR__.'/../availability.json'), true);
  $booked = is_array($av['booked'] ?? null) ? $av['booked'] : [];
  $available = true;
  for($d=strtotime($cin); $d < strtotime($cout); $d=strtotime('+1 day',$d)){
    $day = date('Y-m-d',$d);
    if (in_array($day,$booked,true)){ $available=false; $conflicts[]=$day; }
  }
}

// email
$to = 'hello@casavalesa.gr';
$subj = ($type==='booking' ? 'Booking enquiry' : 'Contact') . " — $name";
$body = "Type: $type\nName: $name\nEmail: $email\nPhone: $phone\n";
if ($type==='booking') $body .= "Check-in: $cin\nCheck-out: $cout\nGuests: $guests\n";
if ($available===false) $body .= "** Requested dates overlap blocked days: ".implode(', ',$conflicts)." **\n";
$body .= "Message:\n$msg\n\n— casavalesa.gr form\n";
$headers = "From: Casa Valesa <hello@casavalesa.gr>\r\n";
if ($email) $headers .= "Reply-To: $name <$email>\r\n";
$headers .= "Content-Type: text/plain; charset=utf-8\r\n";
@mail($to, "=?UTF-8?B?".base64_encode($subj)."?=", $body, $headers, '-f hello@casavalesa.gr');

// optional Airtable capture (drop /etc/casavalesa/airtable.env with PAT=... BASE=... to enable)
$cfg='/etc/casavalesa/airtable.env';
if (is_readable($cfg)){
  $e=parse_ini_file($cfg);
  if (!empty($e['PAT']) && !empty($e['BASE'])){
    $fields=['Name'=>$name,'Email'=>$email,'Phone'=>$phone,'Guests'=>$guests?:null,
      'Message'=>$msg,'Channel'=>($type==='booking'?'Booking form':'Contact form'),'Status'=>'New',
      'Received'=>date('c')];
    if($cin) $fields['Check-in']=$cin; if($cout) $fields['Check-out']=$cout;
    $payload=json_encode(['records'=>[['fields'=>array_filter($fields, fn($x)=>$x!==null && $x!=='')]],'typecast'=>true]);
    $ch=curl_init("https://api.airtable.com/v0/{$e['BASE']}/Enquiries");
    curl_setopt_array($ch,[CURLOPT_POST=>1,CURLOPT_RETURNTRANSFER=>1,CURLOPT_TIMEOUT=>8,
      CURLOPT_HTTPHEADER=>['Authorization: Bearer '.$e['PAT'],'Content-Type: application/json'],
      CURLOPT_POSTFIELDS=>$payload]);
    curl_exec($ch); curl_close($ch);
  }
}
echo json_encode(['ok'=>true,'available'=>$available]);
