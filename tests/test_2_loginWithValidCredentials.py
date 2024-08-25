import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.test_1_RegisterUser import common_password

registered_emails = ['Joshua.Nguyenzwilliams@example.org', 'Ashley.Wilsondwalker@example.com',
                             'Austin.Campbellsonyathomas@hotmail.com', 'Jennifer.Collinsmillercharles@hotmail.com',
                             'Tulika.singh_20240803225822@yahoo.com']
random_registered_emails = random.choice(registered_emails)


def test_login_with_valid_credentials():

    # 1. Launch browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click on 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # 5. Verify 'Login to your account' is visible
    loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
    assert 'Login to your account' in loginUser

    # 6. Enter correct email address and password
    driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys(random_registered_emails)
    driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys(common_password)

    # 7. Click 'login' button
    driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
    time.sleep(2)

    # 8. Verify that 'Logged in as username' is visible
    user_name = 'Joshua'
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == user_name

    # # 9. Click 'Delete Account' button
    # driver.find_element(By.LINK_TEXT, 'Delete Account').click()
    #
    # # 10. Verify that 'ACCOUNT DELETED!' is visible
    # assert driver.find_element(By.CSS_SELECTOR, '.col-sm-9.col-sm-offset-1 h2').text == 'Account Deleted!'.upper()
    driver.close()
