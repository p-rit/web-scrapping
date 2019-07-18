from selenium.webdriver.common.by import By
import urllib.parse, random
import  time
from bs4 import BeautifulSoup
import pandas
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math 
from selenium.webdriver.support import expected_conditions as EC


def ExtractLinks(browser):
	
		connections=[]
		#sleep to make sure everything loads, add random to make us look human.
		time.sleep(3)
		#element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ember4090")))
		url = browser.current_url
		print(url)
		browser.get(url)
		time.sleep(10)	
		page = BeautifulSoup(browser.page_source ,'lxml')
		all=page.find_all("div",{"class":"mn-connection-card__details"})
		print(len(all))
		for i in all:
				j = i.find("a")
				j = j['href']
				connections.append(j)

		return connections

d={}
def fetchData(browser, page):
	global d
	wait = WebDriverWait(browser, 50)

	wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
		)
	name = page.find('h1',{'class':'pv-top-card-section__name Sans-26px-black-85%'}).text
	name = name.replace('\n','').strip()
	
	d['name'] = name
	d["exp"] = {}
	exp = page.find("section",{'id':'experience-section'})
	if exp :	
		companies = exp.find_all('div',{'class':'pv-entity__summary-info pv-entity__summary-info--v2'})
		j=0
		for a in companies:
			j=j+1
			d['exp']['profile %s'%j]= a.find('h3',{'class':'Sans-17px-black-85%-semibold'}).text
			d['exp']['company %s'%j] = a.find('span',{'class':'pv-entity__secondary-title'}).text
			b = a.find('h4',{'class':'pv-entity__date-range inline-block Sans-15px-black-70%'})
			if b:
				c = b.find_all('span')
				d['exp']['time %s'%j] = c[1].text

	k = page.find_all('p',{'class':'pv-entity__secondary-title pv-entity__degree-name pv-entity__secondary-title Sans-15px-black-85%'})
	
	d["course"] = k[0].find('span',{'class':'pv-entity__comma-item'}).text
	l = page.find('p',{'class':'pv-entity__dates Sans-15px-black-70%'})
	x = l.find_all("time")
	d['years'] = x[0].text+"-"+x[1].text
	return 

'''course =[]
name=[]
year=[]
exp =[]

def fetchData(browser, page):
	global  course
	global name
	global  year
	global  exp
	wait = WebDriverWait(browser, 50)

	wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content'))
		)
	n = page.find('h1',{'class':'pv-top-card-section__name Sans-26px-black-85%'}).text
	n = n.replace('\n','').strip()
	
	name.append(n)
	d = {}
	e = page.find("section",{'id':'experience-section'})
	if exp :	
		companies = e.find_all('div',{'class':'pv-entity__summary-info pv-entity__summary-info--v2'})
		j=0
		for a in companies:
			j=j+1
			d['profile %s'%j]= a.find('h3',{'class':'Sans-17px-black-85%-semibold'}).text
			d['company %s'%j] = a.find('span',{'class':'pv-entity__secondary-title'}).text
			b = a.find('h4',{'class':'pv-entity__date-range inline-block Sans-15px-black-70%'})
			c = b.find_all('span')
			d['time %s'%j] = c[1].text
	print(d)
	exp.append(d)

	k = page.find_all('p',{'class':'pv-entity__secondary-title pv-entity__degree-name pv-entity__secondary-title Sans-15px-black-85%'})
	if k:
		c = k[0].find('span',{'class':'pv-entity__comma-item'}).text
		course.append(c)
	l = page.find('p',{'class':'pv-entity__dates Sans-15px-black-70%'})
	if l:
		x = l.find_all("time")
		y = x[0].text+"-"+x[1].text
		year.append(y)'''

def links(browser):
	
	#links = ExtractLinks(browser)
	#print(links)
		connections=[]
	#for link in links:
		browser.get('https://www.linkedin.com'+'/in/rajatj61/')
		page = BeautifulSoup(browser.page_source , 'lxml')
		
		a = page.find('a',{'class':'pv-top-card-v2-section__link pv-top-card-v2-section__link-education mb1'})
		if a:
			a= a.text
			
			if ('IIPS' in a or 'I.I.P.S.' in a or 'Iips' in a or 'International Institute Of Professional Studies' in a or 'International Institute of Professional Studies' in a or 'international institute of professional studies' in a or 'International institute of professional studies' in a ) :#and ('indore' in b or 'Indore' in b):
				wait = WebDriverWait(browser, 50)
				#time.sleep(2)
				wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'pv-deferred-area__content')))
				
				all=page.find_all("li",{"class":"pv-browsemap-section__member-container mt4"})
								
				for i in all:
					j = i.find("a")
					j = j['href']
					connections.append(j)
				print(connections)
								
				#fetchData(browser , page)
				browser.find_element_by_partial_link_text("See connections").click()
								#sleep to make sure everything loads, add random to make us look human.
				time.sleep(2)
				#wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'page-list')))# 'ember-view')))
				#num = getNoOfConnection(page)
				wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'results-list ember-view')))
				time.sleep(2)
				page = BeautifulSoup(browser.page_source,'lxml')

				#while(num):
							
				all = page.find_all("div",{'class':'search-result__image-wrapper'})
				
				for i in all:
						j = i.find("a") 
						j = j['href']
						connections.append(j)
				print(connections)
									
			
							
		#links = links.append(connections)
		#print(links)
		#links = set(links)
		#links = list(links)
				print(len(connections))
		
	#print(d)
		d = {'name':name, 'course':course, 'year':year, 'exp':exp}
		df  = pandas.DataFrame(d)
		df.to_csv("output.csv")
	#return df


def getNoOfConnection(page):
		num = page.find("h3",{'class':'search-results__total Sans-15px-black-55% pl5 pt4 clear-both'})#,{'class':'search-results__total Sans-15px-black-55% pl5 pt4 clear-both'}).text
		print(num)
		num = num.replace('Showing','')
		num = num.replace("results",'')
		#num = num.replace("(",'')
		num = math.ceil(int(num)/10)
		return num

