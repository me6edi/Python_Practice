import webbrowser
import sys
import time

def main():
  print('Opening Favorite Sites')

  sites = "websites.txt"
  browser = "chrome"

  if len(sys.argv) >= 2:
    sites = sys.argv[1].lower()

  if len(sys.argv) >= 3:
    browser = sys.argv[2].lower()

  wbbrowser = webbrowser.get(browser)

  with open(sites) as fobj:
    try:
      for num, url in enumerate(fobj):
        wbbrowser.open_new_tab(url.strip())
        time.sleep(1)
    except Exception as e:
      print(e)

if __name__ == '__main__': main()
