import webbrowser
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from threading import Timer
import pickle


def save_cookie(driver):
    pickle.dump(driver.get_cookies(), open("cookies/cookies.pkl","wb"))

def load_cookie(driver):
    cookies = pickle.load(open("cookies/cookies.pkl", "rb"))
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()

driver = webdriver.Chrome("C:\\Users\Asus\Desktop\selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(150)

try:
    # ---login---
    # ---------------login button ----------------------
    try:
        # load_cookie(driver)
        driver.get('https://www.ea.com/ea-sports-fc/ultimate-team/web-app/')
        login_b = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Login"]/div/div/button[1]'))
        )
        # login_b.click()
        cookies = pickle.load(open("cookies/cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
        driver.find_element_by_xpath('/html/body/main/section/nav/button[3]')
        transfers_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/nav/button[3]'))
        )

        
    except Exception as ex :
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)

    # ---------------login form ---------------------
    # try:
    #     driver.find_element_by_id("email").send_keys("yazeinal@gmail.com")
    #     driver.find_element_by_id("password").send_keys("Y@zd@n2014")
    #     driver.find_element_by_id("logInBtn").click()
    # except:
    #     pass

    # ---------------verification--------------------
    # try:
    #     send_code = driver.find_element_by_id("btnSendCode")
    #     send_code.click()
    # except:
    #     pass


    # ---step in---
    # -------------transfer button in nav -------------------
    def step_in():
        driver.find_element_by_xpath('/html/body/main/section/nav/button[3]')
        transfers_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/nav/button[3]'))
        )
        # save_cookie(driver)
        transfers_button.click()

        # ----------- transfer market ------------------
        transfer_market = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div/div[2]'))
        )
        time.sleep(5)
        transfer_market.click()

        search = driver.find_element_by_xpath(
            '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]')
        search.click()
        # quality = driver.find_element_by_xpath(
        #     '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]')
        # quality.click()
        # driver.find_element_by_xpath(
        #     '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[2]/div/ul/li[4]').click()
        #
        # rarity = driver.find_element_by_xpath(
        #     '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[3]')
        # rarity.click()
        # driver.find_element_by_xpath(
        #     "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[3]/div/ul/li[3]").click()
        #
        # league = driver.find_element_by_xpath(
        #     "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[7]")
        # league.click()
        # driver.find_element_by_xpath(
        #     "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[7]/div/ul/li[6]").click()

        search_input = driver.find_element_by_xpath("/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[1]/div[1]/div/div[1]/input")
        search_input.send_keys("")

        max_buy_now = driver.find_element_by_xpath(
            '/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[6]/div[2]/input')
        max_buy_now.send_keys('0')
        max_buy_now.send_keys('92500')


    step_in()

    driver.implicitly_wait(1)

    toggle_bool = 1


    def sniper():
        global toggle_bool
        # more efficient way
        if toggle_bool:
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[2]").click()
            toggle_bool = False
        else:
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/button[1]").click()
            toggle_bool = True
        search_button = driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
        search_button.click()

        try:

            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]")
            buy_now_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH,
                                            "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/button[2]"))
            )
            buy_now_button.click()

            accept_button = driver.find_element_by_xpath("/html/body/div[4]/section/div/div/button[1]")
            accept_button.click()

            back_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/section/div[1]/button[1]'))
            )
            back_button.click()

        except NoSuchElementException or StaleElementReferenceException:
            back_button = driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]')
            back_button.click()

        except:
            step_in()

        sniper()
        # t = Timer(0.01, sniper)
        # t.start()


    # sniper()


finally:
    pass
    # driver.close()
