// 메뉴
var lis = document.getElementById("menus").getElementsByTagName("li")
var pathname = window.location.pathname;
if(pathname == "/thebible/"){
    lis[0].className = "li_selcet";
}
else if(pathname == "/thebible/read/"){
    lis[1].className = "li_selcet";
}
else if(pathname == "/thebible/read/search/"){
    lis[2].className = "li_selcet";
}

var window_background = document.getElementById("window_background");
if(pathname == "/users/login/"){
    window_background.style.display = "block";
}
else if(pathname == "/users/signup/"){
    window_background.style.display = "block";
}

// 창 닫기
function alert_off(){
    var window_background = document.getElementById("window_background");
    var alert_one_button_window = document.getElementById("alert_one_button_window");
    window_background.style.display = "none";
    alert_one_button_window.style.display = "none";
}

// 창 열기
function alert_on(){
    var window_background = document.getElementById("window_background");
    var alert_one_button_window = document.getElementById("alert_one_button_window");
    window_background.style.display = "block";
    alert_one_button_window.style.display = "block";
}