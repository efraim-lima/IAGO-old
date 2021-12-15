from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from time import sleep


def webDriver():
    options = Options()
    #options.headless = True
    options.add_argument("--headless")
    options.add_argument(
        'disable-gpu'
    )
    global driver

    driver = webdriver.Firefox(
        executable_path=GeckoDriverManager().install(),
        options=options
        )
    return driver

def inChrome():
    try:
        driver.maximize_window() # For maximizing window
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.execute_script(
            "window.scrollTo(0, window.scrollY + 5000)"
        )
        
        # exec. pip install chromedriver

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.execute_script(
            "window.scrollTo(0, window.scrollY + 2000)"
        )
    except WebDriverException:
        print('page down')

def pauseVideo():
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('\ue00d').key_up(Keys.CONTROL).perform()
    sleep(3)
    action.key_down(Keys.CONTROL).send_keys('K').key_up(Keys.CONTROL).perform()
    
def quit():
    quit = driver.quit()
    return quit
