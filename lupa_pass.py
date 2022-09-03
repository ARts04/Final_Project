import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_lupapass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p").click() # klik lupa pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/form/div[1]/div/div[2]/input").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]").click() # klik tombol reset
        time.sleep(5)
        

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()