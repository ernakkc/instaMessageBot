import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.params import SoftwareName, OperatingSystem
from random_user_agent.user_agent import UserAgent

from utils.targetData import isTargetDataExist, getTargetData, setTargetData

class Browser:
    def __init__(self, proxy, accountID, username, password, targetUsername):
        self.targetUsername = targetUsername
        self.driver = None
        self.wait = 20
        self.proxy = proxy
        self.accountID = accountID
        self.username = username
        self.password = password
        
        self.baseUrl = "https://www.instagram.com/"
        self.loginUrl = "https://www.instagram.com/accounts/login/"
        self.profileUrl = "https://www.instagram.com/{}/".format(self.targetUsername)
        self.followersUrl = "https://www.instagram.com/{}/followers/".format(self.targetUsername)

    def start(self):
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value]
        user_agent_rotator = UserAgent(software_name=software_names, operating_systems=operating_systems,limit=100)
        user_agent = user_agent_rotator.get_random_user_agent()

        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-infobars")
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--disable-web-security")
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_experimental_option('excludeSwitches', ['disable-popup-blocking'])
        self.options.add_argument(f"user-agent={user_agent}")
        self.options.add_argument("--user-data-dir={}".format(os.path.join(os.getcwd(), "webDataFolder", str(self.accountID))))
        if self.proxy: self.options.add_argument("--proxy-server={}".format(self.proxy))
        self.driver = webdriver.Chrome(options=self.options, service=Service("chromedriver.exe"))
        
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.driver.get(self.baseUrl)
        self.driver.implicitly_wait(self.wait)
        self.wait = WebDriverWait(self.driver, self.wait)
        
        cookies_file_path = os.path.join(os.getcwd(), "cookies", str(self.accountID) + ".txt")
        if os.path.exists(cookies_file_path):
            with open(cookies_file_path, "r") as file:
                cookies = file.read().splitlines()
                for cookie in cookies:
                    name, value = cookie.split("=", 1)
                    self.driver.add_cookie({"name": name, "value": value})
            self.driver.get(self.baseUrl)
        else:
            self.login()
            
    def quit(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.wait = None
            
    def save_cookies(self):
        cookies = self.driver.get_cookies()
        cookies_file_path = os.path.join(os.getcwd(), "cookies", str(self.accountID) + ".txt")
        with open(cookies_file_path, "w") as file:
            for cookie in cookies:
                file.write(f"{cookie['name']}={cookie['value']}\n")
            
    def login(self):
        if self.driver:
            self.driver.get(self.loginUrl)
            try:
                self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
                username_input = self.driver.find_element(By.NAME, "username")  
                password_input = self.driver.find_element(By.NAME, "password")
                username_input.clear()
                username_input.send_keys(self.username)
                password_input.clear()
                password_input.send_keys(self.password)
                password_input.send_keys(Keys.RETURN)
            except:
                pass
            try:
                self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Save Info')]")))
                save_info_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Save Info')]")))
                save_info_button.click()
            except:
                pass
            try:
                not_now_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Not Now')]")))
                not_now_button.click()
            except:
                pass
            self.save_cookies()
            self.driver.get(self.baseUrl)
            
    def isPrivateAccount(self):
        try:
            self.driver.get(self.profileUrl)
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(.,'This account is private')]")))
            data = getTargetData(self.targetUsername)
            if not isTargetDataExist(self.targetUsername):
                setTargetData(self.targetUsername, {"isPrivate": True})
            else:
                data["isPrivate"] = True
                setTargetData(self.targetUsername, data)
            return True
        except:
            data = getTargetData(self.targetUsername)
            if not isTargetDataExist(self.targetUsername):
                setTargetData(self.targetUsername, {"isPrivate": False, "requested": False})
            else:
                data["isPrivate"] = False
                data["requested"] = False
                setTargetData(self.targetUsername, data)
            return False
    
    def sendRequest(self):
        try:
            self.driver.get(self.profileUrl)
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//button/div/div")))
            follow_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button/div/div")))
            follow_button.click()
            
            data = getTargetData(self.targetUsername)
            if not isTargetDataExist(self.targetUsername):
                setTargetData(self.targetUsername, {"isPrivate": True})
                setTargetData(self.targetUsername, {"requested": True})
            else:
                data["isPrivate"] = True
                data["requested"] = True    
                setTargetData(self.targetUsername, data)
        except:
            data = getTargetData(self.targetUsername)
            if not isTargetDataExist(self.targetUsername):
                setTargetData(self.targetUsername, {"isPrivate": True})
            else:
                data["isPrivate"] = True
                setTargetData(self.targetUsername, data)
                
    def getFollowers(self):
        pass
                
    def restart(self):
        self.quit()
        self.start()


     