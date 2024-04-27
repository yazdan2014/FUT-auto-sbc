import webbrowser
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from threading import Timer



driver = webdriver.Chrome("C:\\Users\Asus\Desktop\selenium\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(150)


# def save_cookie(driver, path):
#     with open(path, 'wb') as filehandler:
#         pickle.dump(driver.get_cookies(), filehandler)

# def load_cookie(driver, path):
#      with open(path, 'rb') as cookiesfile:
#          cookies = pickle.load(cookiesfile)
#          for cookie in cookies:
#              driver.add_cookie(cookie)

try:
    # ---login---
    # ---------------login button ----------------------
    try:
        driver.get('https://www.ea.com/ea-sports-fc/ultimate-team/web-app/')
        login_b = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Login"]/div/div/button[1]'))
        )
        login_b.click()
    except:
        pass

    # ---------------login form ---------------------
    try:
        driver.find_element_by_id("email").send_keys("yazeinal@gmail.com")
        driver.find_element_by_id("password").send_keys("Y@zd@n2014")
        driver.find_element_by_id("logInBtn").click()
    except:
        pass

    # ---------------verification--------------------
    try:
        send_code = driver.find_element_by_id("btnSendCode")
        send_code.click()
    except:
        pass


    # ---step in---
    # -------------transfer button in nav -------------------
    def step_in():
        driver.find_element_by_xpath('/html/body/main/section/nav/button[6]')
        sbc_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/main/section/nav/button[6]'))
        )
        sbc_button.click()

        # ----------- sbc menu  ------------------
        favorites_tab = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[1]/div/button[2]'))
        )
        time.sleep(3)
        favorites_tab.click()


        sbc = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/main/section/section/div[2]/div/div[2]/div[2]/div'))
        )
        sbc.click()

    step_in()
    driver.implicitly_wait(1)


    def auto_sbc():

        try:
            squad_builder = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div/section/div/div[2]/button[2]"))
            )
            squad_builder.click()
            
            # quality = WebDriverWait(driver, 15).until(
            #     EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]/div/div"))
            # )
            # quality.click()
            # driver.find_element_by_xpath(
            # "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[3]/div/ul/li[4]").click()

            rarity = driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[4]/div/div/button")
            rarity.click()
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[4]/div/ul/li[2]").click()


            sort_by = driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[1]/div/div[2]/div/span")
            sort_by.click()
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[1]/div/div[2]/div/ul/li[4]").click()
            
            
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[3]/button[2]").click()
            
            # add some sleep time to make sure builder is done building
            time.sleep(3)

            rb_common = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/div[2]/div[1]/div[2]"))
            )
            rb_common.click()

            swap_player = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[2]/div[2]/button[3]"))
            )
            swap_player.click()

            # Post Removal
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[5]/div/div/button").click()

            sort_by_2 = driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[1]/div[2]")
            sort_by_2.click()
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[1]/div[2]/div/ul/li[4]").click()

            quality_2 = driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]")
            quality_2.click()
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[3]/div/ul/li[4]").click()

            rarity_2 = driver.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]")
            rarity_2.click()
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[2]/div[2]/div[4]/div/ul/li[3]").click()

            # Search button
            driver.find_element_by_xpath(
                "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div/div/div[3]/button[2]").click()

            swap_player_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/section/div[2]/div/div[3]/ul/li[1]/button"))
            )
            swap_player_button.click()

            submit_button = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/main/section/section/div[2]/div/div/div/div[2]/button[2]"))
            )
            submit_button.click()

            claim_rewards = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/footer/button"))
            )
            claim_rewards.click()

            claim_rewards2 = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/footer/button"))
            )
            claim_rewards2.click()
        # except NoSuchElementException or StaleElementReferenceException:
        #     back_button = driver.find_element_by_xpath('/html/body/main/section/section/div[1]/button[1]')
        #     back_button.click()

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print (message)
            # step_in()
            # auto_sbc()

        # auto_sbc()
        # t = Timer(0.01, sniper)
        # t.start()

    auto_sbc()
    # sniper()


finally:
    pass
    # driver.close()
