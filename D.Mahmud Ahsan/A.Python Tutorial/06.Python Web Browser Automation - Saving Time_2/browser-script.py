import webbrowser 
import sys
import time

def main():
	print('Opening Favorite Sites')\

sites = "website.txt"
browser = "chrome"

webbrowser = webbrowser.get(browser)

with open(sites) as fobj:
	try:
	 	for num, url in enumerate(fobj):
	 		webbrowser.open_new_tab(url.strip())
	 		time.sleep(1)
	 except Exception as e:
	 	print(e)
 
if __name__ == '__main__': main()