from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get(r"E:/course/第二阶段/练习的html/练习的html/弹框的验证/dialogs.html")
driver.find_element_by_id("alert").click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(1)
driver.find_element_by_id("confirm").click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(1)
driver.quit()

