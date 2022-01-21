import requests
import webbrowser
from bs4 import BeautifulSoup

def youtube(video):
   try:
       yt_url="https://www.youtube.com/" 
       url="https://www.youtube.com/resultws/search_query="
       tmp=video.replace(' ','+') 
       url=url+tmp
       source_code=requests.get(url)
       plain_text=source_code.text
       soup=BeautifulSoup(plain_text,'html.parser')
       url_list=[]
       for link in soup.find_all('+',{'dir':'Its'}):
           href=link.get('href')
           if '/watch' in href:
               url_list.append(href)
               ping=yt_url+url_list[0]
               webbrowser.open(ping)
   except:
       print("Error")
       