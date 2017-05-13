import os
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

#create list of id in resource e-library from early got page with finding results
def create_list():
    path_f = 'k:\Andrew\\vkr\elib\\90 метрлогия\\90.htm'
    f = open(path_f, 'rb')
    soup = BeautifulSoup(f, "lxml")
    soupa = soup.find_all('a', href=re.compile('selid='))
    res = []
    print(soupa)
    p = re.compile('selid=\d+')
    p1 = re.compile('\d+')
    for ref in soupa:
        el = p1.search(p.search(ref['href']).group()).group()
        res.append(el)
    f.close()
    return res

#loading article
def load_with_firefox(list_id):
    driver = webdriver.Firefox()
    driver.get("http://elibrary.ru/defaultx.asp")
    user_name = driver.find_element_by_id("login")
    user_name.send_keys("nox757")
    password = driver.find_element_by_id("password")
    password.send_keys("7a7n7d7")
    driver.find_element_by_class_name('butred').click()
    time.sleep(5)
    a = ""
    input(a)
   #driver.manage().timeouts().pageLoadTimeout(10, TimeUnit.SECONDS);
    driver.set_page_load_timeout(3)
    for id_el in list_id:
        delay = 2  # seconds
        try:
            driver.get('http://elibrary.ru/full_text.asp?id=' + id_el)
        except:
            print( "Loading took too much time!")
            pass


    input(a)
    driver.close()

#checking correct txt after pdf-converting: ex. wrong empty and ect.
def check_correct_txt():
    path_f = ''
    list_f = os.listdir(path_f)
    # for el in list_f:
    #     f.open('')

result = create_list()
print(len(result))
load_with_firefox(list_id=result)
print("Finished")

















