from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import html2text


def render_html(url: str):
    h = html2text.HTML2Text()
    browser = webdriver.Firefox(executable_path='driver/geckodriver')
    browser.get(url)
    time.sleep(10)
    page_src = browser.page_source
    browser.quit()

    return h.handle(page_src)
