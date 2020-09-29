from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


def chrome():
    driver = webdriver.Chrome('./linux_chromedriver')
    driver.get("https://google.com/ncr")

    driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)

    first_result = WebDriverWait(driver, 10).until(
    presence_of_element_located((By.CSS_SELECTOR, "h3"))
    )

    assert first_result.get_attribute("textContent") == "Cheese - Wikipedia"