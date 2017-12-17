#coding:UTF-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

ChromeDriveDir ="/usr/lib/chromium-browser/chromedriver"





def NewPostRob(Content=["initial"],WaitLoadTime = 5):

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
    
    
def PrintPost():

    #elem = driver.find_elements_by_partial_link_text('則留言')
    elem = driver.find_elements_by_class_name('_34qc')
    print len(elem)    
    for j in elem:
        elem2 = j.find_elements_by_tag_name('a')        
        for i in elem2:
            try:
                print i.get_attribute("href")
            except:
                print 'none url'




# Open Web browser
driver = webdriver.Chrome(ChromeDriveDir)
#    go to mobile facebook
driver.get("https:/m.facebook.com")

print 'login to facebook in 30 sec.'
time.sleep(10)
print 'login to facebook in 20 sec.'
time.sleep(20)
print 'going on'


#NewPostRob(["hello","world"])
PrintPost()

driver.close()
