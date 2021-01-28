import multiprocessing, signal
import sys
import time
from save_db import save_to_db

is_exit = False
print("멀티프로세싱 시작...")
print('cpu코어 개수:' + str(multiprocessing.cpu_count()) + "개")

def my_code(version):
    print('버전 "{}" 크롤링 시작...\n'.format(version['name']))
    save_to_db(version['value'], version['language'], version['name'])
    print('버전 "{}" 작업 완료!'.format(version['name']))

def quit(signum, frame):
    print("멀티프로세싱 종료...")
    sys.exit()

def start_multiprocessing(version_list):
    for version in version_list[:]:
        try:
            signal.signal(signal.SIGINT, quit)
            signal.signal(signal.SIGTERM, quit)
            p = multiprocessing.Process(target=my_code, args=(version,))
            p.start()
        except Exception:
            pass


version_list = [
    {"language": "0", "name": "0", "value": "B_GAE"},
    {"language": "0", "name": "1", "value": "B_RHV"},
    {"language": "0", "name": "2", "value": "B_COGNEW"},
    {"language": "0", "name": "3", "value": "B_SAENEW"},
    {"language": "0", "name": "4", "value": "B_HDB"},
    {"language": "1", "name": "5", "value": "BIBLE_cgb"},
    {"language": "1", "name": "6", "value": "BIBLE_cb5"},
    # {"language": "2", "name": "7", "value": "B_NIV"},
    # {"language": "2", "name": "8", "value": "B_KJV"},
    # {"language": "2", "name": "9", "value": "B_NASB"},
]

start_multiprocessing(version_list)
time.sleep(1)
# print('프로세스 {}개 생성 완료\n'.format(len(multiprocessing.active_children())))