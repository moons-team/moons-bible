// 키워드 색상 변환
var search_keyword_name = document.getElementById('keyword').innerHTML.replaceAll('"', "")
var tmp = document.getElementById('search_result_content').innerHTML
var chage_keyword = tmp.replace(new RegExp(search_keyword_name, 'g'), '<span style="color:#e27917">'+ search_keyword_name +'</span>');
document.getElementById('search_result_content').innerHTML = chage_keyword