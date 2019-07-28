
from bs4 import BeautifulSoup
import requests
url = "https://www.amazon.com/Dimension-Wireless-Bluetooth-Headphones-Cancellation/dp/B07L6RKPHT/ref=gbps_img_m-9_2862_e3edad73?smid=A207MQ9SW70SHE&pf_rd_p=9b8adb89-8774-4860-8b6e-e7cefc1c2862&pf_rd_s=merchandised-search-9&pf_rd_t=101&pf_rd_i=15529609011&pf_rd_m=ATVPDKIKX0DER&pf_rd_r=JB2ZTDSTSHPB355BABBH"

# add header
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")

nombre = soup.title.string
price = soup.find(id="priceblock_dealprice_lbl")#.get_text()
print('el nombre es:'+nombre)
print('El precio es:'+price)
