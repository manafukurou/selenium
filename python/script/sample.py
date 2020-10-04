
from selenium import webdriver
from selenium.webdriver.common.by import By

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument('--headless')

# Selenium Server に接続する
driver = webdriver.Remote(
    command_executor='http://local.selenium:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)
width = 1200
height = 900
driver.set_window_size(width, height)

# Selenium 経由でブラウザを操作する
driver.get('https://tech.manafukurou.com')
print(driver.current_url)


# 2.　例として記事一覧の 4 ページ目に移動する
driver.find_element(By.XPATH, '//*[@id="list"]/a[4]').click()
print(driver.current_url)


#3. 画面の幅をコンテンツの幅と合わせてスクリーンショットをとる
w = driver.execute_script('return document.body.scrollWidth')
h = driver.execute_script('return document.body.scrollHeight')
driver.set_window_size(w, h)
driver.save_screenshot('screenshot.png')


# ブラウザを終了する
driver.quit()


