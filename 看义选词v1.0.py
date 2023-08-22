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

def remove_first_character_and_dots(string):
    # 去除第一个字母
    string = string[1:]
    # 去除所有小数点
    string = string.replace(".", "")
    return string

def is_character_in_string(character, string):
    if character in string:
        return True
    else:
        return False


with open('./config.json') as f:
    config = json.load(f)
# 获取配置项的值
screensize = config['screensize']
randompos = config['randompos']
nextpos = config['nextpos']
shotrange = config['shotrange']
scanrange = config['scanrange']
y_dist = config['y_dist']
botton_dist = config['botton_dist']
# 打印配置项的值
print(f'屏幕分辨率为{screensize}')
print(f'A选项坐标{randompos}')
print(f'下一个按钮的位置{nextpos}')
print(f'题目单词的范围{shotrange}')
print(f'四个选项的范围{scanrange}')
print(f'选项按钮y值的大小{botton_dist}')
print(f'两个选项之间的间隔{y_dist}')

warnings.filterwarnings ('ignore')
modelName = "DDDSSS/translation_en-zh"
print('正在加载翻译模型......')
model = AutoModelWithLMHead.from_pretrained(modelName)
tokenizer = AutoTokenizer.from_pretrained(modelName)
translation = pipeline('translation_zh_to_en',model=model,tokenizer=tokenizer)
print('加载完成')

# 下面为主程序

while True:
    r = int(input('请输入还要多少个单词未完成'))
    #下面是主程序
    print('运行此程序时一定要固定西柚窗口的位置!')
    print('按CTRL+C中断程序!')
    print('三秒后开始运行')
    time.sleep(3)

    for i in range(1,r+1,1):
        screensave = ImageGrab.grab(shotrange)
        screensave.save("./saved/screenshot.png")
        print('已截屏,正在处理...')
        #识别出截屏的内容（已知识别的内容只有中文或英文）
        # 设置语言参数为中文简体
        # 进行文字识别
        text = pytesseract.image_to_string(screensave, lang='chi_sim')
        # 打印识别结果
        print('识别结果为：' , text)

        for t in range (0,4,1):
            print(f'正在识别第{t+1}个选项')
            per_scanrange = [scanrange[0],scanrange[1] + t*(botton_dist+y_dist),scanrange[2],scanrange[1] + t*(botton_dist+y_dist) + botton_dist]
            scansave = ImageGrab.grab(per_scanrange)
            # print(f'扫描的位置是{per_scanrange}')
            scansave.save("./saved/scansave.png")
            scan = pytesseract.image_to_string(scansave, lang='eng')
            scan = remove_first_character_and_dots(scan)
            print(f'识别的结果是{scan}')
            #进行翻译
            res = translation(scan)[0]['translation_text']
            print('翻译的结果为', res)
            res = res[0]
            if is_character_in_string(res, text):
                pyautogui.click( scanrange[0]+20 , scanrange[1] + t*(botton_dist+y_dist)+10 )
                break

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
        clear_terminal()
    
    out=input('扣1退出,回车重新执行任务')
    if out == 1:
        break