# importing webdriver from selenium
from selenium import webdriver
import time
import pywhatkit

# Here Chrome will be used
driver = webdriver.Firefox()


# URL of website
url = "https://web.whatsapp.com/"

# # Opening the website
driver.get(url)
# driver.execute_script("window.open('');")
# driver.switch_to.window(driver.window_handles[1])

# new_url = "https://www.instagram.com"
# driver.get(new_url)
pywhatkit.sendwhatmsg('+919633108610', 'test22', 19, 58)

time.sleep(25)
# Closes the current window
driver.close()
