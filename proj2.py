#proj2.py

import requests
import re
from bs4 import BeautifulSoup
#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')


 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
 
for story_heading in soup.find_all(class_="story-heading")[0:10]: 
    print(story_heading.getText())
    
## Your Problem 1 solution goes here


#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

base_url = 'https://www.michigandaily.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
 
thediv=soup.find(class_="view-most-read")
items=thediv.find_all("li")
for i in items:
    print(i.getText())

## Your Problem 2 solution goes here


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")
base_url = 'http://newmantaylor.com/gallery.html'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
 
images=soup.find_all("img")

for i in images:
    if i.get("alt"):
    	print (i.get("alt"))
    else:
    	print ("No alternative text provided!")


### Your Problem 3 solution goes here


#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")


emaillist=[]
pages=["https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_valu e=&rid=4"]
def get_email(aurl):
	base_url = aurl
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, "html.parser")

	links=soup.find_all("a")
	for a in links:
		ad=str(a.get("href"))
		match=re.match(r'.+@umich.edu',ad)
		if match:
			email=a.get_text()
			# print (email)
			emaillist.append(email)
		# else:
		# 	print("email not found")
def get_people(aurl):
	base_url = aurl
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, "html.parser")
	divs=soup.find_all("div", class_="field-item even")
	for div in divs:
		if div.a:
			short=div.a.get("href")
			# print (short)
			longurl="https://www.si.umich.edu"+short
			get_email(longurl)

def get_next_page(aurl):
	base_url = aurl
	r = requests.get(base_url)
	soup = BeautifulSoup(r.text, "html.parser")
	ali=soup.find('li',class_="pager-next")
	if ali:
		if ali.a:
			short=ali.a.get("href")
			# print (short)
			longurl="https://www.si.umich.edu"+short
			pages.append(longurl)
			get_next_page(longurl)
	# else:
	# 	print ("no!")

get_next_page("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_valu e=&rid=4")

if pages!= []:
	for i in pages:
		get_people(i)


if emaillist!=[]:
	count=1
	for i in emaillist:
		print (str(count)+" "+i)
		count+=1



### Your Problem 4 solution goes here
