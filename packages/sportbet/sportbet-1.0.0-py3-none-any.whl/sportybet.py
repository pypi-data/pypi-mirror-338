import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LoginError(Exception):
    def __init__(self, message="Unable to Login"):
        self.message = message
        super().__init__(self.message)

class SportyBet:

    """ Representation of the whole sporty Bet Games """

    def __init__(self):
        self.service = Service()
        self.options = Options()
        self.driver = None
        self.link = 'https://www.sportybet.com'
        self.phone = ''
        self.password = ''
        self.account_balance = None
        self.login_selectors = {
            "phone": (By.NAME, "phone"),
            "password": (By.NAME, "psd")
        }
        self.DEFAULT_PHONE = "08104563274"
        self.DEFAULT_PASSWORD = "Esther20000"
        self.inParentUrl = False
        self.ingamesUrl = False
        self.headless = False

    def configure(self, phone_number='', password='', headless=False):

        if not phone_number or not password:
            raise ValueError("Phone number or Password must not be empty")
        self.phone = phone_number
        self.password = password
        self.headless = headless
        

    def get_account_info(self):
        if self.phone and self.password:
            return f"Phone: {self.phone}, \nPassword: { '*' * len(self.password)}"
        else:
            raise ValueError("No Phone Number or Password try running 'SportyBet().configure()'")
        
    def login(self):

        if self.driver is None:

            if self.headless == True:
                self.options.add_argument('--headless')

            self.driver = webdriver.Chrome(service=self.service, options=self.options)

            try:
                self.driver.get(self.link)
                self.inParentUrl = True
            except Exception as e:
                raise RuntimeError(f"Failed to navigate to {self.link}: {e}")

        try:
            phone_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_selectors["phone"]))
            password_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.login_selectors["password"]))
            if not self.phone or not self.password:
                raise ValueError("Phone number and Password Required for login")
            phone_field.send_keys(self.phone)
            password_field.send_keys(self.password)
            login_button= WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "logIn")))
            login_button.click()

            self.account_balance = self.get_account_balance()

            if self.account_balance:
                logger.info("Login Sucesful")
            else:
                logger.error("Login failed")
        
        except TimeoutException:
            raise LoginError("Login fields not found")
        except Exception as e:
            raise LoginError(f"Login failed: {e}")

    def get_account_balance(self):

        if self.account_balance is None:
            self.account_balance = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "j_balance")))
            return self.account_balance
        else:
            return self.account_balance
        
    def swith_to_games(self):

        if self.inParentUrl:
            try:
                self.driver.get('https://www.sportybet.com/ng/games?source=TopRibbon')
                self.inParentUrl = False
                self.ingamesUrl = True
            except RuntimeError:
                print("Games section not found")
                self.inParentUrl = True

        else:
            print("Something went wrong. Site not visited")
    
    
    def close(self):
        if self.driver:
            self.driver.quit()
            self.driver = None