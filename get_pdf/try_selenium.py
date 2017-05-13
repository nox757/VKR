from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import PyPDF2
import pdfminer
import codecs


def tohtml():
    driver = webdriver.Firefox()
    driver.get("http://elibrary.ru/defaultx.asp")
    user_name = driver.find_element_by_id("login")
    user_name.send_keys("nox757")
    password = driver.find_element_by_id("password")
    password.send_keys("7a7n7d7")
    driver.find_element_by_class_name('butred').click()
    time.sleep(5)

    #time.sleep(15)
    # try:
    #     WebDriverWait(driver, 10).until(EC.title_contains("confirm"))
    #     print(driver.title)
    # finally:
    #     print False
    a = ""
    input(a)
    driver_new = driver.get('http://elibrary.ru/full_text.asp?id=19027757')
    input(a)
    driver.close()



a = ""
input(a)
tohtml()
