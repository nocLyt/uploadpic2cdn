# Just for Mac OS
# 1. you need run " brew install pngpaste " in console.
# 2. "pip install  qiniu"
# 2. have fun.

import qiniu
import datetime
import os
import sys
import atexit
import subprocess
import string


# Configure V
AK = "your Qiniu account's AKey'"
SK = "your Qiniu account's SKey "
BUCKET_NAME = "your Qiniu account's bucket name "
SAVE_PATH = "/Users/yiyi/wp/tmp"     # save the picture in the  path of your macOS
PNGPAST = "/usr/local/bin/pngpaste"  # the path of pngpaste
URL_TMP = "http://%s.qiniudn.com/%s"


def load_file(file_name, file_path):
    print "QiNiu Loading..."
    q = qiniu.Auth(AK, SK)
    token = q.upload_token(BUCKET_NAME, file_name)
    ret, info = qiniu.put_file(token, file_name, file_path)
    print "RET: ", ret
    print "UPLOAD_INFO : ", info
    print "URL:"
    print (URL_TMP % (BUCKET_NAME, file_name))



def save_paste_pic(file_path=None):
    file_name = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S.png')
    file_path = os.path.join(SAVE_PATH, file_name)
    atexit.register(lambda x: os.remove(x) if os.path.exists(x) else None, file_path)
    info = subprocess.call([PNGPAST, file_path])
    if info == 1:
        print "You clipboard have no picture!"
        exit();
    print "Get picture from your clipboard. ", file_path
    return [file_name, file_path]


def run():
    file_name, file_path = save_paste_pic()
    print "File Size: ", str(os.path.getsize(file_path))
    load_file(file_name, file_path)


run()
