import os
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By

from tests.test_1_RegisterUser import random_email

fake = Faker()


def test_verify_contact_us_form():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click on 'Contact Us' button
    driver.find_element(By.LINK_TEXT, 'Contact us').click()

    # 5. Verify 'GET IN TOUCH' is visible
    assert driver.find_element(By.CSS_SELECTOR, '.col-sm-8 div h2').text == 'Get In Touch'.upper()

    # 6. Enter name, email, subject and message
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name"]').send_keys(fake.name())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="email"]').send_keys(random_email)
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="subject"]').send_keys(fake.sentence(nb_words=15))
    driver.find_element(By.CSS_SELECTOR, 'textarea[data-qa="message"]').send_keys(fake.paragraph(nb_sentences=5))
    
    # 7. Upload file
    filepath = os.path.abspath('C:\\Users\\VENKAT JAYASURYA\\Downloads\\orders.csv')
    driver.find_element(By.NAME, 'upload_file').send_keys(filepath)
    driver.execute_script('window.scrollBy(0, 1000);')

    # 8. Click 'Submit' button
    driver.find_element(By.NAME, 'submit').click()

    # 9. Click OK button
    alert = driver.switch_to.alert
    alert.accept()

    # 10. Verify success message 'Success! Your details have been submitted successfully.' is visible
    assert driver.find_element(By.CSS_SELECTOR, '.status.alert.alert-success').text == \
           'Success! Your details have been submitted successfully.'

    # 11. Click 'Home' button and verify that landed to home page successfully
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-success').click()
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'
    driver.close()
