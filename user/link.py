"""
MIT License

Copyright (c) 2022 Makarand Pundlik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller

# f : Cab or Bus (1= Cab, 2=Bus)
def get_link(source,destination,date_tr,month_tr,time_tr,f):
    """Generates a route link from Google Maps based on the given source, destination, travel date, time, and mode of transport."""
    chromedriver_autoinstaller.install()
    chrome_options = webdriver.ChromeOptions()
    browser = webdriver.Chrome(options=chrome_options)

    dict_month={'Jan':1,'Feb':2,'Mar':3,'Apr':4,'May':5,'Jun':6,'Jul':7,'Aug':8,'Sep':9,'Oct':10,'Nov':11,'Dec':12}
    month_tr=dict_month[month_tr]
    date_tr=int(date_tr)
    browser.get('https://www.google.com/maps')
    box=browser.find_element("xpath",'//*[@id="searchboxinput"]')
    box.click()

    box.send_keys(destination) 
    box.send_keys(Keys.ENTER)
    time.sleep(4)

    dir=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[4]/div[1]/button')
    dir.click()
    time.sleep(4)
    box=browser.find_element("xpath",'//*[@id="sb_ifc51"]/input')
    box.click()
    box.send_keys(source) 
    box.send_keys(Keys.ENTER)
    time.sleep(2)

    browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/span/div/div/div/div[2]').click()
    browser.find_element("xpath",'//*[@id=":9"]/div').click()
    date=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span[1]').text
    date_today=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span[1]').text
    date_today=date_today[5:]
    month=dict_month[date_today[:3]]
    date=int(date_today[3:])
    if(date_tr!=date):
        if(month == month_tr):
            diff=date_tr-date
        else:
            if(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
                diff=date_tr+31-date
            elif(month==2):
                diff=date_tr+28-date
            else:
                diff=date_tr+30-date

        for i in range(diff):
            browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[2]/span[2]/button[2]').click()
            time.sleep(2)
    time_n=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/span[1]/input')
    time_n.send_keys(Keys.CONTROL + "a")
    time_n.send_keys(Keys.DELETE)
    time_n.send_keys(time_tr)
    time.sleep(2)

    if(f==2):
        browser.find_element("xpath",'//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[3]/button').click()
        time.sleep(2)

    browser.find_element("xpath",'//*[@id="section-directions-trip-title-0"]').click()
    time.sleep(2)

    if(f==2):
        route=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[2]').text
        info=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div').text
        route=route+" , "+info
    else:
        route="Cab"

    share=browser.find_element("xpath",'//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/button')
    share.click()
    time.sleep(2)
    emb=browser.find_element("xpath",'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div[1]/div[2]/button[2]')
    emb.click()
    time.sleep(4)
    link=browser.find_element("xpath",'//*[@id="modal-dialog"]/div/div[2]/div/div[3]/div/div/div/div[3]/div[1]/input').get_attribute("value")
    return(route,link)
