#!usr/bin/python2

import time
import webbrowser 
from datetime import date
from urllib2 import tablerequests
from requests import get
from bs4 import BeautifulSoup

a='''
PRESS 1 : Enter any word you want to search: 
PRESS 2 : Enter any word  for which you want the image: 
PRESS 3 : This will give URL for entered word: 
PRESS 4 : Current Date and Time of System : 
PRESS 5 : Default browser is opened : 
PRESS 6 : IP of all the present network :
PRESS 7 : Check owner mail ID and Contact no :

'''
print a

x=raw_input("PRESS a number:")
print x



if(x=='1'):
       p=raw_input("Enter the word you want to search :")
       p1=p.strip()
       var=p1.split() 
       print var
       for i in var:
              webbrowser.open_new_tab("https://www.google.com/search?client=ubuntu&channel=fs&q="+i)



if(x=='2'):
       p=raw_input("Enter the word for which you want to search the image:")
       p1=p.strip()
       var=p1.split() 
       print var
       for i in var:
              webbrowser.open_new_tab("https://www.google.co.in/search?hl=en&tbm=isch&source=hp&biw=1170&bih=567&ei=0K_-WvaaM4v9vgT52YrgDA&q="+i)




if(x=='3'):
       '''p=raw_input("Enter the word for which you want url :")
       p1=p.strip()
       var=p1.split() 
       print var'''
       url='https://www.google.com/search?client=ubuntu&channel=fs&q=hello&ie=utf-8&oe=utf-8'
       response=get(url)
       print response.text[:500]
       html_soup=BeautifulSoup(response.text,'html_parser')
       type(html_soup)






if(x=='4'):
        p="The date and time of the system is :"
        d=date.today()
        print d
        t=time.time()
        print t


       


