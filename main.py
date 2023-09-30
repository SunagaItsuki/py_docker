from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time


driver = webdriver.Remote(
    command_executor = os.environ["SELENIUM_URL"],
    options = webdriver.ChromeOptions()
)

driver.implicitly_wait(10)

# ログイン処理
url = "https://scraping-for-beginner.herokuapp.com/login_page"
username = "imanishi"
password = "kohei"

driver.get(url)
# ユーザー名とパスワードを入力
driver.find_element(By.ID, "username").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)

# ログインボタンをクリック
login_btn = driver.find_element(By.ID, "login-btn")
login_btn.click()

# テーブルを取得
elems_th = driver.find_elements(By.TAG_NAME, "th")
elems_td = driver.find_elements(By.TAG_NAME, "td")

# 要素の個数分表示(パターン1)
for elem_th in elems_th:
    print (f"{elem_th.text}") 

for elem_td in elems_td:
    print (f"{elem_td.text}") 


# 要素の個数分表示(パターン2)
for i in range(len(elems_th)):
    print (f"{elems_th[i].text}:{elems_td[i].text}")
    i += 1

# 別画面に移動
url = "https://scraping-for-beginner.herokuapp.com/ranking/"
driver.get(url)

# 画面の一番下まで移動(document.body.scrollHeightで取得できるのは、厳密に言うと残りのスクロールできる高さ)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(2)
driver.quit()

