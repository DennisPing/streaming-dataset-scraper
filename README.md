# streaming-dataset-scraper

Scrape entire datasets of movies and tv shows from the site ReelGood.com

## Python and Pip Requirements

* Python 3
* beautifulsoup4
* selenium

## Chrome Driver

* Selenium requires a Chrome driver in order to scrape a website
* Download the same Chrome driver version as your current Chrome browser
* Chrome driver download: https://chromedriver.chromium.org/downloads 
* Paste the Chrome driver in the folder with all the other Python scripts

## How to Run

`python scraper.py`

## Example Input

```rtf
Valid websites to scrape:
1. amazon
2. apple_tv
3. crunchyroll_free
4. crunchyroll_premium
5. disney_plus
6. hbo
7. hbo_max
8. hulu
9. netflix
10. peacock
What streaming service to scrape: 9
Movies or TV Shows?
1. movies
2. tv-shows
>> 1
Sort By?
1. Popular
2. IMDb score
3. ReelGood Score
>> 1
How many movies/tv-shows to scrape: 500
```

## Output

* This script first stores the data in JSON files
* Then it parses the JSON files and merges them into one nice CSV file
* After the CSV file is created, it is safe to delete the JSON.
