<?php

define('API_KEY', 'TOKEN BOT');
function bot($method,$datas=[]){
    $url = "https://api.telegram.org/bot".API_KEY."/".$method;
    $ch = curl_init();
    curl_setopt($ch,CURLOPT_URL,$url);
    curl_setopt($ch,CURLOPT_RETURNTRANSFER,true);
    curl_setopt($ch,CURLOPT_POSTFIELDS,$datas);
    $res = curl_exec($ch);
    if(curl_error($ch)){
        var_dump(curl_error($ch));
    }else{
        return json_decode($res);
    }
}

function SendMessage($chatid,$text,$parsmde,$disable_web_page_preview,$keyboard){
 bot('sendMessage',[
 'chat_id'=>$chatid,
 'text'=>$text,
 'parse_mode'=>$parsmde,
 'disable_web_page_preview'=>$disable_web_page_preview,
 'reply_markup'=>$keyboard
 ]);
 } 
 function sendphoto($chat_id, $photo, $caption){
 bot('sendphoto',[
 'chat_id'=>$chat_id,
 'photo'=>$photo,
 'caption'=>$caption,
 ]);
 }
 function Forward($chatid,$from_chat,$message_id){
  bot('ForwardMessage',[
  'chat_id'=>$chatid,
  'from_chat_id'=>$from_chat,
  'message_id'=>$message_id
  ]);
  }
function senddocument($chat_id,$document,$caption){
    bot('senddocument',[
        'chat_id'=>$chat_id,
        'document'=>$document,
        'caption'=>$caption
    ]);
}
 function sendvideo($chat_id, $video, $caption){
 bot('sendvideo',[
 'chat_id'=>$chat_id,
 'photo'=>$video,
 'caption'=>$caption,
 ]);
 }
 function sendaudio($chat_id, $audio, $caption){
 bot('sendaudio',[
 'chat_id'=>$chat_id,
 'audio'=>$audio,
 'caption'=>$caption,
 ]);
 }

$update = json_decode(file_get_contents('php://input'));
$message = $update->message; 
$chat_id = $message->chat->id;
$from_id = $update->message->from->id;
$text = $message->text;
@mkdir("data/$chat_id");
@$hunter = file_get_contents("data/$chat_id/hunter2.txt");
$admin = ID BRO;
$panel = file_get_contents("mirtm.txt");
$name = $message->from->first_name;
$lastname = $message->from->last_name;
$username = $message->from->username;
$from_id = $message->from->id;
$name = $message->from->first_name;
if($text == '/start'){
bot('sendMessage', [
'chat_id' => $chat_id,
'text'=>"مرحبا بك $name

▪ في بوت تحميل سورس الموقع 

▫ الان يمكن تحميل سورس اي موقع

▪ في *Google* ونشاء موقعك

▫ في سورس جاهز بدون اي عناء

▪ السورس ستكون في لغه *HTML*",
'parse_mode'=>'MarkDown',
'reply_markup'=>json_encode([
'keyboard'=>[
[
['text'=>"تحميل سورس موقع ┇🌐"]
],
[
['text'=>"تعليمات البوت ┇👩‍💻"],
],
[
['text'=>"⁦⁦𝐀𝐇𝐌𝐄𝐃 𝐇𝐔𝐍𝐓𝐄𝐑℡ ̇༗"]
],
]
])
]);
}
if($text == "تحميل سورس موقع ┇🌐"){
file_put_contents("data/$from_id/hunter2.txt","dansite");
bot('sendMessage',[
 'chat_id'=>$chat_id,
 'text'=>"حسنا ارسل لي رابط الموقع الان 
ويجب ان يبدا بـ http او https ┇🌐",
 'parse_mode'=>"html",
'reply_markup'=>json_encode([
'keyboard'=>[
[
['text'=>"رجوع ⏪"]
],
]
])
]);
}
elseif($hunter == 'dansite'){
$dan = file_get_contents("$text");
file_put_contents("data/$from_id/q.html", $dan);
file_put_contents("data/$from_id/hunter2.txt","djsjshhwhah");
    bot('senddocument',[
        'chat_id'=>$chat_id,
        'document'=>new CURLFile("data/$from_id/q.html"),
        'caption'=>"ممتاز تم تحميل سورس الموقع 📥\n رابط الموقع\n$text",
         'parse_mode'=>"MarkDown",
 'reply_markup'=>json_encode([
'inline_keyboard'=>[
[
['text'=>"⁦⁦𝐀𝐇𝐌𝐄𝐃 𝐇 𝐔𝐍𝐓𝐄𝐑℡ ̇༗",'url'=>"t.me/x_q_9"]
]
]
])
 ]);
}
if($text == "رجوع ⏪"){
file_put_contents("data/$from_id/hunter2".txt,"");
file_put_contents("mirtm.txt","");
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"تم الرجوع للقائمه الرئيسيه 🔙",
'parse_mode'=>"markDown",
'reply_markup'=>json_encode([
'keyboard'=>[
[
['text'=>"تحميل سورس موقع ┇🌐"]
],
[
['text'=>"تعليمات البوت ┇👩‍💻"],
],
[
['text'=>"⁦⁦𝐀𝐇𝐌𝐄𝐃 𝐇𝐔𝐍𝐓𝐄𝐑℡ ̇༗"]
],
]
])
]);
}
if($text == "𝐀𝐇𝐌𝐄𝐃 𝐇𝐔𝐍𝐓𝐄𝐑℡ ̇༗"){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"تم كتابه ملف بوت باايدي مصريه بالكامل
البوت من \nAHMED HUNTER",
'parse_mode'=>"html",
'reply_markup'=>json_encode([
'inline_keyboard'=>[
[
['text'=>"𝐀𝐇𝐌𝐄𝐃 𝐇𝐔𝐍𝐓𝐄𝐑℡ ̇༗",'url'=>"http://telegram.me/x_q_9"]
],
]
])
]);
}
if($text == "تعليمات البوت ┇👩‍💻"){
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"عزيزي $name

▪ لتحميل سورس لموقع ما عليك 📥
▪ باتباع الخطوات وهي كلاتي ⤵️

▫اظغط علئ زر تحميل سورس موقع 🌐
▫️ يطلب منك البوت رابط للموقع 🌐
▫️عند ارسالك الرابط سيرسل لك البوت  ▫️ملف سورس الموقع جاهز في لغه *Html*",
 'parse_mode'=>"MarkDown",
 'reply_markup'=>json_encode([
'inline_keyboard'=>[
[
['text'=>"⁦⁦𝐀𝐇𝐌𝐄𝐃 𝐇 𝐔𝐍𝐓𝐄𝐑℡ ̇༗",'url'=>"t.me/x_q_9."]
]
]
])
 ]);
}
?>