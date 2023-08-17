import streamlit as st
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# ユーザーエージェントを指定
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

s_num = st.text_input('URL')
submit = st.button("Search")
if submit:
    options = webdriver.ChromeOptions()
    # option設定を追加（設定する理由はメモリの削減）
    options.add_argument("--headless")
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    # ユーザーエージェントを設定
    options.add_argument(f"user-agent={user_agent}")

    CHROMEDRIVER = ChromeDriverManager().install()  # ChromeTypeを指定しない
    service = ChromeService(executable_path=CHROMEDRIVER)
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
