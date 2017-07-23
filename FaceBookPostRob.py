#coding:UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

ChromeDriveDir ="/usr/lib/chromium-browser/chromedriver"

def NewPostRob(FaceBookID = "id@gmail.com",FaceBookPass = "xxxxxxxxxx",Content=["initial"],WaitLoadTime = 5):
	#    Open Web browser
    driver = webdriver.Chrome(ChromeDriveDir)
    #    go to mobile facebook
    driver.get("https:/m.facebook.com")

    #    enter email & password
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys(FaceBookID)
    elem = driver.find_element_by_name("pass")
    elem.clear()
    elem.send_keys(FaceBookPass)
    elem.send_keys(Keys.RETURN)
    time.sleep(WaitLoadTime)

    #    go to facebook's home
    driver.get("https://m.facebook.com/")


    #    create new post
    for con in Content:
        time.sleep(WaitLoadTime)
        elem = driver.find_element_by_name("xc_message")
        elem.send_keys(str(con))
        elem = driver.find_elements_by_css_selector("button._54k8")
        for i in elem:
            try:
                
                ButtonTitle = i.get_attribute("value")
                if ButtonTitle.encode('utf8') == "發佈":
                    i.click()
            except:
                pass
    
    driver.close()

NewPostRob("FacebookID@xxxxmail.com","password",["hello","world"])
