from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from passwords import a_username,a_password
import time
import speech_recognition as sr
c=webdriver.ChromeOptions()
c.add_argument('--incognito')
r=sr.Recognizer()
with sr.Microphone() as source:
    print('listening..')
    r.pause_threshold=0.8
    audio=r.listen(source)
    audio=r.recognize(audio)
order=audio
print(order)
time.sleep(3)
driver = webdriver.Chrome(executable_path=r"C:\Users\hp\OneDrive\Desktop\website\chromedriver.exe")
url = 'https://www.amazon.in/'
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="nav-signin-tooltip"]/a/span').click()
driver.maximize_window()
a=driver.find_element(By.ID,'ap_email')
a.send_keys(a_username)
driver.find_element(By.XPATH,'//*[@id="continue"]').click()
driver.find_element(By.ID,'ap_password').send_keys(a_password)
driver.find_element(By.XPATH,'//*[@id="signInSubmit"]').click()
driver.find_element(By.XPATH,'//*[@id="twotabsearchtextbox"]').send_keys(order)
driver.find_element(By.XPATH,'//*[@id="nav-search-submit-button"]').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="nav-hamburger-menu"]/i').click()
driver.find_element(By.XPATH,'//*[@id="hmenu-content"]/ul[1]/li[30]/a').click()