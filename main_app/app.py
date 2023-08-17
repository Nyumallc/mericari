# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36
# import requests
# from bs4 import BeautifulSoup

# URL = 'https://jp.mercari.com/item/m33273674060'
# useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
# headers = {"User-Agent": useragent}

# resp = requests.get(URL, timeout=1, headers=headers)
# r_text = resp.text

# soup = BeautifulSoup(r_text, 'html.parser')


# print(soup)

import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome import service as fs
from selenium.webdriver import ChromeOptions
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import time

s_num = st.text_input('URL')
submit = st.button("Search")
if submit:
    options = ChromeOptions()
    # option設定を追加（設定する理由はメモリの削減）
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    CHROMEDRIVER = ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    service = fs.Service(CHROMEDRIVER)
    driver = webdriver.Chrome(
                              options=options,
                              service=service
                             )

    # URLで指定したwebページを開く
    driver.get(s_num)
    time.sleep(1)
    counthtml = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(counthtml, "html.parser")
    print(soup)