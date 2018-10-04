# Google Translate(PopClipExtension)
[中文说明](https://github.com/wizyoung/googletranslate.popclipext/blob/master/README_CN.md)

An unofficial free Google translate PopClip Extension based on [Googletrans Python API](https://github.com/ssut/py-googletrans) and [Pashua](https://github.com/BlueM/Pashua).

## Preview

- English to Chinese (Simplified):
  
<div align=center><img width="70%" height="70%" src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/en2cn.gif?raw=true"/></div>


- Chinese (Simplified) to English:

<div align=center><img width="70%" height="70%" src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/cn2en.gif?raw=true"/></div>

  Click `Copy` to copy the translated results.

  Click `Pronounce` to get the pronouncaton of the selected sentences. (Currently only English supported.)

## Settings

- `Google Translate Site`: Choosing from `translate.google.cn` (default) or `translate.google.com`. The `.cn` server is for users in mainland China where the `.com` server is blocked by the government. 
- `Destination Language` and `Source Language`: If the selected text is not the `Source Language`, the sentences will be translated to the `Source Language`. Otherwise, the  sentences will be translated to the `Destination Language`.
- `Show Pronounece Button`: Whether to show the pronounce button. Default to False.

<div align=center><img width="30%" height="30%" src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/settings.png?raw=true"/></div>


You can change all these settings by clicking the pencil shaped icon at the bottom of the popclip drop-down list.

## Install

Download the file from [Releases](https://github.com/wizyoung/googletranslate.popclipext/releases) and double click to install the extension.

The auto update feature is new to version 2.1, so the extension will check for updates once every seven days.

## Frequently asked questions

- Sometimes the pop-up window of PopClip just doesn't show up when I select some sentences.

It's the bug of PopClip. You can manually  trigger PopClip window to appear by AppleScript: `tell application "PopClip" to appear`. And I'm using BetterTouchTool to achieve this function by binding `3 Finger Swipe Up` gesture to run this AppleScript.

## Thanks

- [Googletrans Python API](https://github.com/ssut/py-googletrans): A **free** and **unlimited** python library that implemented Google Translate API.
- [Pashua](https://github.com/BlueM/Pashua): Native macOS dialogs for scripting languages.
- [Turbo_祥](https://weibo.com/u/2627732300?topnav=1&wvr=6&topsug=1) and [把那该死的球传给我](https://weibo.com/u/2282786300?refer_flag=1001030101_): They helped design the beautiful icon and test this extension.

## Donation

If this extension helps you a lot, you can support me by:

<div align=center><img width="60%" height="60%" src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/donation.png?raw=true"/></div>

