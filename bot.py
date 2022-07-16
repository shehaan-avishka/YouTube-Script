from selenium import webdriver
from datetime import datetime
import time

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-gpu")
#chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")
# chrome_options.headless = True # also works options=chrome_options

bot = webdriver.Chrome(options=chrome_options)
print("\n\n\n\n\n\n")
print(datetime.today())


name = input("Hey tell me your favorite song : ")
#bot = webdriver.Chrome()
bot.get('https://www.youtube.com')
print("\nGot it I am trying to do my best, So now I am in youtube")
time.sleep(2)
bot.find_element("xpath",'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(name)
time.sleep(2)
bot.find_element("xpath",'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button').click()
time.sleep(2)
bot.find_element("xpath",'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()

print("Hey found your song enjoy\nGood day...!\n\n\n\n")

decission = input("Stop the song [Y]: ").lower()
print("\n\n\n\n\n\n")
while decission != "y":
    decission = input("Stop the song [Y]: ").lower()

bot.quit()


