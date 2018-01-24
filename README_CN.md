# Google Translate(PopClipExtension)

[English Version](https://github.com/wizyoung/googletranslate.popclipext/blob/master/README.md)

一个免费的谷歌翻译popclip插件，基于[Googletrans Python API](https://github.com/ssut/py-googletrans) 和[cocoaDialog](https://cocoadialog.com/)制作。

## 1. 预览

- 英译中

  ![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/en2cn.gif)

- 中译英

  ![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/cn2en.gif)

  **右上角Bubble弹窗默认4秒后自动消失，若鼠标移动到Bubble内，则不会自动消失。**


## 2. 设置

- `Google Translate Site`: 要使用的谷歌翻译服务器。墙内的朋友请选择`translate.google.cn`，墙外的选择`translate.google.com`


  - `Destination Language` 和`Mother Language`: 目标外语和母语。程序将对划中的语言进行检测，若检测的语言非母语，则翻译为母语；若检测的语言为母语，则翻译为目标外语。


  - `Output Window Location`：选择翻译结果是在右上角显示，还是屏幕中央弹窗显示。默认前者。

  - 若勾选`Copy the results`每次翻译的结果将自动复制到剪贴板，默认该选项关闭。

    ![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/screenshots/settings.png?raw=true)

- 若要后期更改设置，点击popclip下拉列表，再点击最下面的笔标记，会看到`Google Translate`插件右边有个齿轮图标，点击进去即可修改。


## 3. 安装

从 [Releases](https://github.com/wizyoung/googletranslate.popclipext/releases) 下载的文件，双击即可完成安装。

## 4. TODO

- [ ] 翻译结果随鼠标显示在文字旁
- [ ] 自动更新机制

## 5. 致谢

- [Googletrans Python API](https://github.com/ssut/py-googletrans): 一个免费的谷歌翻译第三方 Python API。
- [cocoaDialog](https://cocoadialog.com/): 简单通过命令行生成 macOS 对话框。
- [Turbo_祥](https://weibo.com/u/2627732300?topnav=1&wvr=6&topsug=1) 和 [把那该死的球传给我](https://weibo.com/u/2282786300?refer_flag=1001030101_): 两位朋友帮我设计和修改了图标，并对扩展做了相应的测试。

