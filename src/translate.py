# coding: utf-8
import argparse
import os
from urllib import unquote
import subprocess
import datetime

import requests
from googletrans import Translator

def Pashua_run(result, show_pronounce, config_data=None):
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

        """.format(result.replace('\n', '[return]'))
        if show_pronounce == '1':
            config_data += """
            pronc_button.type = button
            pronc_button.label = Pronounce
            pronc_button.tooltip = Click to get the pronunciation of the selected sentences. Currently only support English.
            """
    result, _ = s.communicate(input=config_data)
    # Parse result
    d = {}
    for line in result.decode('utf8').splitlines():
        if '=' in line: 
            k, _, v = line.partition('=')
            d[k] = v.rstrip()
    return d


def shelloutput(src, show_pronounce, result):
    os.environ['result'] = result
    ret = Pashua_run(result, show_pronounce)
    if ret['copy_button'] == '1':
        os.system('echo "$result" | /usr/bin/pbcopy')
    if show_pronounce == '1':
        if ret['pronc_button'] == '1':
            os.system('say --voice="Samantha" ' + src)


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
    if now_day % 7 == 0:
        check = open('check', 'r').read().strip()
        if check != now_time_stamp:
            open('check', 'w').write(now_time_stamp)

            version_url = 'https://github.com/wizyoung/googletranslate.popclipext/blob/master/src/version?raw=true'
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

                    # default ok button
                    ok_button.type = defaultbutton

                    cancel_button.type = button
                    cancel_button.label = Cancel
                    """.format(remote_version_str, current_version_str)
                    ret = Pashua_run(None, None, config_data)
                    if ret['ok_button'] == '1':
                        import webbrowser
                        webbrowser.open('https://github.com/wizyoung/googletranslate.popclipext/releases')


LANGUAGES = {
    'Afrikaans': 'af',
    'Albanian': 'sq',
    'Amharic': 'am',
    'Arabic': 'ar',
    'Armenian': 'hy',
    'Azerbaijani': 'az',
    'Basque': 'eu',
    'Belarusian': 'be',
    'Bengali': 'bn',
    'Bosnian': 'bs',
    'Bulgarian': 'bg',
    'Catalan': 'ca',
    'Cebuano': 'ceb',
    'Chichewa': 'ny',
    'Chinese_Simplified': 'zh-CN',
    'Chinese_Traditional': 'zh-TW',
    'Corsican': 'co',
    'Croatian': 'hr',
    'Czech': 'cs',
    'Danish': 'da',
    'Dutch': 'nl',
    'English': 'en',
    'Esperanto': 'eo',
    'Estonian': 'et',
    'Filipino': 'tl',
    'Finnish': 'fi',
    'French': 'fr',
    'Frisian': 'fy',
    'Galician': 'gl',
    'Georgian': 'ka',
    'German': 'de',
    'Greek': 'el',
    'Gujarati': 'gu',
    'Haitian_creole': 'ht',
    'Hausa': 'ha',
    'Hawaiian': 'haw',
    'Hebrew': 'iw',
    'Hindi': 'hi',
    'Hmong': 'hmn',
    'Hungarian': 'hu',
    'Icelandic': 'is',
    'Igbo': 'ig',
    'Indonesian': 'id',
    'Irish': 'ga',
    'Italian': 'it',
    'Japanese': 'ja',
    'Javanese': 'jw',
    'Kannada': 'kn',
    'Kazakh': 'kk',
    'Khmer': 'km',
    'Korean': 'ko',
    'Kurdish': 'ku',
    'Kyrgyz': 'ky',
    'Lao': 'lo',
    'Latin': 'la',
    'Latvian': 'lv',
    'Lithuanian': 'lt',
    'Luxembourgish': 'lb',
    'Macedonian': 'mk',
    'Malagasy': 'mg',
    'Malay': 'ms',
    'Malayalam': 'ml',
    'Maltese': 'mt',
    'Maori': 'mi',
    'Marathi': 'mr',
    'Mongolian': 'mn',
    'Myanmar': 'my',
    'Nepali': 'ne',
    'Norwegian': 'no',
    'Pashto': 'ps',
    'Persian': 'fa',
    'Polish': 'pl',
    'Portuguese': 'pt',
    'Punjabi': 'pa',
    'Romanian': 'ro',
    'Russian': 'ru',
    'Samoan': 'sm',
    'Scots_gaelic': 'gd',
    'Serbian': 'sr',
    'Sesotho': 'st',
    'Shona': 'sn',
    'Sindhi': 'sd',
    'Sinhala': 'si',
    'Slovak': 'sk',
    'Slovenian': 'sl',
    'Somali': 'so',
    'Spanish': 'es',
    'Sundanese': 'su',
    'Swahili': 'sw',
    'Swedish': 'sv',
    'Tajik': 'tg',
    'Tamil': 'ta',
    'Telugu': 'te',
    'Thai': 'th',
    'Turkish': 'tr',
    'Ukrainian': 'uk',
    'Urdu': 'ur',
    'Uzbek': 'uz',
    'Vietnamese': 'vi',
    'Welsh': 'cy',
    'Xhosa': 'xh',
    'Yiddish': 'yi',
    'Yoruba': 'yo',
    'Zulu': 'zu'}


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('query', nargs='?', default=None)
    parser.add_argument('--site', dest='site', nargs='?', default=None)
    parser.add_argument('--srclang', dest='srclang', nargs='?', default=None)
    parser.add_argument('--destlang', dest='destlang', nargs='?', default=None)
    parser.add_argument('--show_pronounce', dest='show_pronounce', nargs='?', default=None)
    args = parser.parse_args()

    site = args.site
    srclang = args.srclang
    destlang = args.destlang
    show_pronounce = args.show_pronounce
    query = args.query

    unquoted_query = unquote(query)
    query = unquoted_query.decode('utf-8')

    if site == 'translate.google.cn':
        service_urls = ['translate.google.cn']
    elif site == 'translate.google.com':
        service_urls = ['translate.google.com']

    translator = Translator(service_urls=service_urls)

    detectedlang = translator.detect(query).lang

    # not using 'if detectedlang != LANGUAGES[srclang]' for exceptions like
    # 'zh-CNja' and 'ja' are both Japanese
    if LANGUAGES[srclang] not in detectedlang:
        result = translator.translate(query, dest=LANGUAGES[srclang]).text.encode('utf-8')
    else:
        result = translator.translate(query, dest=LANGUAGES[destlang]).text.encode('utf-8')

    shelloutput(unquoted_query, show_pronounce, result)
    check_update()

