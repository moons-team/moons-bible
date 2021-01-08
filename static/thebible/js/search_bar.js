var obox = document.getElementById("box");
var odown = document.getElementById("down");
var oli = document.getElementById("down").getElementsByClassName("select");
var img = document.getElementById("search_version").getElementsByTagName("img")[0];
console.log(oli);

obox.onclick = function(){
    odown.style.display = "block";
    img.style.transform = "rotate(180deg)";
    for(var i=0;i<oli.length;i++){
        oli[i].n = i;
        oli[i].onclick = function(){
            obox.innerHTML = this.innerHTML;
            odown.style.display = "none";
            img.style.transform = "rotate(0deg)";
        }
    }
}