print('引入资源中...')

#指明tesseract命令位置
import pytesseract
tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'
pytesseract.pytesseract.tesseract_cmd =tesseract_cmd

import time
import json
from transformers import pipeline, AutoModelWithLMHead, AutoTokenizer
import warnings
from PIL import ImageGrab
import string
import pyautogui
import os

def clear_terminal():
    # 判断操作系统类型
    if os.name == 'nt':  # Windows系统
        os.system('cls')
    else:  # Linux、macOS等系统
        os.system('clear')
    # 清空终端
    #clear_terminal()

#配置文件的格式：
#屏幕分辨率
#‘随机选指定的位置’
#‘下一步指定的位置’
#截图的范围
#识别的范围

with open('./config.json') as f:
    config = json.load(f)
# 获取配置项的值
screensize = config['screensize']
randompos = config['randompos']
nextpos = config['nextpos']
shotrange = config['shotrange']
scanrange = config['scanrange']
# 打印配置项的值
print(f'屏幕分辨率为{screensize}')
print(f'A选项坐标{randompos}')
print(f'下一个按钮的位置{nextpos}')
print(f'题目单词的范围{shotrange}')
print(f'四个选项的范围{scanrange}')
input('按回车开始')

warnings.filterwarnings ('ignore')
modelName = "DDDSSS/translation_en-zh"
print('正在加载翻译模型......')
model = AutoModelWithLMHead.from_pretrained(modelName)
tokenizer = AutoTokenizer.from_pretrained(modelName)
translation = pipeline('translation_zh_to_en',model=model,tokenizer=tokenizer)
print('加载完成')


while True:
    r = int(input('请输入还要多少个单词未完成'))
    #下面是主程序
    print('运行此程序时一定要固定西柚窗口的位置!')
    print('按CTRL+C中断程序!')
    print('三秒后开始运行')
    time.sleep(3)

    for i in range(1,r+1,1):
        #按照配置中截图的范围截屏，将截图保存在./saved/中
        clear_terminal()
        print(f"现在正在完成第{i}个单词")
        screensave = ImageGrab.grab(shotrange)
        screensave.save("./saved/screenshot.png")
        print('已截屏,正在处理...')

        #识别出截屏的内容（已知识别的内容只有中文或英文）
        # 设置语言参数为中文简体
        lang = 'eng'
        # 进行文字识别
        text = pytesseract.image_to_string(screensave, lang=lang)
        # 打印识别结果
        print('识别结果为：' , text)

        #进行翻译
        res = translation(text)[0]['translation_text']
        print('翻译的结果为', res)
        res = res[0]

        #在配置中的识别的范围，在这个范围内识别变量是否有res的文字
        scansave = ImageGrab.grab(scanrange)#保存识别范围的截图
        scansave.save("./saved/scansave.png")
        # 在指定范围内进行文字识别
        text = pytesseract.image_to_string(scansave, lang='chi_sim')
        # 获取每个单词的坐标
        boxes = pytesseract.image_to_boxes(scansave, lang='chi_sim')
        # 打印每个单词及其坐标
        for box in boxes.splitlines():
            box = box.split(' ')
            word = box[0]
            coordinates = (int(box[1]), int(box[2]), int(box[3]), int(box[4]))
            # 判断识别出的字是否与目标字相同
            if word == res:
                print(f"字符: {word}, 坐标: {coordinates}, 是否匹配: 是")
                # 点击识别正确文字的坐标
                x, y = scanrange[0] + coordinates[0], scanrange[3] - coordinates[1]
                pyautogui.click( x , y )
                # 停顿一段时间，以便观察点击效果
                #pyautogui.sleep(1)
                break
            else:
                print(f"字符: {word}, 是否匹配: 否")

        
        
        time.sleep(0.5)
        pyautogui.click(randompos[0], randompos[1])
        #此时自动点击‘下一步指定的位置’
        time.sleep(0.5)
        target_x, target_y = nextpos
        pyautogui.click(target_x, target_y)
        #print('点击了下一步按钮',nextpos)#逗号后面跟配置文件里的指定位置
        print('按CTRL+C终止程序运行!')
        time.sleep(1.5)
        #重复识别-点击的操作
    
    out=input('扣1退出,回车重新执行任务')
    if out == 1:
        break