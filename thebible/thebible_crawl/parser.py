from bs4 import BeautifulSoup
import re

# html소스 해석
def analysis_bible_source(page_source, version, title_num, language, version_name):
    bs_source = BeautifulSoup(page_source, 'html.parser')
    tables = bs_source.findAll("table")
    if version == "BIBLE_cgb" or version == "BIBLE_cb5":
        new_tables = tables[7:-3]
    else:
        new_tables = tables[9:-4]
    all_content = []
    num = 0
    for table in new_tables:
        if num == 0:
            # print(table)
            sub_title = table.findAll("td", {"class": "tkb"})[1].text
            title = re.findall(r"(.*?) ", sub_title)[1]
            chapter_num = re.findall(r" \d+", sub_title)[0]
            if title_num <= 39:
                if language == "0":
                    title_type = "0"
                elif version == "BIBLE_cgb":
                    title_type = "2"
                elif version == "BIBLE_cb5":
                    title_type = "4"
                elif language == "2":
                    title_type = "6"
            else:
                if language == "0":
                    title_type = "1"
                elif version == "BIBLE_cgb":
                    title_type = "3"
                elif version == "BIBLE_cb5":
                    title_type = "5"
                elif language == "2":
                    title_type = "7"
            num += 1
            continue
        else:
            ol = table.find("ol")
            lis = ol.findAll("li")
            for li in lis:
                try:
                    content = re.findall(r"(.*?)\n", li.text)[0].replace("\t", "")
                except:
                    content = li.text.replace("\t", "")

                one_content = {
                    "language": language,
                    "version_name": version_name,
                    "title_type": title_type,
                    "title_num": title_num,
                    "title": title,
                    "chapter_num": chapter_num,
                    "verse_num": num,
                    "verse": content,
                }
                num += 1
                all_content.append(one_content)
    return all_content