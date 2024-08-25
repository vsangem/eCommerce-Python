import random

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.test_2_loginWithValidCredentials import random_registered_emails

fake = Faker()


def test_register_with_already_existing_user():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click on 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # 5. Verify 'New User Signup!' is visible
    newUserSignup = driver.find_element(By.CSS_SELECTOR,'.signup-form h2').text
    assert 'New User Signup!' in newUserSignup

    # 6. Enter name and already registered email address
    driver.find_element(By.XPATH, '//input[@data-qa="signup-name"]').send_keys(fake.name())
    driver.find_element(By.XPATH, '//input[@data-qa="signup-email"]').send_keys(random_registered_emails)

    # 7. Click 'Signup' button
    driver.find_element(By.XPATH, '//button[@data-qa="signup-button"]').click()

    # 8. Verify error 'Email Address already exist!' is visible
    assert driver.find_element(By.CSS_SELECTOR, '[action="/signup"] p').text == 'Email Address already exist!'
    driver.close()