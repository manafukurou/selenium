from selenium import webdriver
from selenium.webdriver.common.by import By
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

endpoint = config.get('general', 'endpoint')
email = config.get('general', 'email')
password = config.get('general', 'password')
implicitly_wait = config.get('general', 'implicitly_wait')

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
#options.add_argument('--headless')

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://local.selenium:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)
#要素がロードされるまでの待ち時間を設定
driver.implicitly_wait(implicitly_wait)


width = 1200
height = 900
driver.set_window_size(width, height)

# Selenium 経由でブラウザを操作する
driver.get(endpoint)
print(driver.current_url)

#サインアップボタンクリック
element = driver.find_element_by_link_text('ログイン')
element.click()

semail = driver.find_element_by_id("email")
semail.send_keys(email)
spassword = driver.find_element_by_id("password")
spassword.send_keys(password)

driver.find_element_by_id("login-button").click()
print(driver.current_url)

# #3. 画面の幅をコンテンツの幅と合わせてスクリーンショットをとる
driver.save_screenshot('screenshot.png')


# ブラウザを終了する
driver.quit()

