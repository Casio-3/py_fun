from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

def click(i,tag):
    tr = i.find_elements_by_tag_name(tag)
    for r in tr:
        a = r.find_elements_by_tag_name('a')
        randnum = random.randint(0, len(a))
        for k, n in enumerate(a):
            try:
                n.click()
                if k == randnum:
                    break
            except:
                pass
 
def input_info(i,class_name,info):
    text = i.find_elements_by_class_name(class_name)
    for i in text:
        try:
            i.click()
            i.send_keys(info)
        except:
            pass
 
def submit_content(i):
    randcontent = ['无可奉告','不清楚','不知道','还行','不错','ok','可以']
    info = random.choice(randcontent)
    input_info(i,'inputtext',info)
    input_info(i,'underline',info)
    input_info(i,'lisort',info)
 
def main():
    div_question = chrome.find_elements_by_class_name('div_question')
    for i in div_question:
        click(i,'ul')
        click(i,'tr')
        submit_content(i)
    submit = chrome.find_element_by_id('submit_button').click()
 
if __name__ == '__main__':
    url = input('请输入问卷星的问卷调查链接：')
    chrome = webdriver.Chrome()
    chrome.get(url)
    main()
    time.sleep(2)
    for i in range(1):
        chrome.get(url)
        main()
        chrome.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    print('问卷填写完成！')
    chrome.quit()
