from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.test_1_RegisterUser import common_password


def test_logout_of_application():

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

    # 5. Verify 'Login to your account' is visible
    loginUser = driver.find_element(By.CSS_SELECTOR,'.login-form h2').text
    assert 'Login to your account' in loginUser

    # 6. Enter correct email address and password
    driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Joshua.Nguyenzwilliams@example.org')
    driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys(common_password)

    # 7. Click 'login' button
    driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()

    # 8. Verify that 'Logged in as username' is visible
    name = 'Joshua'
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text.__contains__(name)

    # 9. Click 'Logout' button
    driver.find_element(By.LINK_TEXT, 'Logout').click()

    # 10. Verify that user is navigated to login page
    assert 'Login to your account' in loginUser
    driver.close()