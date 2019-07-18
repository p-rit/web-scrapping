from selenium.webdriver.common.by import By
import argparse, os, time
import requests
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from demo import *

def Main():
	parser = argparse.ArgumentParser('lxml')
	parser.add_argument("email",help="linkedin email")
	parser.add_argument("password",help="linkedin password")
	args = parser.parse_args()
	print(args)
	
	chromedriver = r'C:\Users\FFC!\Downloads\chromedriver.exe'
	os.environ["webdriver.chrome.driver"] = chromedriver
	browser = webdriver.Chrome(chromedriver)
	wait = WebDriverWait(browser, 10)
	
	browser.get("https://www.linkedin.com/uas/login")
	wait.until(EC.presence_of_element_located((By.ID, 'session_key-login')))
	
	emailElement = browser.find_element_by_id("session_key-login")
	emailElement.send_keys(args.email)
	passElement  = browser.find_element_by_id("session_password-login")
	passElement.send_keys(args.password)
	passElement.submit()
	os.system("cls")
	print("logged in")
	#time.sleep(2)
				
	wait.until(EC.presence_of_element_located((By.ID, 'mynetwork-tab-icon')))# 'ember-view')))
					
	browser.find_element_by_xpath('//*[@id="mynetwork-nav-item"]').click()
	
	#wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pt4')))
	#browser.find("li",{"class":'mynetwork-nav-item'}).click()
	browser.find_element_by_link_text('See all').click()

	
	l = links(browser)
	print(l)
	browser.close()

if __name__=="__main__":
	Main()

