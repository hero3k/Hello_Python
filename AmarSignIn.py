#coding=utf-8
from selenium import webdriver
import requests
from PIL import Image
from PIL import ImageOps
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from urllib.request import urlopen
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x: 0 if x < 143 else 255)
    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)

driver = webdriver.PhantomJS(executable_path='D:/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
#driver = webdriver.Chrome(executable_path='E:/python/chromedriver_x64.exe')

urls = "http://www.amarsoft.com/sso/ssologin.jsp?continue=http://www.amarsoft.com/EIP/DeskTop/MyDesktop.jsp"
driver.get(urls)
driver.save_screenshot("dd.png")
imgelement = driver.find_element_by_xpath('//img[@src="Kaptcha.jpg"]')  #定位验证码
location = imgelement.location  #获取验证码x,y轴坐标
size=imgelement.size  #获取验证码的长宽
rangle=(int(location['x']),int(location['y']+100),int(location['x']+size['width']),int(location['y']+size['height']+90)) #写成我们需要截取的位置坐标
img = Image.open("dd.png")
frame4=img.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
frame4.save('f://frame4.jpg')
qq=Image.open('f://frame4.jpg')
qq.show()





yzm = input("输入验证码：")
driver.find_element_by_id("mail").clear()
driver.find_element_by_id("mail").send_keys("****")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("****")
driver.find_element_by_name("captcha").send_keys(yzm)
driver.find_element_by_class_name('button').click()
title = driver.title
print(title)
driver.find_element_by_xpath("//span[@class='co_day co_day_current']").click()
time.sleep(2)
driver.find_element_by_xpath("//label[@for='workspot_A_O']").click()
driver.find_element_by_xpath("//label[@for='workspot_P_O']").click()

#driver.find_element_by_xpath("//button[@type='button']").click()
driver.find_element_by_xpath("//fieldset[@id='fieldset_A']/div/div/div[2]/div[2]/span/button[@class='ui-autocomplete-dropdown ui-button ui-widget ui-state-default ui-corner-right ui-button-icon-only']").click()
time.sleep(2)
driver.find_element_by_xpath("//li[@class='ui-autocomplete-item ui-autocomplete-list-item ui-corner-all']").click()

driver.find_element_by_xpath("//fieldset[@id='fieldset_P']/div/div/div[2]/div[2]/span/button[@class='ui-autocomplete-dropdown ui-button ui-widget ui-state-default ui-corner-right ui-button-icon-only']").click()
time.sleep(2)
#driver.find_element_by_xpath("//li[@class='ui-autocomplete-item ui-autocomplete-list-item ui-corner-all']").click()
#driver.find_element_by_xpath("//body//div[@style='height:auto; visibility: visible; width: 519px; z-index: 1001; top: 195.2px; left: 805.233px; display: block;']").click()
#driver.find_element_by_xpath("//div[@style='visibility: visible; display: block; height: auto; width: 519px; z-index: 1048; top: 195.2px; left: 805.233px;']").click()
#/ul/li[@class='ui-autocomplete-item ui-autocomplete-list-item ui-corner-all']"

time.sleep(2)

#driver.find_element_by_xpath("//li[contains(text(), '其他')]").click()
#driver.find_element_by_xpath("//button[@class='ui-autocomplete-dropdown ui-button ui-widget ui-state-default ui-corner-right ui-button-icon-only']").click()
#time.sleep(5)
#注意这里是element‘S’
aa = driver.find_elements_by_xpath("//li[@class='ui-autocomplete-item ui-autocomplete-list-item ui-corner-all']")
for a in aa:
    if a.is_displayed() is True:
        a.click()
#复制XPATH内容到火狐元素搜索框可以直接搜索-判断是否定位准确
driver.find_element_by_xpath("//fieldset[@id='fieldset_A']/div/div/div[3]/div[4]/div/div[3]/span[@class='fa fa-fw fa-caret-down']").click()
time.sleep(2)
driver.find_element_by_xpath("//li[contains(text(), '深圳')]").click()


driver.find_element_by_xpath("//fieldset[@id='fieldset_P']/div/div/div[3]/div[4]/div/div[3]/span[@class='fa fa-fw fa-caret-down']").click()
time.sleep(2)
aa1=driver.find_elements_by_xpath("//li[contains(text(), '深圳')]")
for a1 in aa1:
    if a1.is_displayed() is True:
        a1.click()

driver.find_element_by_id('save').click()

print("签到成功！")

driver.get_screenshot_as_file("bb.png")
img = Image.open("bb.png")
img.show()

#<li class="ui-autocomplete-item ui-autocomplete-list-item ui-corner-all ui-state-highlight">其他任务（待建立任务或者待被加入到任务中）</li>
#time.sleep(10)
#url2 = "http://www.amarsoft.com/EIP/DeskTop/MyDesktop.jsp"
#driver.get(url2)
#html = driver.page_source
#print(html)

driver.quit()
