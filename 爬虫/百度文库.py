#codeing : utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/") #打开页面
assert "百度一下，你就知道" in driver.title
elem = driver.find_element_by_id("kw")
elem.send_keys("python")  #模拟按键输入
elem.send_keys(Keys.RETURN) #模拟submmit
print(driver.page_source)  #获取页面源代码