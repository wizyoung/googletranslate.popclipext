# googletranslate.popclipext
一个免费的谷歌翻译popclip插件。

### 1. 使用

- 使用效果：

  鼠标划中待翻译句子，点击翻译图标，右上角弹出翻译。

  **右上角Bubble弹窗默认4秒后自动消失，若鼠标移动到Bubble内，则不会自动消失。**

  - 英译中:

    ![](https://raw.githubusercontent.com/wizyoung/googletranslate.popclipext/master/3.gif)

  - 中译英:

    ![](https://raw.githubusercontent.com/wizyoung/googletranslate.popclipext/master/4.gif)

- 使用方法:

  初次使用，设置`Google Translate Site`，`Target Foreign Language`和`Output Window Location`字段，并勾选是否`复制结果到剪贴板`。

  - `Google Translate Site`: 要使用的谷歌翻译服务器。墙内的朋友请选择`translate.google.cn`，墙外的选择`translate.google.com`
  - `Target Foreign Language`: 目标外语。程序将对划中的语言进行检测，若为中文，则翻译为选中的目标外语；若为非中文，无论什么语言，一律翻译为中文。


  - `Output Window Location`：选择翻译结果是在右上角显示，还是屏幕中央弹窗显示。默认前者。

  - 若勾选`复制结果到剪贴板`每次翻译的结果将自动复制到剪贴板，默认该选项关闭。

    ![](https://github.com/wizyoung/googletranslate.popclipext/blob/master/1.png?raw=true)

- 若要后期更改设置，点击popclip下拉列表，再点击最下面的笔标记，会看到`Google Translate`插件右边有个齿轮图标，点击进去即可修改。


### 2. 致谢

- 翻译API：目前谷歌翻译API已经开始收费，想用爬虫去爬谷歌翻译网页版，却有TK校验值问题。网上大部分TK校验值破解方法均已失效。多亏[py-googletrans](https://github.com/ssut/py-googletrans)提供了稳定的TK校验值破解方法，才能做成这个插件。对它们的工作表示感谢
- 界面: 弹窗显示界面使用了[cocoaDialog](http://mstratman.github.io/cocoadialog/)。
- 图标: 感谢[linivor](https://github.com/linivor)和[lfcxlfcx](https://github.com/lfcxlfcx)同学对改插件图标提出中肯意见并帮忙修改，同时感谢[linivor](https://github.com/linivor)同学提供的软件测试服务。

### 3. 附件说明

本人同时制作了官方API版本的谷歌翻译popclip插件，需要的可Email联系本人。

### 4. 下载链接

[Release](https://github.com/wizyoung/googletranslate.popclipext/releases)


