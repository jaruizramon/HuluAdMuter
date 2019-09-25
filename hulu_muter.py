
'''

ADVERTISEMENTS ARE TOO LOUD -> PROBLEM

'''

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
    
global driver, usern, passw

def launch_driver():
    
    global driver, usern, passw
    
    usern = 'email'
    passw = 'password'
    
    options = Options()
    
    options.add_argument("--disable-extensions")
    options.add_argument("--start-maximized")
    
    
    driver = webdriver.Chrome(options=options)
    
    driver.get('https://www.hulu.com/welcome')
    
    login_click = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/nav/header/div[1]/div[2]/div[2]/button[2]')
    login_click.click()
    
    user_in = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/input[1]')
    user_in.clear()
    user_in.send_keys(usern)
    sleep(1)
    
    pass_in = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/input[2]')
    pass_in.clear()
    pass_in.send_keys(passw)
    sleep(1)
    
    login_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/button')
    login_btn.click()
    
    shush_ads()
    


def shush_ads():
    
    global driver
    
    
    while(True):
        
        try:
            
            soup = BeautifulSoup(driver.page_source, 'lxml')
            video_window = driver.find_element_by_xpath('/html/body') 
            
            try:
                
                general = soup.find('div', class_='num-down-counter-in-rotor')
                seconds_to_mute = int(general.text)
                
                if(seconds_to_mute < 2):
                    shush_ads()
    
                video_window.send_keys(Keys.SPACE)
                mutebtn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[8]/div[2]/div[2]/div[3]/div[1]/div[4]/div[1]')
                mutebtn.click()
                video_window.send_keys(Keys.SPACE)
                
                sleep(seconds_to_mute + 3)
                
                video_window.send_keys(Keys.SPACE)
                mutebtn = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[8]/div[2]/div[2]/div[3]/div[1]/div[4]/div[1]')
                mutebtn.click()
                video_window.send_keys(Keys.SPACE)
                
                
                sleep(1)
                
            except:
                
                print('no annoying ads detected')
                sleep(1)
            
        except:
            
            print('no windows detected')
            sleep(1) 
       
'''

S T A R T

'''

'''

Jana's Tkinter here

'''


launch_driver()
