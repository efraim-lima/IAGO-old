#pip install selenium-wire
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options as ChromeOpt 
from time import sleep
import random, os, inspect;
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from seleniumwire import webdriver  # Import from seleniumwire  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def DriverLog(): 
	options = ChromeOpt()
	agentes = [ "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" ,
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63",
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:63.0) Gecko/20100101 Firefox/63.0",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36",
		"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
		];
	agente = agentes[random.randint(0, len(agentes) - 1)]
	#options.headless = True
	options.add_argument("user-agent=" + agente);
    #options.add_argument("--headless")
	options.add_argument(
        '--disable-gpu'
    )
	options.add_argument("--no-sandbox");
	options.add_argument("--mute-audio");
	global driver
	driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options,
        # seleniumwire_options=options
        )
	driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
	driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
	driver.execute_script(
		"window.scrollTo(0, window.scrollY + 5000)"
	)
	html = driver.find_element_by_tag_name('html')
	html.send_keys(Keys.END)

	# Go to the Google home page  
	driver.get('https://www.instagram.com/jadepicon')
 
	driver.find_element(
		By.XPATH,
		'//*[@id="react-root"]/section/main/div/div[4]/div[1]/div/button/div/div'
	).click()

	# Access and print requests via the `requests` attribute  
	for request in driver.requests:  
		if request.response:  
			print(  
				request.url,  
				request.response.status_code,  
				request.response.headers['Content-Type'])  

DriverLog()