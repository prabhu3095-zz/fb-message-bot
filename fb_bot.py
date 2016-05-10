'''
    Author : Prabhu Dayal Sahoo
    Institute : National Institute of Technology Karnataka
    Project Name : Facebook Meassage Bot
    Project Idea : A python script to automate user login into facebook.com and sending message to a friend/group.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import time

text1 = 'ENTER YOUR EMAIL ID'
text2 = 'ENTER YOUR PASSWORD'

#This will open the facebook.com 
driver = webdriver.Firefox()
driver.get('https://www.facebook.com/')
print("Opened facebook...")
time.sleep(2)

#Find the email input in the html code, send_keys enters your email
email = driver.find_element_by_xpath("//input[@id='email' or @name='email']")
email.send_keys(text1)
print("Email Id entered...")

#Find password input in the html code, enter password
password = driver.find_element_by_xpath("//input[@id='pass']")
password.send_keys(text2)
print("Password entered...")

#Press the login button 
button = driver.find_element_by_xpath("//input[@id='u_0_w']")
button.click()
time.sleep(2)
print 'Logged in...'

#Open the message dialog box by clicking on message symbol
message = driver.find_element_by_xpath("//div[@class='uiToggle _4962 _1z4y']")
message.click()
time.sleep(2)


#Click on the name of the person/group who want to message. This will open the message box.
tomatoes = driver.find_element_by_xpath("//*[text()='Tomatoes']") #'Tomatoes is the name of recipient of the message'
tomatoes.click()
print 'Open message box...'
time.sleep(2)

#This will enter the message and send.
msg = driver.find_element_by_xpath("//div[@class='_5rpu']")
msg.send_keys('I am Mr. BOT. Say hi...') #message to be sent
msg.send_keys(Keys.ENTER)
print 'Message Sent...'
time.sleep(2)


