# coding: utf-8
import argparse
import os
import re
from urllib import unquote

import requests
from googletrans import Translator

def shelloutput(result, toclipboard, location):
    os.environ['result'] = result
    if location == 'topright':
        shell = 'exec ./dialog/Contents/MacOS/cocoaDialog bubble \
                --title "Translation Result" \
                --icon-file gt.png \
                --text "$result"'
    else:
        shell = 'rv=`./dialog/Contents/MacOS/cocoaDialog msgbox \
            --title "Google Translate" \
            --text "Translation Result" \
            --icon-file gt.png \
            --informative-text "$result" \
            --button1 "OK" --button3 "复制结果"` '
        shell = shell + '\n if [ "$rv" == "3" ]; then echo "$result" | /usr/bin/pbcopy ;fi'
    os.system(shell)
    if toclipboard == '1':
        os.system('echo "$result" |/usr/bin/pbcopy')

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
    parser.add_argument('--motherlang', dest='motherlang', nargs='?', default=None)
    parser.add_argument('--destlang', dest='destlang', nargs='?', default=None)
    parser.add_argument('--toclipboard', dest='toclipboard', nargs='?', default=None)
    parser.add_argument('--location', dest='location', nargs='?', default=None)
    args = parser.parse_args()

    site = args.site
    motherlang = args.motherlang
    destlang = args.destlang
    toclipboard = args.toclipboard
    location = args.location
    query = args.query

    query = unquote(query)
    query = query.decode('utf-8')

    if site == 'translate.google.cn':
        service_urls = ['translate.google.cn']
    elif site == 'translate.google.com':
        service_urls = ['translate.google.com']

    translator = Translator(service_urls=service_urls)

    detectedlang = translator.detect(query).lang

    # not using 'if detectedlang != LANGUAGES[motherlang]' for exceptions like
    # 'zh-CNja' and 'ja' are both Japanese
    if LANGUAGES[motherlang] not in detectedlang:
        result = translator.translate(query, dest=LANGUAGES[motherlang]).text.encode('utf-8')
    else:
        result = translator.translate(query, dest=LANGUAGES[destlang]).text.encode('utf-8')

    shelloutput(result, toclipboard, location)

