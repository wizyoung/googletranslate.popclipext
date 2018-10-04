# Google Translate(PopClipExtension)

[English Version](https://github.com/wizyoung/googletranslate.popclipext/blob/master/README.md)

一个免费的谷歌翻译popclip插件，基于[Googletrans Python API](https://github.com/ssut/py-googletrans) 和[Pashua](https://github.com/BlueM/Pashua)制作。

## 预览

- 英译中

<img src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/en2cn.gif?raw=true" width="70%" height="70%" />

- 中译英

<img src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/cn2en.gif?raw=true" width="70%" height="70%" />

  点击`Copy`复制翻译结果。

  点击`Pronounce`获取所选文字发音。（目前只支持英文）


## 设置

- `Google Translate Site`: 要使用的谷歌翻译服务器。墙内的朋友请选择`translate.google.cn`，墙外的选择`translate.google.com`


  - `Destination Language` 和`Source Language`: 目标外语(destination language)和母语(source language)。程序将对划中的语言进行检测，若检测的语言非母语，则翻译为母语；若检测的语言为母语，则翻译为目标外语。
  - `Show Pronounce Button`: 是否显示发音按钮。

<div align=center><img width="30%" height="30%" src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/settings.png?raw=true"/></div>


- 若要后期更改设置，点击popclip下拉列表，再点击最下面的铅笔标记，会看到`Google Translate`插件右边有个齿轮图标，点击进去即可修改。


## 安装

从 [Releases](https://github.com/wizyoung/googletranslate.popclipext/releases) 下载的文件，双击即可完成安装。

版本 2.1 后引入了自动更新提醒功能，默认每7天检测一次更新。

## 常见问题

- 选中文字后，PopClip 弹窗不出现？

  这是 PopClip 的 bug。你可以通过 AppleScrip 手动唤出 PopClip 弹窗: `tell application "PopClip" to appear`。我使用 BetterTouchTool 实现这个功能，即绑定三指上滑手势为调用该 AppleScript 脚本。

## 致谢

- [Googletrans Python API](https://github.com/ssut/py-googletrans): 一个免费的谷歌翻译第三方 Python API。
- [Pashua](https://github.com/BlueM/Pashua): 使用脚本语言调用原生 macOS 对话框。
- [Turbo_祥](https://weibo.com/u/2627732300?topnav=1&wvr=6&topsug=1) 和 [把那该死的球传给我](https://weibo.com/u/2282786300?refer_flag=1001030101_): 两位朋友帮我设计和修改了图标，并对扩展做了相应的测试。

## 捐助

如果你认为此扩展对你帮助很大，不放请我喝杯咖啡吧：

<img src="https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/donation.png?raw=true" width="60%" height="60%" />