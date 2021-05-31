from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/course/第二阶段/练习的html/练习的html/跳转页面/pop.html")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='goo']").click()
time.sleep(5)
driver.quit()
