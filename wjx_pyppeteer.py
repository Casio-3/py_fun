# @Reference: http://www.babyitellyou.com/details?id=606bfba80a6c642cafe25b02
# @Modifier: Casio3

import asyncio
import time
from random import choice

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from pyppeteer import launch
from pyppeteer_stealth import stealth

# TODO(1-halfway): Repeat simple get request until the questionnaire is open, then go to main run function.
# TODO(2): Profile Class to collect a student information, aiming at multi-autofill
# TODO(3): Click radio button, due to complex options, now i use random choice

url = "https://www.wjx.cn/jq/99620028.aspx" # Radio button passed
# url = "https://www.wjx.cn/jq/93605088.aspx"
# url = "https://www.wjx.cn/jq/96430564.aspx" # Successful example, only text forms
# url = "https://www.wjx.top/vj/twI3Q7E.aspx" # Aborted, contains multi-select button

name = "田所浩二"
student_id = "2020114514180"
college = "今晚吃鸡"
phone_number = "19198105200"
# class_id = "苹果班"
# ...

async def run():
    driver = await launch({
        'executablePath': r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        # Pyppeteer 默认使用的是无头浏览器
        'headless': False,
        # 设置Windows-size和Viewport大小来实现网页完整显示
        'args': ['--no-sandbox', '--window-size=1024,768', '--disable-infobars'],
        'dumpio': True
    })

    # 用 newPage 方法相当于浏览器中新建了一个选项卡,同时新建了一个Page对象
    page = await driver.newPage()
    #简称换头
    await page.setUserAgent(
        UserAgent().random
    )

    await page.setViewport({
        'width': 1024,
        'height': 768
    })
    # 反爬虫跳入网页
    await stealth(page)
    await page.goto(url)

    page_text = await page.content()  # 获取网页源码

    soup = BeautifulSoup(page_text, 'html.parser')
    # with open('idx.html', 'w+', encoding='utf-8', errors='ignore') as f:
    #     print(soup,file=f)

    title_ques = soup.find_all(class_='div_title_question')

    for item in title_ques:
        if '姓名' in item:
            da_name = 'q' + item['id'][-1]
        if '学号' in item:
            da_student_id = 'q' + item['id'][-1]
        if '学院' in item:
            da_college = 'q' + item['id'][-1]
        if '电话' in item or '手机' in item:
            da_phone_number = 'q' + item['id'][-1]

    text = '[name="{}"]'

    ran_radio = soup.find(class_='ulradiocheck')

    alt = []

    if ran_radio is not None:
        for item in ran_radio:
            i = item.find('label')
            if i:
                alt.append(i.get('for'))
        radio = 'a[rel="{}"]'

    try:
        await page.type(text.format(da_name), name)
    except Exception as e:
        print("'姓名' Missed...")
    try:
        await page.type(text.format(da_student_id), student_id)
    except Exception as e:
        print("'学号' Missed...")
    try:
        await page.type(text.format(da_college), college)
    except Exception as e:
        print("'学院' Missed...")
    try:
        await page.type(text.format(da_phone_number), phone_number)
    except Exception as e:
        print("'电话' Missed...")

# some unknown things...click twice is better.
    try:
        await page.click(radio.format(choice(alt)))
        await page.click(radio.format(choice(alt)))
    except Exception as e:
        print("jqRadio Missed.")

    try:
        await page.click('#submit_button')
        pass
    except Exception as e:
        await page.click('#submit_button')
        print('Catch Exception when submitting:',e)

    time.sleep(10)

asyncio.get_event_loop().run_until_complete(run())

"""
For Racing.
flag = False

while True:
    if flag:
        asyncio.get_event_loop().run_until_complete(run())
        break
    res = requests.get(url)
    if False:
        flag = True
"""
