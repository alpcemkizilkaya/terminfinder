import os
import time

import winsound
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

if __name__ == '__main__':
    counter = 0
    test = False
    while not test:
        #os.chdir("C:\\Program Files\\NordVPN")
        #proc = subprocess.Popen('nordvpn -c', stdin=subprocess.PIPE, stdout=subprocess.PIPE,shell=True)
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        driver = webdriver.Chrome(options=options, executable_path='C:\\Users\\kizil\\PycharmProjects\\chromedriver.exe')
        try:
            driver.get('https://otv.verwalt-berlin.de/ams/TerminBuchen')
            time.sleep(2)
            book_link = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '/html/body/div[2]/div[2]/div[4]/form/div/div/div/div/div/div/div/div/div/div[1]/div[1]/div[2]/a')))
            book_link.click()
            time.sleep(2)
            allow_check = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="xi-cb-1"]')))
            allow_check.click()
            go_to_params_page = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="applicationForm:managedForm:proceed"]')))
            go_to_params_page.click()
            time.sleep(10)
            select_nationality = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="xi-sel-400"]')))
            Select(select_nationality).select_by_value('163')
            time.sleep(1)
            select_persons = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                                '//*[@id="xi-sel-422"]')))
            Select(select_persons).select_by_value('2')
            time.sleep(1)
            confirm_family_in_berlin = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                            '//*[@id="xi-sel-427"]')))
            Select(confirm_family_in_berlin).select_by_value('1')
            time.sleep(1)
            family_nationality = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                                            '//*[@id="xi-sel-428"]')))
            Select(family_nationality).select_by_value('163-0')
            time.sleep(1)


            apply_residence_title = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                                        '/html/body/div[2]/div[2]/div[4]/div[2]/form/div[2]/div/div[2]/div[8]/div[2]/div[2]/div[1]/fieldset/div[8]/div[1]/div[1]/div[1]/div[1]/label/p')))
            apply_residence_title.click()

            economic_act = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                               '/html/body/div[2]/div[2]/div[4]/div[2]/form/div[2]/div/div[2]/div[8]/div[2]/div[2]/div[1]/fieldset/div[8]/div[1]/div[1]/div[1]/div[6]/div/div[1]/label')))
            economic_act.click()

            blue_card = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="SERVICEWAHL_DE163-0-1-3-305244"]')))
            blue_card.click()
            submit_button = WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[@id="applicationForm:managedForm:proceed"]')))

            submit_button.click()

            time.sleep(10)
            free_time = driver.find_elements(By.CLASS_NAME,
                                             value='errorMessage')
            if len(free_time) == 0:
                free_time[0].click()
                test = True
                winsound.Beep(1000, 20000)
                time.sleep(60)
                print("XXXXXXXXX_DATA_XXXXXXXXX")

        except Exception as e:
            print(e)
        counter = counter + 1
        print(f'try count: {counter}')
        driver.quit()
