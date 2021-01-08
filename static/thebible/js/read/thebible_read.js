// 필터기능
function select(num) {
    var selectList = document.getElementsByClassName("select-list")[num];
    var img = document.getElementsByClassName("select_img")[num];
    if (selectList.style.display === "none") {
        selectList.style.display = "block";
        img.style.transform = "rotate(180deg)";
    } else {
        selectList.style.display = "none";
        img.style.transform = "rotate(0deg)";
        }
    }

// 아무곳이나 클릭시 열렸던 필터를 닫기
window.onclick=function(e){
    if(!e.target.matches('.span')){
        var dropdown = document.getElementsByClassName("select-list");
        var img = document.getElementsByClassName("select_img");
        for(i = 0, len = dropdown.length; i < len; i++){
            if (dropdown[i].style.display = "block") {
            dropdown[i].style.display = "none";
            img[i].style.transform = "rotate(0deg)";
                }
            }
        }
    }

// 좋아요 백앤드 처리
function ApiLike(is_active, elem){
    const data = {};
    verseid = elem.getAttribute('name');
    data['is_active'] = is_active;
    data['verseid'] = verseid
    $.ajax({
        type    : "POST",
        dataType: "json",
        url     : "/thebible/api/like/",
        data    : data,
        success: function (data) {
            alert(1)
        },
    })
}

// 좋아요 클릭 처리
function like(elem) {
    if (elem.classList.contains('like-text')){
        elem.classList.remove('like-text');
        is_active = true;
        }
    else{
        elem.classList.add('like-text');
        is_active = false;
        }
    ApiLike(is_active, elem)
    }
    