
from selenium.webdriver.common.by import By
import argparse, os, time
import requests
import urllib.parse, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

'''def getPeopleLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:
			if 'profile/view?id=' in url:
				links.append(url)
	return links

def getJobLinks(page):
	links = []
	for link in page.find_all('a'):
		url = link.get('href')
		if url:		
			if '/jobs' in url:
				links.append(url)
	return links

def getID(url):
	pUrl = urllib.parse.urlparse(url)
	return urllib.parse.parse_qs(pUrl.query)['id'][0]


def ViewBot(browser):
	visited = {}
	pList = []
	count = 0
	while True:
		#sleep to make sure everything loads, add random to make us look human.
		time.sleep(random.uniform(3.5,6.9))
		page = BeautifulSoup(browser.page_source)
		people = getPeopleLinks(page)
		print(people)
		if people:
			for person in people:
				ID = getID(person)
				if ID not in visited:
					pList.append(person)
					visited[ID] = 1
		if pList: #if there is people to look at look at them
			person = pList.pop()
			browser.get(person)
			count += 1
		else: #otherwise find people via the job pages
			jobs = getJobLinks(page)
			if jobs:
				job = random.choice(jobs)
				root = 'http://www.linkedin.com'
				roots = 'https://www.linkedin.com'
				if root not in job or roots not in job:
					job = 'https://www.linkedin.com'+job
				browser.get(job)
			else:
				print ("I'm Lost Exiting")
				break

		#Output (Make option for this)			
		print( "[+] "+browser.title+" Visited! \n("\
			+str(count)+"/"+str(len(pList))+") Visited/Queue)")'''
def ViewBot(browser):
	while True:
		connections=[]
		#sleep to make sure everything loads, add random to make us look human.
		time.sleep(random.uniform(3.5,6.9))
		#browser.find_element_by_xpath('//*[@id="ember3137"]/button').click()
		
		page = BeautifulSoup(browser.page_source)
		

		all=page.find_all("div",{"class":"mn-connection-card__details"})
		for i in all:
			j = i.find("a")
			j = j['href']
			
			connections.append(j)

		print(connections)
		return
        

					
def Main():
	parser = argparse.ArgumentParser('lxml')
	parser.add_argument("email",help="linkedin email")
	parser.add_argument("password",help="linkedin password")
	args = parser.parse_args()
	print(args)
	chromedriver = r'C:\Users\FFC!\Downloads\chromedriver_win32\chromedriver.exe'
	os.environ["webdriver.chrome.driver"] = chromedriver
	browser = webdriver.Chrome(chromedriver)
	
	browser.get("https://www.linkedin.com/uas/login")
	browser.implicitly_wait(10)
	emailElement = browser.find_element_by_id("session_key-login")
	emailElement.send_keys(args.email)
	passElement  = browser.find_element_by_id("session_password-login")
	passElement.send_keys(args.password)
	passElement.submit()
	os.system("cls")
	print("logged in")
		
	browser.find_element_by_xpath('//*[@id="mynetwork-nav-item"]').click()
	
	
	#browser.find("li",{"class":'mynetwork-nav-item'}).click()
	browser.find_element_by_link_text('See all').click()

	
	ViewBot(browser)
	browser.close()

if __name__=="__main__":
	Main()


