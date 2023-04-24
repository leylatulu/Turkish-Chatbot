# GEREKLİ KÜTÜPHANELER
import requests
from bs4 import BeautifulSoup
import pandas as pd

#################################
# WEB SCRAPING - Miuul & VBO
#################################
# MIUUL faq
# 1.site: https://www.miuul.com/sifirdan-baslayanlar-icin-veri-bilimi#faq
# 2.site: https://www.miuul.com/data-engineer-path#faq
# 3.site: https://www.miuul.com/data-analyst-path#faq
# 4.site: https://www.miuul.com/data-scientist#faq
# 5.site: https://www.miuul.com/machine-learning-engineer-path#faq

#############################
# 1.site için çekme işlemi:
#############################
sorular1 = []
cevaplar1 = []
url1 = "https://www.miuul.com/sifirdan-baslayanlar-icin-veri-bilimi#faq"
response = requests.get(url1)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.find('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}).text)
# print(soup.find('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}).text)
for soru in soup.find_all('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}):
    sorular1.append(soru.text)

for cevap in soup.find_all('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}):
    cevaplar1.append(cevap.text)

sorular1 = [soru.replace("\n", "").strip() for soru in sorular1]

cevaplar1 = [cevaplar.replace("\n", "") for cevaplar in cevaplar1]
cevaplar1 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in cevaplar1] # \xa0

tag = ["sifirdan-baslayanlar-icin-veri-bilimi"] * len(sorular1)

# sorular cevaplar ve tag ları birleştirme
df1 = pd.DataFrame({"tag": tag, "soru": sorular1, "cevap": cevaplar1})

#sorucevap1 = dict(zip(sorular, cevaplar))
#sorucevap1.to_excel("sorucevap1.xlsx")
#df1 = pd.DataFrame(sorucevap1.items(), columns=['Soru', 'Cevap'])
#df1.to_excel("miuul_sifirdan_baslayanlar_icin_veri_bilimi.xlsx", index=False)

#############################
# 2.site için çekme işlemi:
#############################
sorular2 = []
cevaplar2 = []
url2 = "https://www.miuul.com/data-engineer-path#faq"
response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")

# print(soup.find('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}).text)
# print(soup.find('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}).text)

for soru in soup.find_all('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}):
    sorular2.append(soru.text)

for cevap in soup.find_all('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}):
    cevaplar2.append(cevap.text)

sorular2 = [soru.replace("\n", "").strip() for soru in sorular2]

cevaplar2 = [cevaplar.replace("\n", " ") for cevaplar in cevaplar2]
cevaplar2 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in cevaplar2] # \xa0
cevaplar2 = [cevaplar.replace("\r", "") for cevaplar in cevaplar2] # \r
cevaplar2 = [cevaplar.replace(".  ", ". ").replace(":  ", ": ") for cevaplar in cevaplar2]

tag = ["data-engineer-path"] * len(sorular2)

# sorular cevaplar ve tag ları birleştirme
df2 = pd.DataFrame({"tag": tag, "soru": sorular2, "cevap": cevaplar2})

#############################
# 3.site için çekme işlemi:
#############################
sorular3 = []
cevaplar3 = []
url3 = "https://www.miuul.com/data-analyst-path#faq"
response = requests.get(url3)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}):
    sorular3.append(soru.text)

for cevap in soup.find_all('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}):
    cevaplar3.append(cevap.text)

sorular3 = [soru.replace("\n", "").strip() for soru in sorular3]

cevaplar3 = [cevaplar.replace("\n", "") for cevaplar in cevaplar3]

tag = ["data-analyst-path"] * len(sorular3)

df3 = pd.DataFrame({"tag": tag, "soru": sorular3, "cevap": cevaplar3})

#############################
# 4.site için çekme işlemi:
#############################
sorular4 = []
cevaplar4 = []
url4 = "https://www.miuul.com/data-scientist#faq"
response = requests.get(url4)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.find('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}).text)
# print(soup.find('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}).text)
for soru in soup.find_all('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}):
    sorular4.append(soru.text)

for cevap in soup.find_all('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}):
    cevaplar4.append(cevap.text)

sorular4 = [soru.replace("\n", "").strip() for soru in sorular4] # gereksiz kısımları sil

cevaplar4 = [cevaplar.replace("\n", "").strip() for cevaplar in cevaplar4] # gereksiz kısımları sil
cevaplar4 = [cevaplar.replace("\xa0\r", " ").strip() for cevaplar in cevaplar4] # \xa0\r
cevaplar4 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in cevaplar4] # \xa0
cevaplar4 = [cevaplar.replace("\r", " ").strip() for cevaplar in cevaplar4] # \r

tag = ["data-scientist"] * len(sorular4)

df4 = pd.DataFrame({"tag": tag, "soru": sorular4, "cevap": cevaplar4})


#############################
# 5.site için çekme işlemi:
#############################
sorular5 = []
cevaplar5 = []
url5 = "https://www.miuul.com/machine-learning-engineer-path#faq"
response = requests.get(url5)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'text-dark-blue ff-medium fs-23 text-decoration-none d-block position-relative'}):
    sorular5.append(soru.text)

for cevap in soup.find_all('div', {'class': 'col-lg-9 ff-regular fs-18 mt-4 pe-5'}):
    cevaplar5.append(cevap.text)

sorular5 = [sorular.replace("\n", "").strip() for sorular in sorular5]

cevaplar5 = [cevaplar.replace("\n", "") for cevaplar in cevaplar5]
cevaplar5 = [cevaplar.replace("\xa0", "") for cevaplar in cevaplar5] # \xa0

tag = ["machine-learning-engineer-path"] * len(sorular5)

df5 = pd.DataFrame({"tag": tag, "soru": sorular5, "cevap": cevaplar5})


###############################################################
###############################################################

# VBO faq
# 1.site: https://bootcamp.veribilimiokulu.com/bootcamp-programlari/veri-bilimci-yetistirme-programi/
# 2.site: https://bootcamp.veribilimiokulu.com/bootcamp-programlari/data-engineering-bootcamp/
# 3.site: https://bootcamp.veribilimiokulu.com/bootcamp-programlari/veri-analisti-yetistirme-programi/
# 4.site: https://bootcamp.veribilimiokulu.com/bootcamp-programlari/mlops-bootcamp/
# 5.site: https://bootcamp.veribilimiokulu.com/bootcamp-programlari/aws-cloud-technical/
# 6.site: https://bootcamp.veribilimiokulu.com/bootcamp-programlari/microsoft-azure-cloud-bootcamp/



#############################
# 1.site için çekme işlemi:
#############################
vbo_sorular1 = []
vbo_cevaplar1 = []
url1 = "https://bootcamp.veribilimiokulu.com/bootcamp-programlari/veri-bilimci-yetistirme-programi/"
response = requests.get(url1)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'elementor-accordion-title'}):
    vbo_sorular1.append(soru.text)

