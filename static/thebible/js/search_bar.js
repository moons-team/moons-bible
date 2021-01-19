// 파라메터 가져오기
function getSearchString(key, Url) {
    var str = Url;
    str = str.substring(1, str.length);
    var arr = str.split("&");
    var obj = new Object();
    for (var i = 0; i < arr.length; i++) {
        var tmp_arr = arr[i].split("=");
        obj[decodeURIComponent(tmp_arr[0])] = decodeURIComponent(tmp_arr[1]);
    }
    return obj[key];
}

// 현재 버전
window.onload = function(){
    var search = window.location.search;
    var search_version_name = getSearchString('search_version', search);
    var version_name = document.getElementsByName("version_name")[0];
    var search_version = document.getElementsByName("search_version")[0];
    if(search_version_name == undefined){
        version_name.innerHTML = "개역한글";
        search_version.value = "개역한글";
    }
    else{
        version_name.innerHTML = search_version_name;
        search_version.value = search_version_name;
    }
}

// 검색 버전 체인지
function search_version(elem){
    var version_name = document.getElementsByName("version_name")[0];
    var search_version = document.getElementsByName("search_version")[0];
    version_name.innerHTML = elem.innerHTML;
    search_version.value = elem.innerHTML;
}

