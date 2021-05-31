
from selenium import webdriver
import time
# 创建谷歌浏览器对象
chromeDriver = webdriver.Chrome()

# 打开百度网址
chromeDriver.get("http://www.baidu.com")

# 窗口最大化
chromeDriver.maximize_window()

#寻找搜索输入框
chromeDriver.find_element_by_id("kw").send_keys("java")

# 点击百度一下按钮
chromeDriver.find_element_by_id("su").click()

time.sleep(20)
# 退出浏览器
chromeDriver.quit()