for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix active-default'}):
    vbo_cevaplar1.append(cevap.text)
for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix'}):
    vbo_cevaplar1.append(cevap.text)


vbo_cevaplar1 = [cevaplar.replace("\n", " ") for cevaplar in vbo_cevaplar1]
vbo_cevaplar1 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in vbo_cevaplar1] # \xa0
#vbo_cevaplar = [cevaplar.replace("•             ", " ").strip() for cevaplar in vbo_cevaplar]

# TODO: Veri temizleme işlemleri yapılacak.
tag = ["veri-bilimci-yetistirme-programi"] * len(vbo_sorular1)

df6 = pd.DataFrame({"tag": tag, "soru": vbo_sorular1, "cevap": vbo_cevaplar1})


#############################
# 2.site için çekme işlemi:
#############################
vbo_sorular2 = []
vbo_cevaplar2 = []
url2 = "https://bootcamp.veribilimiokulu.com/bootcamp-programlari/data-engineering-bootcamp/"
response = requests.get(url2)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'elementor-accordion-title'}):
    vbo_sorular2.append(soru.text)

for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix active-default'}):
    vbo_cevaplar2.append(cevap.text)
for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix'}):
    vbo_cevaplar2.append(cevap.text)

# TODO: Veri temizleme işlemleri yapılacak.
vbo_sorular2 = [sorular.strip() for sorular in vbo_sorular2]

vbo_cevaplar2 = [cevaplar.replace("\n", " ") for cevaplar in vbo_cevaplar2]
vbo_cevaplar2 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in vbo_cevaplar2] # \xa0
#cevaplar = [cevaplar.replace("\r", "") for cevaplar in cevaplar] # \r
#cevaplar = [cevaplar.replace(".  ", ". ").replace(":  ", ": ") for cevaplar in cevaplar]

tag = ["data-engineering-bootcamp"] * len(vbo_sorular2)

df7 = pd.DataFrame({"tag": tag, "soru": vbo_sorular2, "cevap": vbo_cevaplar2})

#############################
# 3.site için çekme işlemi:
#############################
vbo_sorular3 = []
vbo_cevaplar3 = []
url3 = "https://bootcamp.veribilimiokulu.com/bootcamp-programlari/veri-analisti-yetistirme-programi/"
response = requests.get(url3)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'elementor-accordion-title'}):
    vbo_sorular3.append(soru.text)

for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix active-default'}):
    vbo_cevaplar3.append(cevap.text)
for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix'}):
    vbo_cevaplar3.append(cevap.text)

# TODO: Veri temizleme işlemleri yapılacak.
#vbo_sorular = [sorular.strip() for sorular in vbo_sorular]

