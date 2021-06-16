from bs4 import BeautifulSoup, element
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
import json
import time
import os

#api kısmı
url = ('https://www.virustotal.com/vtapi/v2/file/scan')
os.system("cls")
print("="*15+ "\n" + "Emrovsky Antivirus" + "\n" + "="*15 )
print("Taratacağınız dosyayı programın olduğu klasöre sürükleyin")
fileqwe = input("Lütfen taratılacak dosyanın adını giriniz : ")

dosya = open("apikey.txt","r",encoding="utf-8")
apikey = (dosya.readline())

params = {'apikey': apikey}

files = {'file': (fileqwe, open(fileqwe, 'rb'))}

response = requests.post(url, files=files, params=params)
data = json.loads(response.text)
linkkk = data['permalink']
print("Virus taraması sonuçları 2 dakika içerisinde bu linkte olacaktır " +linkkk)
time.sleep(5)

#api kısmı

#indiriliyor animasyon
a = 1
b = "="
c = ">"
dosya = "Dosya yükleniyor... "


while True:
    a += 1
    print(dosya+b*a+c)
    time.sleep(1)
    os.system("cls")
    if a == 150:
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        os.system("ping " + linkkk)
        os.system("cls")
        break
#indiriliyor animasyonu


weblink = linkkk


if weblink.endswith("/details"):
    weblink = weblink.replace("/details", "/summary")

option = Options()
option.headless = True
driver = webdriver.Chrome(executable_path='C:/Users/ozguc/OneDrive/Desktop/Python Günlükleri/python antivirüs/chromedriver.exe',options=option)

driver.get(weblink)

def expand_shadow_element(element):
  shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

#the above becomes 
shadow_section = expand_shadow_element(driver.find_element_by_tag_name("file-view"))
shadow_section2 = expand_shadow_element(shadow_section.find_element_by_css_selector('vt-ui-main-generic-report'))
shadow_section3 = expand_shadow_element(shadow_section2.find_element_by_css_selector('vt-ui-detections-widget'))
html = shadow_section3.get_attribute('innerHTML')
driver.close()
soup = BeautifulSoup(html, "lxml")
div = soup.find('div', {'class':"engines"})

informations = str(div.text)
informations = informations.replace(" ", "")
os.system("cls")
print("Sonuçlar Aşağıdaki Gibidir" + "\n")
print("="*15+f"\n Virüs bulunan/Antivirüs programı: {informations}\n"+"="*15)
print("Hangi antivirüs programları virüs algılaşmış daha detaylı bakmak için : " + linkkk)