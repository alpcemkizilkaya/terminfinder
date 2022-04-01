import datetime
import os
import subprocess
import time

from selenium import webdriver

from selenium.common.exceptions import WebDriverException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sound_path = os.path.join(dir_path, 'alarm.mp3')
    counter = 0
    test = False
    #driver = webdriver.Chrome(
     #   '/Users/alpcemkizilkaya/Downloads/chromedriver')  # Optional argument, if not specified will search path.
    driver = webdriver.Firefox(executable_path='/Users/alpcemkizilkaya/Downloads/geckodriver')
    while not test:

        driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen')
        time.sleep(10)  # Let the user actually see something!
        book_link = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[5]/form/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a')))
        book_link.click()

        allow_check = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[4]/div[1]/div[4]/input')))
        allow_check.click()
        go_to_params_page = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[5]/button')))
        go_to_params_page.click()
        time.sleep(60)
        select_nationality = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[2]/select')))
        Select(select_nationality).select_by_value('163')
        time.sleep(1)
        select_persons = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[3]/div[1]/div[1]/select')))
        Select(select_persons).select_by_value('3')
        time.sleep(1)
        confirm_family_in_berlin = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                        '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[4]/select')))
        Select(confirm_family_in_berlin).select_by_value('1')
        time.sleep(1)
        family_nationality = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                                        '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[5]/select')))
        Select(family_nationality).select_by_value('163-0')
        time.sleep(1)
        apply_residence_title = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                                    '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[9]/div[1]/div[1]/div[1]/div[1]/label/p')))
        apply_residence_title.click()

        economic_act = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[9]/div[1]/div[1]/div[1]/div[6]/div/div[3]/label/p')))
        economic_act.click()

        blue_card = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH,
                                        '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[2]/div/div[2]/div[8]/div[1]/div[2]/div[1]/fieldset/div[9]/div[1]/div[1]/div[1]/div[6]/div/div[4]/div/div[11]/input')))
        blue_card.click()
        submit_button = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[2]/form/div[5]/button')))

        submit_button.click()

        try:
            time.sleep(45)
            WebDriverWait(driver, 60).until(
                EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[4]/ul/li')))
            counter = counter + 1
            print("failed count :", counter,"time :",str(datetime.datetime.now()))

        except (NoSuchElementException,TimeoutException) as e:
            print(str(e))
            print("success on count :", counter,str(datetime.datetime.now()))
            test = True
            print(driver.current_url)
            subprocess.Popen(["afplay", sound_path])
            time.sleep(300)
    driver.quit()
