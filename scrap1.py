

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


def getlinks(browser):
	links = ViewBot(browser)
	for l in links:
		base = 

        

def fetchData(page):
	global d
	name = page.find('h1',{'class':'pv-top-card-section__name Sans-26px-black-85%'}).text
	name = name.replace('\n','').strip()
	
	d['name'] = name
	d["exp"] = {}
	exp = page.find("section",{'id':'experience-section'})
	companies = exp.find_all('div',{'class':'pv-entity__summary-info pv-entity__summary-info--v2'})
	for a in companies:
		d['exp']['profile']= a.find('h3',{'class':'Sans-17px-black-85%-semibold'}).text
		d['exp']['company'] = a.find('span',{'class':'pv-entity__secondary-title'}).text
		b = a.find('h4',{'class':'pv-entity__date-range inline-block Sans-15px-black-70%'})
		c = b.find_all('span')
		d['exp']['time'] = c[1].text
		k = page.find_all('p',{'class':'pv-entity__secondary-title pv-entity__degree-name pv-entity__secondary-title Sans-15px-black-85%'})
	for i in k:
			d["course"] = i.find('span',{'class':'pv-entity__comma-item'}).text
	l = page.find('p',{'class':'pv-entity__dates Sans-15px-black-70%'})
	x = l.find_all("time")
	d['years'] = x[0].text+"-"+x[1].text
	return 
			
#browser.find_element_by_css_selector('button.next')
								#e = page.find_elements_by_class_name("next")#.click()
								#c =  page.find("button",{'class':''})
								#browser.find_element_by_xpath('//*[@id="ember3554"]/li[2]/button/span/li-icon/svg').click()
								#print(e)

								
								
							#	num = 0#num -1
