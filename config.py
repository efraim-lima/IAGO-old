from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException


def webDriver():
    chrome_options = Options()
    chrome_options.add_argument(
        "-headless"
    )
    chrome_options.add_argument(
        '--disable-gpu'
    )
    global driver
    driver = webdriver.Chrome(
                ChromeDriverManager().install(),
                options = chrome_options
        )
    return driver
driver = webDriver()

def inChrome():
    try:
        driver.maximize_window() # For maximizing window
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.execute_script(
            "window.scrollTo(0, window.scrollY + 5000)"
        )
        # print (driver) #para ver qual o driver utilizado
        # print (content) #mostra o java script do site
        # executar um python main.py
        # exec. pip install chromedriver

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        driver.execute_script(
            "window.scrollTo(0, window.scrollY + 2000)"
        )
    except WebDriverException:
        print('page down')
