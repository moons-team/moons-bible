// 로그인 정보 기억하기
window.onload = function(){
var oForm = document.getElementById('loginForm');
var oUser = document.getElementById('user');
var oPswd = document.getElementById('pswd');
var oRemember = document.getElementById('remember');

if(getCookie('user') && getCookie('pswd')){
    oUser.value = getCookie('user');
    oPswd.value = getCookie('pswd');
    oRemember.checked = true;
}
oRemember.onchange = function(){
    if(!this.checked){
    delCookie('user');
    delCookie('pswd');
    }
};
oForm.onsubmit = function(){
    if(remember.checked){ 
    setCookie('user',oUser.value,30);
    setCookie('pswd',oPswd.value,30);
    }
};
};
function setCookie(name,value,day){
var date = new Date();
date.setDate(date.getDate() + day);
document.cookie = name + '=' + value + ';expires='+ date;
};
function getCookie(name){
var reg = RegExp(name+'=([^;]+)');
var arr = document.cookie.match(reg);
if(arr){
    return arr[1];
}else{
    return '';
}
};
function delCookie(name){
setCookie(name,null,-1);
};


// x클릭시 끄기
// function login_x_click(){
//     var window_background = document.getElementById("window_background");
//     var window = document.getElementById("window_login");
//     window_background.style.display = "none";
//     window.style.display = "none";
//     }