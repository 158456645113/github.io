import os
import threading
import time
import subprocess
from multiprocessing import Process
from urllib.parse import urlparse
from you_get import common as you_get
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import keyboard 
 

url_list = [] 
 

def href():
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


ie = input("请输入url:")
driver = webdriver.Edge(EdgeChromiumDriverManager().install())

def url():
    global ie
    global ll
    driver.get(ie)
    WebDriverWait(driver, 999999)
    JavaScript()
    if ll != None:
        if url_list:
            uu = url_list.pop(0)
            try:
                command = ['you-get', '-u', uu]
                p = subprocess.check_output(command, universal_newlines=True)
                start_index = p.find("['") + 2  
                end_index = p.find("']")  #
                lin = p[start_index:end_index]  
                t1 = threading.Thread(target=m3u8, args=("D:\桌面\m3u8下载工具\Downloads",lin))
                t1.start()
                t2 = threading.Thread(target=video)
                t2.start()
            except Exception as e:
                t2 = threading.Thread(target=video)
                t2.start()
    else:
        print("网页没有视频")
        t1 = threading.Thread(target=video)
        t1.start()
    while True:
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(1.5)
        if driver.execute_script('return window.pageYOffset + window.innerHeight >= document.body.scrollHeight;'):
            t1 = threading.Thread(target=href)
            t1.start()
            break

def m3u8(directory, url):
    command = f'N_m3u8DL-CLI_v3.0.2.exe --workDir "{directory}" --enableDelAfterDone --maxThreads 64 --retryCount 1 {url}'
    os.system(command)

def JavaScript():
    sj = '''
    var content = document.documentElement.innerHTML;
    var regex = /https?:\/\/[^\s'"]+\.m3u8/g;
    var m3u8Links = content.match(regex);
    return m3u8Links;
    '''
    global ll
    ll = driver.execute_script(sj)

def video():
    global ie
    if url_list:
        ie = url_list.pop(0)
        del url_list[0]
    else:
        pass
    t1 = threading.Thread(target=url)
    t1.start()

t1 = threading.Thread(target=url)
t1.start()
t1.join()
