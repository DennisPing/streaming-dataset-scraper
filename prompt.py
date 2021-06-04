class Prompt:
    """
    A class to prompt the user for input and check the input values.
    """

    def __init__(self):
        pass

    def promptInput(self):
        # Add as many valid sites as you want. I only added 10.
        validSites = ['amazon', 'apple_tv', 'crunchyroll_free', 'crunchyroll_premium', \
            'disney_plus', 'hbo', 'hbo_max', 'hulu', 'netflix', 'peacock']
        print(f"Valid websites to scrape: ")
        for i, site in enumerate(validSites):
            print(f"{i+1}. {site}")
        website = input("What streaming service to scrape: ")
        website = self.parseWebsite(website)

        showType = input("Movies or TV Shows?\n1. movies\n2. tv-shows\n>> ")
        showType = self.parseShowType(showType)

        sortBy = input("Sort By?\n1. Popular\n2. IMDb score\n3. ReelGood Score\n>> ")
        sortBy = self.parseSortBy(sortBy)

        numShows = input("How many movies/tv-shows to scrape: ")
        numShows = self.parseNumShows(numShows)

        return (website, showType, sortBy, numShows)

    def parseWebsite(self, website):
        try:
            options = {
                '1':'amazon',
                '2':'apple_tv_plus',
                '3':'crunchyroll_free',
                '4':'crunchyroll_premium',
                '5':'disney_plus',
                '6':'hbo',
                '7':'hbo_max',
                '8':'hulu',
                '9':'netflix',
                '10':'peacock'
            }
            return options[website]
        except:
            raise ValueError("Error, invalid website selection.")

    def parseShowType(self, showType):
        try:
            options = {
                '1':'movies',
                '2':'tv'
            }
            return options[showType]
        except:
            raise ValueError("Error, please enter 1 or 2.")
            
    def parseSortBy(self, sortBy):
        try: 
            options = {
                '1':'filter-sort=1',
                '2':'filter-sort=2',
                '3':'filter-sort=8'
            }
            return options[sortBy]
        except:
            raise ValueError("Error, please enter 1, 2, or 3.")
    
    def parseNumShows(self, numShows):
        if not numShows.isnumeric():
            raise ValueError(f"Error, {numShows} must be an integer.")
        if int(numShows) % 50 != 0:
            raise ValueError("Error, the number of shows to scrape must be a multiple of 50.")
        return int(numShows)