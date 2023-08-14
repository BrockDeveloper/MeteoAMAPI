from assets.xpath import XPATH
from selenium import webdriver
from models.forecast import *
from selenium.webdriver.common.by import By


class WebScraper():

    ENDPOINT: str = "https://www.meteoam.it/it/meteo-citta/{}"


    def __init__(self, location: str):

        try:
            self.location = location
            
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            options.add_argument("--start-maximized")

            self.driver = webdriver.Firefox(options=options)
            self.driver.get(self.ENDPOINT.format(location))

        except:
            raise Exception("Unable to initialize webdriver")
        
    
    def __del__(self):
            
        self.driver.quit()
        del self
        

    def __get_element(self, xpath: str, attribute: str) -> str:

        try:
            return self.driver.find_element(By.XPATH, xpath).get_attribute(attribute)

        except:
            raise Exception("Unable to get element")
        
    
    def get_data(self) -> dict:

        data = {}

        try:

            for xpath in XPATH:
                data[xpath["name"]] = self.__get_element(xpath["xpath"], xpath["get"])

        except:
            raise Exception("Unable to get data")
        
        return data
    

    def get(self):

        data = self.get_data()

        return Forecast.from_dict(data)