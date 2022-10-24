import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class WaPoScraper():
    
    # initialize the object of the scraper
    def __init__(self):
        self.driver = webdriver.Chrome() # add arg of path to chromedriver
        self.driver.get('https://www.washingtonpost.com/tech-policy/?itid=nb_technology_tech-policy');
        # time.sleep(2) # Let the user actually see something!

    # close the chrome instance
    def quit(self):
        self.driver.quit()

    # get article links on page
    def getLinks(self):
        headings = self.driver.find_elements(By.TAG_NAME, 'h3')
        stories = self.driver.find_elements(By.CLASS_NAME, 'story-headline')
        objs = self.driver.find_elements(By.CSS_SELECTOR,
                                        "div[data-feature-id='homepage/story']")
        for o in objs:
            headline = o.find_element(By.TAG_NAME, 'h3').text
            timestamp = o.find_elements(By.TAG_NAME, 'span')[-1].text

            print(headline, timestamp)

def main():
    scraper = WaPoScraper()
    try:
        scraper.getLinks()
        scraper.quit()
    except Exception as e:
        print('failed')
        print(e)
        scraper.quit()
    
main()
