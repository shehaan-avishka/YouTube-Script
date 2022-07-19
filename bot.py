from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options

import time

def buildBot():
    chrome_options = Options()
    chrome_options.add_argument("--headless")

    #build bot
    bot = webdriver.Chrome(options=chrome_options)

    print("\n\n\n\n\n\n")
    #display date and time
    print(datetime.today())
    return bot


def takeUserInput():
    name = input("Hey tell me your favorite song : ")
    return name


def botTask(bot,name):
    bot.get('https://www.youtube.com')

    #console
    print("\nGot it I am trying to do my best, So now I am in youtube")
    time.sleep(2)

    #find search bar and insert name
    bot.find_element("xpath",'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/'
                        +'div[2]/ytd-searchbox/form/div[1]/div[1]/input').send_keys(name)
    time.sleep(2)

    #clice search button
    bot.find_element("xpath",'/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button').click()
    time.sleep(2)

    #select top sond on the list
    bot.find_element("xpath",'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-'
                            +'search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-'
                            +'renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').click()
    print("Hey found your song enjoy\nGood day...!\n\n\n\n")

def quitBot():
    decission = input("Stop the song [Y]: ").lower()
    print("\n\n\n\n\n\n")

    while decission != "y":
        decission = input("Stop the song [Y]: ").lower()

    musicBot.quit()


if __name__ == "__main__":
    musicBot = buildBot()
    inputFromUser = takeUserInput()
    botTask(musicBot,inputFromUser)
    quitBot()

    
    


