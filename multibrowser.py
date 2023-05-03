import time
import requests
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://atg.party/article")
driver.maximize_window()
r = requests.get("https://atg.party/article")
print(r.status_code)
print("Title:",driver.title)
driver.find_element(By.XPATH,'/html/body/nav/div/div/div/div[2]/div/button[2]').click()
time.sleep(5)
#login details
user=driver.find_element(By.XPATH,'//*[@id="email_landing"]')
password=driver.find_element(By.XPATH,'//*[@id="password_landing"]')
user.clear()
user.send_keys("wiz_saurabh@rediffmail.com")
password.clear()
password.send_keys("Pass@123")
driver.find_element(By.XPATH,'//*[@id="frm_landing_page_user_login"]/div[3]/button').click()
time.sleep(5)
#post an article
title=driver.find_element(By.XPATH,'//*[@id="title"]')
desc = driver.find_element(By.XPATH,'//*[@id="description"]/div/div[1]/div/div/div')
title.clear()
title.send_keys("task-3 complete")
desc.clear()
desc.send_keys("the task assigned has been completed")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="cover_image"]').send_keys("C:/Users/sanjeev/Downloads/th.jpg")
time.sleep(10)
#submitting article
driver.find_element(By.XPATH,'//*[@id="hpost_btn"]').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="closeModal"]/img').click()
get_url = driver.current_url
print(get_url)
time.sleep(10)
driver.close()