vbo_cevaplar3 = [cevaplar.replace("\n", " ") for cevaplar in vbo_cevaplar3]
vbo_cevaplar3 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in vbo_cevaplar3] # \xa0
#cevaplar = [cevaplar.replace("\r", "") for cevaplar in cevaplar] # \r
#cevaplar = [cevaplar.replace(".  ", ". ").replace(":  ", ": ") for cevaplar in cevaplar]

tag = ["veri-analisti-yetistirme-programi"] * len(vbo_sorular3)

df8 = pd.DataFrame({"tag": tag, "soru": vbo_sorular3, "cevap": vbo_cevaplar3})

#############################
# 4.site için çekme işlemi:
#############################
vbo_sorular4 = []
vbo_cevaplar4 = []
url4 = "https://bootcamp.veribilimiokulu.com/bootcamp-programlari/mlops-bootcamp/"
response = requests.get(url4)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'elementor-accordion-title'}):
    vbo_sorular4.append(soru.text)

for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix active-default'}):
    vbo_cevaplar4.append(cevap.text)
for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix'}):
    vbo_cevaplar4.append(cevap.text)

# TODO: Veri temizleme işlemleri yapılacak.
#vbo_sorular = [sorular.strip() for sorular in vbo_sorular]

vbo_cevaplar4 = [cevaplar.replace("\n", " ") for cevaplar in vbo_cevaplar4]
vbo_cevaplar4 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in vbo_cevaplar4] # \xa0
#cevaplar = [cevaplar.replace("\r", "") for cevaplar in cevaplar] # \r
#cevaplar = [cevaplar.replace(".  ", ". ").replace(":  ", ": ") for cevaplar in cevaplar]

tag = ["mlops-bootcamp"] * len(vbo_sorular4)

df9 = pd.DataFrame({"tag": tag, "soru": vbo_sorular4, "cevap": vbo_cevaplar4})


#############################
# 5.site için çekme işlemi:
#############################
vbo_sorular5 = []
vbo_cevaplar5 = []
url5 = "https://bootcamp.veribilimiokulu.com/bootcamp-programlari/aws-cloud-technical/"
response = requests.get(url5)
soup = BeautifulSoup(response.content, "html.parser")

for soru in soup.find_all('a', {'class': 'elementor-accordion-title'}):
    vbo_sorular5.append(soru.text)

for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix active-default'}):
    vbo_cevaplar5.append(cevap.text)
for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix'}):
    vbo_cevaplar5.append(cevap.text)

#vbo_sorular = [sorular.strip() for sorular in vbo_sorular]

vbo_cevaplar5 = [cevaplar.replace("\n", " ") for cevaplar in vbo_cevaplar5]
vbo_cevaplar5 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in vbo_cevaplar5] # \xa0
#cevaplar = [cevaplar.replace("\r", "") for cevaplar in cevaplar] # \r
#cevaplar = [cevaplar.replace(".  ", ". ").replace(":  ", ": ") for cevaplar in cevaplar]

tag = ["aws-cloud-technical"] * len(vbo_sorular5)

df10 = pd.DataFrame({"tag": tag, "soru": vbo_sorular5, "cevap": vbo_cevaplar5})


#############################
# 6.site için çekme işlemi:
#############################
vbo_sorular6 = []
vbo_cevaplar6 = []
url6 = "https://bootcamp.veribilimiokulu.com/bootcamp-programlari/microsoft-azure-cloud-bootcamp/"
response = requests.get(url6)
soup = BeautifulSoup(response.content, "html.parser")
azure_soru=[]
azure_cevap = []

# SORULARI ÇEK
for soru in soup.find_all('a', {'class': 'elementor-accordion-title'}):
    azure_soru.append(soru.text)

vbo_sorular6.extend(azure_soru[9::])

# CEVAPLARI ÇEK
for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix deactive-default'}):
    azure_cevap.append(cevap.text)

for cevap in soup.find_all('div', {'class': 'elementor-tab-content elementor-clearfix'}):
    azure_cevap.append(cevap.text)

vbo_cevaplar6.append(azure_cevap[1]) # 2. sorunun cevabını üstten çektim
vbo_cevaplar6.extend(azure_cevap[10::]) # asıl cevapların olduğu kısımları ekledim aynı listeye

# VERİ TEMİZLEME
vbo_cevaplar6 = [cevaplar.replace("\n", " ") for cevaplar in vbo_cevaplar6]
vbo_cevaplar6 = [cevaplar.replace("\xa0", " ").strip() for cevaplar in vbo_cevaplar6] # \xa0

tag = ["microsoft-azure-cloud-bootcamp"] * len(vbo_sorular6)

df11 = pd.DataFrame({"tag": tag, "soru": vbo_sorular6, "cevap": vbo_cevaplar6})


#######################################################

# Tüm verileri birleştirme
df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11], ignore_index=True)

df.to_excel("PROJE/data.xlsx", index=False)

#######################################################
#######################################################
#######################################################



