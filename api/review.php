<?php
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD']!=='POST'){http_response_code(405);echo json_encode(['ok'=>false]);exit;}
function v($k){return isset($_POST[$k])?trim($_POST[$k]):'';}
if (v('company')!==''){echo json_encode(['ok'=>true]);exit;}
$name=substr(v('name'),0,120);
$email=filter_var(v('email'),FILTER_VALIDATE_EMAIL)?v('email'):'';
$country=substr(v('country'),0,60);
$stay=substr(v('stay'),0,80);
$score=(float)v('score'); if($score<1)$score=5; if($score>5)$score=5;
$text=substr(v('text'),0,3000);
if($name===''||$text===''){http_response_code(422);echo json_encode(['ok'=>false,'error'=>'missing']);exit;}
// email to owner (forwards to Gmail via mail server bcc)
$to='hello@casavalesa.gr';
$subj="New guest review — $name (".$score."/5)";
$body="A guest left a review on casavalesa.gr (pending your approval):\n\nName: $name\nCountry: $country\nStay: $stay\nScore: $score/5\nEmail: $email\n\nReview:\n$text\n\nApprove it in Airtable (Reviews table) and it will appear on the site.\n";
$h="From: Casa Valesa <hello@casavalesa.gr>\r\n";
if($email)$h.="Reply-To: $name <$email>\r\n";
$h.="Content-Type: text/plain; charset=utf-8\r\n";
@mail($to,"=?UTF-8?B?".base64_encode($subj)."?=",$body,$h,'-f hello@casavalesa.gr');
// optional Airtable Reviews (Pending) when token configured
$cfg='/etc/casavalesa/airtable.env';
if(is_readable($cfg)){
  $e=parse_ini_file($cfg);
  if(!empty($e['PAT'])&&!empty($e['BASE'])){
    $payload=json_encode(['records'=>[['fields'=>array_filter([
      'Name'=>$name,'Source'=>'Direct','Country'=>$country,'Stay'=>$stay,'Score'=>$score,'Scale'=>5,
      'Text'=>$text,'Status'=>'Pending','Email'=>$email,'Received'=>date('c')],fn($x)=>$x!==''&&$x!==null)]],'typecast'=>true]);
    $ch=curl_init("https://api.airtable.com/v0/{$e['BASE']}/Reviews");
    curl_setopt_array($ch,[CURLOPT_POST=>1,CURLOPT_RETURNTRANSFER=>1,CURLOPT_TIMEOUT=>8,
      CURLOPT_HTTPHEADER=>['Authorization: Bearer '.$e['PAT'],'Content-Type: application/json'],CURLOPT_POSTFIELDS=>$payload]);
    curl_exec($ch);curl_close($ch);
  }
}
echo json_encode(['ok'=>true]);
