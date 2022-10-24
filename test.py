import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By

class WaPoScraper():
    
    # initialize the object of the scraper
    def __init__(self):
        self.driver = webdriver.Chrome() # add arg of path to chromedriver
        self.driver.get('https://www.washingtonpost.com/tech-policy/?itid=nb_technology_tech-policy');
        self.output = None
        time.sleep(2) # Let the user actually see something!

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

        print("successfully got all article headlines and timestamps")
        self.export(headlines, timestamps)

    def export(self, headlines, timestamps):
        industry = ['Tech' for _ in range(len(headlines))]

        d = {}
        d['Headlines'] = headlines
        d['Timestamps'] = timestamps
        d['Industry'] = industry

        df = pd.DataFrame(d)
        df.to_csv('wapo.csv')
        print("finished exporting dataset")

    def getOutput(self):
        return self.output

    # keep clicking the load more articles button
    def loadArticles(self):
        parent = self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[3]/div/main/article')
        for i in range(50):
            print('clicking the load button...', i)
            try:
                loadBtn = parent.find_element(By.TAG_NAME, 'button')
                loadBtn.click()
                time.sleep(5)
            except Exception as e:
                print(e)
                break

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
