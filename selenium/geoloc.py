import time
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


URL="https://www.google.com/maps"
TIMEBREAK=15

def timer(timebreak):
    while timebreak > 0:
        print("%d" %timebreak, end="\r")
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
    driver = webdriver.Firefox()
    driver.get(URL)
    # accept google agreement
    elem = driver.find_element("xpath","//button[contains(@class, 'VfPpkd-LgbsSe')]")
    elem.send_keys(Keys.RETURN)
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
