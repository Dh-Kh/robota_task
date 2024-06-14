from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
#from webdriver_manager.chrome import ChromeDriverManager
from re import findall
from typing import Union
from time import sleep
import os
from dotenv import load_dotenv

load_dotenv()

SELENIUM_URL = os.getenv("SELENIUM_URL")

class SeleniumRobota(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SeleniumRobota, cls).__new__(cls, *args, **kwargs)
            options = Options()
            options.add_argument('--headless')
            options.add_argument("--no-sandbox")
            cls._instance._driver = webdriver.Remote(
                command_executor=SELENIUM_URL,
                options=options
            )
        return cls._instance
            
    def parser(self, url: str, key_word: str) -> Union[str, int]:
    
        self._driver.get(url)   

        try:
            wait = WebDriverWait(self._driver, 10)
            input_field = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@_ngcontent-app-desktop-c77]')
                )
            )
            input_field.clear()
            input_field.send_keys(key_word)
            input_field.send_keys(Keys.ENTER)
            count = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, '//div[@_ngcontent-app-desktop-c128]')
                )
            )
            int_list = findall(r'\d+', count.text)
            return int("".join(int_list))
            
        except TimeoutException:
            return "TimeoutException"
        finally:
            self._driver.close()


#s = SeleniumRobota()
#amount = s.parser("https://robota.ua/", "junior")
#print(amount)
#print(isinstance(amount, int))
