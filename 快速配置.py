import time,os
import pyautogui as pag
import json

#x, y = pag.position()
#获取鼠标的坐标
import json
 
#保存json文件
def save_json(save_path,data):
    assert save_path.split('.')[-1] == 'json'
    with open(save_path,'w') as file:
        json.dump(data,file)

#“screensize”: 屏幕分辨率【x,y】
#“randompos”: A选项的坐标【x,y】
#“nextpos”: 选择错误选项时,’下一个’按钮的坐标【x,y】
#“shotrange”: 题目单词的范围（注意,只要加粗黑字题目的信息,不要把下一行的音标也框进去了）【左上角x,左上角y,右下角x,右下角y】
#“scanrange”: 选项的范围（注意,该范围是严格的,即以a选项的上边框,d选项的下边框为范围）【左上角x,左上角y,右下角x,右下角y】
#“y_dist”: 两个选项边框间的间隙宽度【y】
#“botton_dist”: 选项按钮的宽度【y】


# 获取屏幕的尺寸
screenWidth, screenHeight = pag.size()
print(f'屏幕尺寸为：{screenWidth}*{screenHeight}')

print('现在全屏打开西柚的‘看词选义’或‘看义选词’作业,完成如下配置')

#获取A选项位置
input('现在,将鼠标放置A选项上,按下回车键确认位置')
randx, randy = pag.position()
print(f'好,A选项的位置是({randx},{randy})')

#获取下一个按钮位置
input('现在,选择一个错误的答案,右下角将会出现“下一个按钮”,将鼠标放置此按钮上,按下回车键确认位置')
nextx, nexty = pag.position()
print(f'好,‘下一个按钮’的位置是({nextx},{nexty})')

#获取题目单词的范围
input('现在,将鼠标放置在题目文字的左上角,按下回车键确认位置')
shotx1, shoty1 = pag.position()
input('好,接下来鼠标放置在题目文字的右下角,按下回车键确认位置（注意,只要加粗黑字题目的信息,不要把下一行的音标也框进去了）')
shotx2, shoty2 = pag.position()
print(f'好,题目的范围是({shotx1},{shoty1},{shotx2},{shoty2})')

#获取选项单词的范围
input('现在,将鼠标放置在选项的左上角,按下回车键确认位置(注意,该范围是严格的,即以a选项的上边框,d选项的下边框为范围)')
scanx1, scany1 = pag.position()
input('好,接下来鼠标放置在选项的右下角,按下回车键确认位置')
scanx2, scany2 = pag.position()
print(f'好,选项的范围是({scanx1},{scany1},{scanx2},{scany2})')

#获取两个选项边框间的间隙宽度
input('现在准备获取两个选项边框间的间隙宽度,将鼠标放置在a选项的下边框,按下回车键确认位置')
x1, y1 = pag.position()
input('好,接下来鼠标放置在b选项的上边框,按下回车键确认位置')
x2, y2 = pag.position()
y_dist = y2 - y1
print(f'好,两个选项边框间的间隙宽度是{y_dist}')
botton_dist = y1 - scany1
print(f'好,按钮间的间隙宽度是{botton_dist}')

print('坐标录入完毕，正在处理中')

config = {
  "screensize": [screenWidth,screenHeight],
  "randompos": [randx,randy],
  "nextpos": [nextx,nexty],
  "shotrange": [shotx1,shoty1,shotx2,shoty2],
  "scanrange": [scanx1,scany1,scanx2,scany2],
  "y_dist": y_dist,
  "botton_dist": botton_dist
}
save_json('config.json',config)

print(config)
print(f'你的配置文件已保存！现在你可以启动‘看词选义’和‘看义选词’程序了')
input('回车退出')