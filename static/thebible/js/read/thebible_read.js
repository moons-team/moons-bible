// 필터기능
function select(num) {
    var selectList = document.getElementsByClassName("select-list");
    var img = document.getElementsByClassName("select_img");
    for (i = 0, len = selectList.length; i < len; i++){
        if (selectList[i].classList.contains('none') && i == num) {
            selectList[i].classList.remove('none');
            img[i].classList.add('rorate180');
        }
        else {
            selectList[i].classList.add('none');
            img[i].classList.remove('rorate180');
            }
        }
    }

// 아무곳이나 클릭시 열렸던 필터를 닫기
window.onclick=function(e){
    if(!e.target.matches('#fil-click')){
        var dropdown = document.getElementsByClassName("select-list");
        var img = document.getElementsByClassName("select_img");
        for(i = 0, len = dropdown.length; i < len; i++){
            if (dropdown[i].classList.contains('none')) {}
            else {
                dropdown[i].classList.add('none');
                img[i].classList.remove('rorate180');
                }
            }
        }
    }

// 좋아요 백앤드 처리
function ApiLike(is_active, elem, csrfmiddlewaretoken){
    var verseid = elem.getAttribute('name')
    var data = {}
    data['is_active'] = is_active
    data['verseid'] = verseid
    data['csrfmiddlewaretoken'] = csrfmiddlewaretoken
    $.ajax({
        type : "POST",
        dataType: "json",
        url : "/thebible/api/like/",
        data : data,
        success: function (response){
            if(response == 1){
                alert("좋아요 목록에 저장되었습니다!")
            }
            else if(response == 2){
                var login = confirm("로그인이 필요한 기능입니다 로그인 하시겠습니까?")
                if (login == true){
                    window.location.href="/users/login/?next_path=" + window.location.pathname
                }
                else{
                    elem.classList.remove('like-text');
                    is_active = true;
                }
            }
            else if(response == 0){
                alert("좋아요 목록에서 제거되었습니다!")
            }
        },
        error: function (err){
            alert("서버 오류")
        }
    });
}

// 좋아요 클릭 처리
function like(elem, csrfmiddlewaretoken) {
    if (elem.classList.contains('like-text')){
        elem.classList.remove('like-text');
        is_active = true;
        }
    else{
        elem.classList.add('like-text');
        is_active = false;
        }
    ApiLike(is_active, elem, csrfmiddlewaretoken)
    }
    