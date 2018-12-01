# coding: utf-8

import argparse
import os
import commands
from urllib import unquote
import datetime

import requests
from googletrans import Translator


def showoutput(result):
    os.environ['result'] = result
    disk_prefix = commands.getoutput('osascript -e \'path to desktop as text\'').split(':')[0]
    icon_path = disk_prefix + os.getcwd().replace('/', ':') + ':gt.png'

    script = '\'display dialog "%s" with icon alias ("%s") with title "Google Translate" buttons {"Copy", "OK"} default button "OK" cancel button "Copy"\'' % (result, icon_path)
    os.system('osascript -e {}'.format(script))

# service_urls = ['translate.google.cn']
# translator = Translator(service_urls=service_urls)

# input = 'hello'
# result = translator.translate(input, dest='zh-CN').text.encode('utf-8')

# showoutput(result)


def calc_version(version_num_str):
    version = version_num_str.strip().split('.')
    if len(version) == 2:
            version = int(version[0]) * 100 + int(version[1]) * 10
    elif len(version) == 3:
            version = int(version[0]) * 100 + int(version[1]) * 10 + int(version[2])
    return version

def check_update():
    now_time = datetime.datetime.today()
    now_year, now_month, now_day = now_time.year, now_time.month, now_time.day
    now_time_stamp = '{}-{}-{}'.format(now_year, now_month, now_day)
    if now_day % 1 == 0:
        check = open('check', 'r').read().strip()
        print check
        if check != now_time_stamp:
            open('check', 'w').write(now_time_stamp)

            version_url = 'https://github.com/wizyoung/googletranslate.popclipext/blob/dev_pashua/src/version?raw=true'
            version_response = requests.get(version_url)
            if version_response.status_code == 200:
                remote_version_str = version_response.content
                remote_version = calc_version(remote_version_str)
                current_version_str = open('./version', 'r').read()
                current_version = calc_version(current_version_str)

                if remote_version > current_version:
                    script = '\'display dialog "Found a new version %s -- Your current version is %s.\n\nClick OK to download." with title "Check Update" buttons {"Cancel", "OK"} default button "OK" cancel button "Cancel"\'' % (remote_version_str, current_version_str)
                    btn_res = commands.getoutput('osascript -e {}'.format(script))
                    if btn_res.startswith('button'):
                        import webbrowser
                        webbrowser.open('https://github.com/wizyoung/googletranslate.popclipext/releases')



check_update()




