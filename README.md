** 此文章同步保存在以下网站 ** 
[森的神秘空间](https://yhsome.github.io/2023/08/19/xiyouchooser)
[github](https://github.com/YHSome/xiyouchooser/)

# 功能简介
该脚本可以帮助你完成 [西柚英语](https://student.xiyouyingyu.com) 中烦人的看词选义和看义选词。
# 使用方法
## 第一步：安装python以及相应库
你需要安装的python库有
```
pytesseract
transformers
pillow
pyautogui
```
## 第二部，完成相应配置
打开 ``` ./config.json ``` ，填写相应配置。以下是配置文件的相关释义
**提示：**你可以使用 ``` ./显示鼠标坐标.py ``` 快速定位光标所处的像素的坐标
>"screensize": 屏幕分辨率【x,y】

>"randompos": A选项的坐标【x,y】

>"nextpos": 选择错误选项时，'下一个'按钮的坐标【x,y】

>"shotrange": 题目单词的范围（注意，只要加粗黑字题目的信息，不要把下一行的音标也框进去了）【左上角x,左上角y,右下角x,右下角y】

>"scanrange": 题目的范围（注意，该范围是严格的，即以a选项的上边框，d选项的下边框为范围）【左上角x,左上角y,右下角x,右下角y】

>"y_dist": 两个选项边框间的间隙宽度【y】

>"botton_dist": 选项按钮的宽度【y】

这个是1600x900分辨率下，谷歌浏览器全屏打开的设置示例
```
{
  "screensize": [1600,900],
  "randompos": [535,565],
  "nextpos": [1215,825],
  "shotrange": [500,180,970,225],
  "scanrange": [500,470,970,820],
  "y_dist": 15,
  "botton_dist": 55
}
```
这个是这个是1600x900分辨率下，谷歌浏览器（左）半屏打开向右拉到底的设置示例
```
{
  "screensize": [1600,900],
  "randompos": [350,565],
  "nextpos": [1025,825],
  "shotrange": [300,180,780,225],
  "scanrange": [300,537,780,795],
  "y_dist": 15,
  "botton_dist": 55
}
```

## 第三步，启动程序
你可以用cmd运行，也可以用vscode等ide运行文件
```cmd
$ python 看词选义v1.1.py
```
或者
```cmd
$ python 看义选词v1.0.py
```
**注意：首次启动时会从huggingface.com下载翻译模型，需要耐心等待，如果出现服务器拒绝连接的问题，请重新运行程序或选择适合的代理**

# 此脚本的不足
不幸的是，谷歌翻译在2022年9月停止了对中国大陆的翻译服务，所以我们只能采用huggingface提供的本地离线翻译模型。
由于基于本地的图像识别以及翻译模型，识别速度和准确度会随着电脑性能而有所不同。我的便携电脑cpu不太好，识别准确率只有70%左右。
~~~谁让我没钱买百度识别和百度翻译的的api呢~~~

# 未来的展望
目前只做了几个功能，会考虑以后更多功能的开发