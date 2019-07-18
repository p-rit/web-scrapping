from selenium.webdriver.common.by import By
import urllib.parse, random
import  time
from bs4 import BeautifulSoup
import pandas
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
wait untill page loads
'''
def ExtractLinks(browser):
	
		connections=[]
		#sleep to make sure everything loads, add random to make us look human.
		#time.sleep(30)
		
		element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "ember4090")))
			
		page = BeautifulSoup(browser.page_source)
		all=page.find_all("div",{"class":"mn-connection-card__details"})
		print(len(all))
		for i in all:
				j = i.find("a")
				j = j['href']
				connections.append(j)

		return connections

d={}
def fetchData(page):
	global d
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
			c = b.find_all('span')
			d['exp']['time %s'%j] = c[1].text

	k = page.find_all('p',{'class':'pv-entity__secondary-title pv-entity__degree-name pv-entity__secondary-title Sans-15px-black-85%'})
	
	d["course"] = k[0].find('span',{'class':'pv-entity__comma-item'}).text
	l = page.find('p',{'class':'pv-entity__dates Sans-15px-black-70%'})
	x = l.find_all("time")
	d['years'] = x[0].text+"-"+x[1].text
	return 

def links(browser):
	
	links = ExtractLinks(browser)
	for link in links:
		browser.get('https://www.linkedin.com'+link)
		page = BeautifulSoup(browser.page_source)
		
		a = page.find('a',{'class':'pv-top-card-v2-section__link pv-top-card-v2-section__link-education mb1'})
		a= a.text
		
		if ('IIPS' in a or 'I.I.P.S.' in a or 'Iips' in a or 'International Institute Of Professional Studies' in a or 'International Institute of Professional Studies' in a or 'international institute of professional studies' in a or 'International institute of professional studies' in a ) :#and ('indore' in b or 'Indore' in b):
							#L.append(link)
							fetchData(page)
							print("y")
		
				
	df  = pandas.DataFrame(d)
	df.to_csv("output.csv")
	return d