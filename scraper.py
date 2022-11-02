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
        self.d = {
            'Headlines' : [],
            'Timestamps' : [],
            'Industry' : []
        }
        self.seen = set()
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
            if o not in self.seen:
                h = o.find_element(By.TAG_NAME, 'h3').text
                t = o.find_elements(By.TAG_NAME, 'span')[-1].text
                self.seen.add(o)
            
                headlines.append(h)
                timestamps.append(t)

        self.export(headlines, timestamps)

    def export(self, headlines, timestamps):
        for i in range(len(headlines)):
            self.d['Headlines'].append(headlines[i])
            self.d['Timestamps'].append(timestamps[i])
            self.d['Industry'].append('Tech')

        df = pd.DataFrame(self.d)
        df.to_csv('wapo.csv')
        print("finished exporting dataset of size", len(df.index))

    # keep clicking the load more articles button
    def loadArticles(self):
        parent = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/main/article')

        now = datetime.now()
        future = now + timedelta(minutes = 10)
        cnt = 0
        while True:
            print('clicking the load button...', datetime.now())
            try:
                loadBtn = parent.find_element(By.TAG_NAME, 'button')
                loadBtn.click()
                time.sleep(3)
            except Exception as e:
                print(e)
                break
            finally:
                if cnt % 10 == 0:
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
