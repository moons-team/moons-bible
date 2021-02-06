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

// 검색 버전 체인지
function search_version(elem){
    var version_name = document.getElementsByName("version_name")[0];
    var search_version = document.getElementsByName("search_version")[0];
    version_name.innerHTML = elem.innerHTML;
    search_version.value = elem.innerHTML;
}

