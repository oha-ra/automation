# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# ブラウザを開く
driver = webdriver.Chrome('/Users/michihiro_ohara/Desktop/automation/chromedriver', options=options)

# Googleの検索TOP画面を開く
driver.get("https://www.google.co.jp/")

# 検索語として「selenium」と入力し、Enterキーを押す。
# search = driver.find_element_by_name('q')  #old
search = driver.find_element("name", "q") #Selenium v4.3.0
search.send_keys("selenium")
search.send_keys(Keys.ENTER)

# 5秒間待機してみる。
sleep(5)
# ブラウザを終了する。
driver.close()