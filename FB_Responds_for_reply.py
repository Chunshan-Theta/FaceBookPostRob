#coding:utf-8
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
    
    
def SelectPost(Tcontent):
    Turl='not find'
    #elem = driver.find_elements_by_partial_link_text('world')
    story_body_container = driver.find_elements_by_class_name('story_body_container')
    for c in story_body_container:       
        textbox = c.find_element_by_class_name('_5rgt')
        content_in_textbox = textbox.find_element_by_tag_name('span')   
        try:
            if content_in_textbox.text == Tcontent:
               reply_url = c.find_element_by_css_selector("a._5msj")
               Turl =  reply_url.get_attribute("href")
        except Exception as e:
            print u' '.join(('error: ', unicode(e))).encode('utf-8')
    return Turl

# Open Web browser
driver = webdriver.Chrome(ChromeDriveDir)
#    go to mobile facebook
driver.get("https:/m.facebook.com")

print 'login to facebook in 30 sec.'
time.sleep(10)
print 'login to facebook in 20 sec.'
time.sleep(15)
print '5'
time.sleep(1)
print '4'
time.sleep(1)
print '3'
time.sleep(1)
print '2'
time.sleep(1)
print '1'
time.sleep(1)
print 'going on'

driver.get("https://m.facebook.com/profile.php?")

driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")

#NewPostRob(["hello","world"])
Today_Post_url = SelectPost("element.style")
print Today_Post_url

driver.get(Today_Post_url)
time.sleep(60)
driver.close()
