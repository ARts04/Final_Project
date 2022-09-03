import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_change_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[3]/a").click() # change pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/input").send_keys("admin123") # current pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Admin12345?") # pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Admin12345?") # confirm pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() # save
        time.sleep(3)
    
    def test_a_failed_change_pass(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") # buka situs
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin") # isi email
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click() # klik tombol sign in
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/span").click()
        time.sleep(2)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[3]/a").click() # change pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/input").send_keys("admin123") # current pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input").send_keys("Admin12373#") # pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input").send_keys("Admin12345?") # confirm pass
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]").click() # save
        time.sleep(3)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()