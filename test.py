import time
import pandas as pd

from datetime import datetime, timedelta
from selenium import webdriver
from selenium.webdriver.common.by import By

class WaPoScraper():
    
    # initialize the object of the scraper
    def __init__(self):
        self.driver = webdriver.Chrome() # add arg of path to chromedriver
        self.driver.get('https://www.washingtonpost.com/tech-policy/?itid=nb_technology_tech-policy');
        self.output = None
        self.d = {}
        time.sleep(5) # Let the user actually see something!

    # close the chrome instance
    def quit(self):
        self.driver.quit()

    # get article links on page
    def getLinks(self):
        print("loading articles...")
        objs = self.driver.find_elements(By.CSS_SELECTOR,
                                        "div[data-feature-id='homepage/story']")

        headlines = []
        timestamps = []
        for o in objs:
            h = o.find_element(By.TAG_NAME, 'h3').text
            t = o.find_elements(By.TAG_NAME, 'span')[-1].text
            
            headlines.append(h)
            timestamps.append(t)

        print("_____")
        print("exported", len(headlines), "headlines to csv @", datetime.now())
        print("_____")
        self.export(headlines, timestamps)

    def export(self, headlines, timestamps):
        industry = ['Tech' for _ in range(len(headlines))]

        self.d['Headlines'] = headlines
        self.d['Timestamps'] = timestamps
        self.d['Industry'] = industry

        df = pd.DataFrame(d)
        df.to_csv('wapo.csv')
        print("finished exporting dataset")

    # keep clicking the load more articles button
    def loadArticles(self):
        parent = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/main/article')

        now = datetime.now()
        future = now + timedelta(minutes = 10)
        cnt = 0
        while datetime.now() < future:
            print('clicking the load button...', datetime.now())
            try:
                loadBtn = parent.find_element(By.TAG_NAME, 'button')
                loadBtn.click()
                time.sleep(3)
            except Exception as e:
                print(e)
                break
            finally:
                if cnt % 5 == 0:
                    self.getLinks()

                cnt += 1

        print("loaded all articles")
        time.sleep(2)

def main():
    scraper = WaPoScraper()
    try:
        scraper.loadArticles() # first, get all articles on screen
        scraper.getLinks() # parse the articles on screen
        scraper.quit()

    except Exception as e:
        print('failed')
        print(e)
        scraper.quit()
    
main()
