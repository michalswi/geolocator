import time
import sys

from selenium import webdriver

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# use english by default
URL="https://www.google.com/maps?hl=en-US"
TIMEBREAK=15

def timer(timebreak):
    while timebreak > 0:
        print(f"{timebreak:2d}", end="\r", flush=True)
        timebreak -= 1
        time.sleep(1)
    print("BUUM!")

def validate(data):
    if len(data) == 2:
        if " " in data[1]:
            return ",".join(data[1].split())
        else:
            return data[1]
    else:
        return ",".join([data[1],data[2]])

def geoLocation(geoloc):
    # [optional] 'en-US' in URL is enough
    # options = Options()
    # options.set_preference("intl.accept_languages", "en-US, en")  # Preferred languages
    # options.set_preference("intl.locale.requested", "en-US")  # Locale override
    # options.set_preference("general.useragent.locale", "en-US")  # User agent locale
    # driver = webdriver.Firefox(options=options)

    driver = webdriver.Firefox()
    driver.get(URL)
    
    # ACCEPT GOOGLE AGREEMENT
    # elem = driver.find_element("xpath","//button[contains(@class, 'VfPpkd-RLmnJb')]")
    # elem.send_keys(Keys.RETURN)
    elem = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='VfPpkd-vQzf8d' and text()='Reject all']"))
    )
    elem.click()

    # wait until page (URL) is loaded
    time.sleep(5)
    elem = driver.find_element("id","searchboxinput")
    elem.send_keys(geoloc)
    elem.send_keys(Keys.RETURN)
    print("Webriver is going to be closed after: %d [seconds]" %TIMEBREAK)
    timer(TIMEBREAK)
    driver.quit()

if __name__ == "__main__":
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print(f"Missing or wrong parameters given.\
            \nFormat: {sys.argv[0]} '<latitude>,<longitude>' \
            \nExample: {sys.argv[0]} '28.475492 -80.558464' \
            \nFormat: {sys.argv[0]} <latitude> <longitude> \
            \nExample: {sys.argv[0]} 28.475492 -80.558464")
    else:
        geoloc = validate(sys.argv)
        print(f"Geolocation to be checked: {geoloc}")
        geoLocation(geoloc)
