# coding: utf-8

import os
import re
import subprocess

from googletrans import Translator
import requests
import datetime


def Pashua_run(result, config_data=None):
    Pashua_path = './Pashua/Contents/MacOS/Pashua'
    s=subprocess.Popen([Pashua_path,  "-"],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
    if not config_data:
        config_data = """
        # set the window title
        *.title = Google Translate
        *.floating = 1

        # the translation results
        result.type = text
        result.text = {}
        result.width = 400

        # # default ok button
        # ok_button.type = defaultbutton

        copy_button.type = button
        copy_button.label = Copy
        copy_button.tooltip = Click to copy the translated results.

        pronc_button.type = button
        pronc_button.label = Pronounce
        pronc_button.tooltip = Click to get the pronunciation of the selected sentences.
        """.format(result.replace('\n', '[return]'))
    result, _ = s.communicate(input=config_data)
    # Parse result
    d = {}
    for line in result.decode('utf8').splitlines():
        if '=' in line: 
            k, _, v = line.partition('=')
            d[k] = v.rstrip()
    return d


def shelloutput(result):
    os.environ['result'] = result
    ret = Pashua_run(result)
    if ret['copy_button'] == '1':
        os.system('echo "$result" | /usr/bin/pbcopy')

# service_urls = ['translate.google.cn']
# translator = Translator(service_urls=service_urls)

# input = 'Concretely, we introduce a joint formulation of a Qlearning agent [29] and a class recognition model. In contrast to related webly-supervised approaches [7, 19], the data collection and classiﬁer training steps are not disjoint but rather integrated into a single uniﬁed framework. The agent selects web search examples to label as positives, which are then used to train the recognition model. A signiﬁcant challenge is the choice of the state representation, and we introduce a novel representation based on the distribution of classiﬁer scores output by the recognition model. At training time, the model uses a dataset of labeled training classes to learn a data labeling policy, and at test time the model can use this policy to label noisy web data for new unseen classes.'

# result = translator.translate(input, dest='zh-CN').text.encode('utf-8')

# shelloutput(result)


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
    if now_day % 4 == 0:
        check = open('check', 'r').read()
        if check is not now_time_stamp:
            open('check', 'w').write(now_time_stamp)

            version_url = 'https://github.com/wizyoung/workflows.kyoyue/blob/master/version?raw=true'
            version_response = requests.get(version_url)
            if version_response.status_code == 200:
                remote_version_str = version_response.content
                remote_version = calc_version(remote_version_str)
                current_version_str = open('./version', 'r').read()
                current_version = calc_version(current_version_str)

                if remote_version > current_version:
                    config_data = """
                    *.title = Check Updates
                    *.floating = 1

                    # the translation results
                    result.type = text
                    result.text = Found a new version {} -- your current version is {}. [return]Click 'OK' to download. 
                    result.width = 400

                    # # default ok button
                    # ok_button.type = defaultbutton

                    cancel_button.type = button
                    cancel_button.label = Cancel
                    """.format(remote_version_str, current_version_str)
                    ret = Pashua_run(None, config_data)
                    if ret['ok_button'] == '1':
                        import webbrowser
                        webbrowser.open('https://github.com/wizyoung/googletranslate.popclipext/releases')

check_update()




