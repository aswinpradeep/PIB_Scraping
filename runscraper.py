import urllib.request 
from inscriptis import get_text
from langdetect import detect ,detect_langs
import re
import requests
from bs4 import BeautifulSoup
import pdfkit 
import csv
from googletrans import Translator
from pyvirtualdisplay import Display

display = Display()
display.start()

translator = Translator()
#1653267 - 2020 limit
#1479900 - 2017 limit
for i in range(1653267,1479900,-1):
    try:
        # print(i)
        url="https://www.pib.gov.in/PressReleasePage.aspx?PRID="+str(i)
        # print("Url=",url)
        html = urllib.request.urlopen(url).read().decode('utf-8') 
        text = get_text(html) 
        # print("Textlength=",len(text))
        if(len(text)>250):
            fnametxt = str(i)+".txt"
            file1 = open(fnametxt,"w")
            file1.write(text) 
            file1.close()

            fnamepdf=str(i)+".pdf"
            pdfkit.from_url(url, fnamepdf)


            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'lxml')
            h2text=''
            v2=''
            for heading in soup.find_all(["h2"]):
                h2text=h2text+heading.text.strip()
            # print("Heading=",h2text.strip())
            mydivs = soup.findAll("div", {"class": "ReleaseDateSubHeaddateTime text-center pt20"})
            for div in mydivs: 
                    div1=str(div)
                    start = ':'
                    end = '<'
                    s = div1
                    v2=s[s.find(start)+len(start):s.rfind(end)]
                    print("Timestamp=",v2.strip())       
            ln=translator.detect(h2text.strip()).lang
            # print(ln)
            if(ln=='bn'):
                ln='NA'
            row_contents = [i,url,len(text),v2.strip(),ln,h2text.strip()]
            print(row_contents)
            with open(r'piboutput.csv', 'a') as f:
                writer = csv.writer(f)
                writer.writerow(row_contents)
    except:
        print(i," failed")
        file2 = open("failedfiles.txt","a")
        file2.write("\n")
        file2.write(str(i)) 
        file2.close()
