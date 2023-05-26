import os
import threading
import time
import mp4
from multiprocessing import Process
from urllib.parse import urlparse
from you_get import common as you_get
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import keyboard

url_list = []


def JavaScript():
    js = """
    let links = document.getElementsByTagName('a');
    let hrefs = [];
    for (let i = 0; i < links.length; i++) {
        let href = links[i].href;
        if (href.startsWith('http') && !hrefs.includes(href)) {
            hrefs.push(href);
        }
    }
    return hrefs;
    """
    p = driver.execute_script(js)
    for i in p:
        url_list.append(i)
    t1 = threading.Thread(target=video)
    t1.start()


def video():
    global ie
    if url_list:
        ie = url_list.pop(0)
        del url_list[0]
    else:
        pass
    t1 = threading.Thread(target=url)
    t1.start()


ie = input("请输入url:")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())


def url():
    global ie
    driver.get(ie)
    WebDriverWait(driver, 999999)
    html_content = driver.page_source
    if 'video' in html_content.lower():
        print('网页包含视频')
        global uu
        if url_list:
            uu = url_list.pop(0)
            print("网页包含视频")
            # p = Process(target=mp4)
            t1 = threading.Thread(target=mp4, args=("D:\桌面\m3u8下载工具\视频", uu))
            t1.start()
        else:
            pass
    else:
        print("网页没有视频")
        t1 = threading.Thread(target=video)
        t1.start()
    while True:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(1.5)
        if driver.execute_script('return window.pageYOffset + window.innerHeight >= document.body.scrollHeight;'):
            t1 = threading.Thread(target=JavaScript)
            t1.start()
            break


def mp4(directory, url):
    command = f'you-get -o "{directory}" --no-caption {url}'
    os.system(command)
# 创建多个线程来执行多个下载任务




t1 = threading.Thread(target=url)
t1.start()


def on_key_event(event):
    if event.name == 'esc':
        os._exit(0)
        driver.quit()
keyboard.on_press(on_key_event)
keyboard.wait()