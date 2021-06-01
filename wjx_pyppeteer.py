import asyncio
from pyppeteer import launch
from pyppeteer_stealth import stealth
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import re
import time

url = "https://www.wjx.top/vj/twI3Q7E.aspx"

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

    fit = '[name="{}"]'

    try:
        await page.type(fit.format(da_name), name)
    except:
        print("'姓名' Missed...")

    try:
        await page.type(fit.format(da_student_id), student_id)
    except:
        print("'学号' Missed...")
    try:
        await page.type(fit.format(da_college), college)
    except:
        print("'学院' Missed...")
    try:
        await page.type(fit.format(da_phone_number), phone_number)
    except:
        print("'电话' Missed...")

    try:
        await page.click('#submit_button')
    except:
        print("提交出错.")

    time.sleep(20)


asyncio.get_event_loop().run_until_complete(run())