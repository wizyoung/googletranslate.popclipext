# Google Translate(PopClipExtension)
[中文说明](https://github.com/wizyoung/googletranslate.popclipext/blob/master/README_CN.md)

An unofficial free Google translate PopClip Extension based on [Googletrans Python API](https://github.com/ssut/py-googletrans) and [cocoaDialog](https://cocoadialog.com/).

## Preview

- English to Chinese (Simplified):

  ![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/en2cn.gif)

- Chinese (Simplified) to English:

  ![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/cn2en.gif)

  The pop-up Bubble containing translation results will disappear automatically after 4 sec unless you move the mouse into it.

## Settings

- `Google Translate Site`: Choosing from `translate.google.cn` (default) or `translate.google.com`. The `.cn` server is for users in mainland China where the `.com` server is blocked by the government. 
- `Destination Language` and `Mother Language`: If the selected text is not the `Mother Language`, the words will be translated to the `Mother Language`. Else, the words will be translated to the `Destination Language`.
- `Output Window Location`: Where the result window will be. Choosing from `topright `(default) or `center`.
- `Copy the results`: Whether to copy the results to clipboard after the translation.

![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/settings.png?raw=true)

You can change all these settings by clicking the pencil shaped icon at the bottom of the popclip drop-down list.

## Install

Download the file from [Releases](https://github.com/wizyoung/googletranslate.popclipext/releases) and double click to install the extension.

## TODO

- [ ] Result Bubble beside the selected words.
- [ ] Auto Update.

## Thank You

- [Googletrans Python API](https://github.com/ssut/py-googletrans): A **free** and **unlimited** python library that implemented Google Translate API.
- [cocoaDialog](https://cocoadialog.com/): Create macOS dialogs from the command line easily.
- [Turbo_祥](https://weibo.com/u/2627732300?topnav=1&wvr=6&topsug=1) and [把那该死的球传给我](https://weibo.com/u/2282786300?refer_flag=1001030101_): They helped design the beautiful icon and test this extension.

