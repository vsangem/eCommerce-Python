from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.test_1_RegisterUser import random_email


def test_verify_subscription_in_cart_page():
    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 5. Scroll down to footer
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 5. Verify text 'SUBSCRIPTION'
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-3.col-sm-offset-1 h2').text == 'Subscription'.upper()

    # 6. Enter email address in input and click arrow button
    driver.find_element(By.ID, 'susbscribe_email').send_keys(random_email)
    driver.find_element(By.CSS_SELECTOR, '#subscribe').click()

    # 7. Verify success message 'You have been successfully subscribed!' is visible
    assert driver.find_element(By.CSS_SELECTOR, '.alert-success.alert').text == 'You have been successfully subscribed!'
    driver.close()