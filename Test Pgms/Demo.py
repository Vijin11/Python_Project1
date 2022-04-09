from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

    // Intalising the webdriver
    
    ser = Service("E:\CDRIVER\chromedriver.exe")
    driver = webdriver.Chrome(service=ser)


	// navigating to url

    driver.get("http://www.google.com")

    Element = driver.find_element(By.XPATH, '//input[@class="gLFyf gsfi"]');


