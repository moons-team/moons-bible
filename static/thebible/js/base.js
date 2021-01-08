// 메뉴
var lis = document.getElementById("menus").getElementsByTagName("li")
var pathname = window.location.pathname;
if(pathname == "/thebible/home/"){
    lis[0].className = "li_selcet";
}
else if(pathname == "/thebible/read/"){
    lis[1].className = "li_selcet";
}

var window_background = document.getElementById("window_background");
if(pathname == "/users/login/"){
    window_background.style.display = "block";
}
if(pathname == "/users/signup/"){
    window_background.style.display = "block";
}