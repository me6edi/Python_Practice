# ----------------------------------------
# Connection
# ----------------------------------------

from urllib.request import urlopen

html_data = urlopen('http://fusionbd.com/')
print(html_data.read())

#---------------------------------------
# Data parsing
#---------------------------------------

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
#
# html_data = urlopen('http://ww.bbc.com')
# bs_obj = BeautifulSoup(html_data.read(),
#                        'html.parser')
#
#
# print(bs_obj.h1)
# print(bs_obj.h1.string)

