from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from jsonToCsv import jsonToCsv
from prompt import Prompt

class ReelGoodScraper:
    """
    A class to scrape the movie aggregation website ReelGood.com
    Do not re-distribute, this script is against Terms of Service.
    """
    def __init__(self, website, showType, sortBy, numShows):
        self.website = website
        self.showType = showType
        self.sortBy = sortBy
        self.numShows = numShows

        # Place your chrome driver path in this folder
        # Download chrome driver here: https://chromedriver.chromium.org/downloads 
        options = Options()
        options.headless = True
        self.cwd = os.getcwd()
        self.driver = webdriver.Chrome(f"{self.cwd}/chromedriver", options=options)

    def getPageSource(self, driver, url):
        self.driver.get(url)
        sleep(5) # must wait for javascript elements to load up
        htmlPage = driver.page_source
        return htmlPage

    def scrapePage(self):
        urlBuilder = f"https://reelgood.com/{self.showType}/source/{self.website}?{self.sortBy}&offset="

        # The page offset value is in multiples of 50.
        for i in range(0, self.numShows, 50):
            url = urlBuilder + str(i)
            myfile = open(f"{self.cwd}/{self.website}-{self.showType}-{i}.json" , mode="w")
            html = self.getPageSource(self.driver, url)
            soup = BeautifulSoup(html, 'html.parser')
            stuff = soup.find_all('script')

            # Manually find the stuff because I don't know regex.
            target = str(stuff[16])

            # Remove the extra json at the front.
            split_target = target.split("{", 8)
            target = split_target[8]

            # Remove the extra json at the back.
            split_target = target.rsplit(",\"listings\"")
            target = split_target[0]
            target = "{" + target

            # Remove the metadata.
            split_target = target.split(",\"meta\"")
            target = split_target[0]
            target = target

            print(f"Finished scraping page: {i}")
            myfile.write(target)
            myfile.close()
        self.driver.quit() # Very important to quit or the driver remains on your computer.

    def convertJsonToCsv(self):
        converter = jsonToCsv()
        converter.convert(self.website, self.showType, self.numShows, self.cwd)
        
def main():
    prompt = Prompt()
    website, showType, sortBy, numShows = prompt.promptInput()

    print(f"\nStarting to scrape {website}")
    scraper = ReelGoodScraper(website, showType, sortBy, numShows)
    scraper.scrapePage()
    print(f"Finished scraping {website}")

    scraper.convertJsonToCsv()
    print(f"CSV file created: {website}-{showType}.csv")

if __name__ == "__main__":
    main()
