import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

s_num = st.text_input('URL')
submit = st.button("Search")
if submit:
    options = webdriver.ChromeOptions()
    # option設定を追加（設定する理由はメモリの削減）
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    CHROMEDRIVER = ChromeDriverManager().install()  # ChromeTypeを指定しない
    service = ChromeService(CHROMEDRIVER)
    driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER,
        options=options,
        service=service
    )

    # URLで指定したwebページを開く
    driver.get(s_num)
    time.sleep(1)
    counthtml = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(counthtml, "html.parser")
    print(soup)
