#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

ChromeDriveDir ="/usr/lib/chromium-browser/chromedriver"
WaitLoadTime = 2


def Login(FaceBookID = "id@gmail.com",FaceBookPass = "xxxxxxxxxx",WaitLoadTime = 5):
    #    go to mobile facebook
    driver.get("https:/m.facebook.com")
    time.sleep(WaitLoadTime)
    #    enter email & password
    elem = driver.find_element_by_name("email")
    elem.clear()
    elem.send_keys(FaceBookID)
    elem = driver.find_element_by_name("pass")
    elem.clear()
    elem.send_keys(FaceBookPass)
    elem.send_keys(Keys.RETURN)
    time.sleep(WaitLoadTime)

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
                    i.submit()
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
Login('40241124+fuck@gm.nfu.edu.tw','gavin840511')
'''
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
'''
print 'going on'

driver.get("https://m.facebook.com/profile.php?")
time.sleep(WaitLoadTime)
driver.execute_script("window.scrollTo(100, document.body.scrollHeight);")

#NewPostRob(["hello","world"])
Today_Post_url = SelectPost("element.style")
print Today_Post_url




driver.get(Today_Post_url)
time.sleep(WaitLoadTime)
reply_container = driver.find_elements_by_class_name('_2b04')
for c in reply_container:
    reply_text = c.find_elements_by_class_name('_2b06')
    reply_text = c.find_element_by_tag_name('div')
    reply_button = c.find_element_by_partial_link_text('回覆')
    try:
        print reply_text.text.split('\n')
        reply_button.click()
        time.sleep(WaitLoadTime)
        reply_textBox = c.find_element_by_class_name('mentions-input')
        reply_textBox.send_keys('reply')
        time.sleep(WaitLoadTime)
        reply_submit = c.find_elements_by_css_selector("button._54k8")
        for i in reply_submit:
            try:                
                ButtonTitletype = i.get_attribute("type")
                
                if ButtonTitletype == 'submit':
                    i.click()
                    print i.get_attribute("value")
            except:
                print 'error'
    except Exception as e:
        print e




print 'end'
time.sleep(60)
driver.close()
