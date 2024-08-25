import random
import time

from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from tests.test_1_RegisterUser import common_password


def test_login_before_checkout():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click 'Signup / Login' button
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()

    # 5. Fill email, password and click 'Login' button
    name_1 = 'Austin'
    driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Austin.Campbellsonyathomas@hotmail.com')
    driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys(common_password)
    driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()
    time.sleep(2)

    # 6. Verify 'Logged in as username' at top
    assert driver.find_element(By.CSS_SELECTOR, 'li a b').text == name_1

    # 7. Add products to cart
    actions = ActionChains(driver)

    first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')
    random_first_product = random.choice(first_product)
    actions.move_to_element(random_first_product).perform()
    random_first_product.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')
    random_second_product = random.choice(second_product)
    driver.execute_script('arguments[0].scrollIntoView(true);', random_second_product)
    actions.move_to_element(random_second_product).perform()
    random_second_product.find_element(By.CSS_SELECTOR, '.product-overlay div a').click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    # 8. Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 9. Verify that cart page is displayed
    assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'

    # 10. Click Proceed To Checkout
    driver.find_element(By.CSS_SELECTOR, '.col-sm-6 a').click()

    # 11. Verify Address Details and Review Your Order
    assert driver.find_element(By.CSS_SELECTOR, 'li.address_firstname.address_lastname').text.__contains__(name_1)
    review_your_order = driver.find_element(By.CSS_SELECTOR, '.cart_description h4 a')
    print('You\'re ordering: '+review_your_order.text)

    # 12. Enter description in comment text area and click 'Place Order'
    driver.find_element(By.CSS_SELECTOR, '.form-control').send_keys('Nothing to Add, Please Proceed!')
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.check_out').click()

    # 13. Enter payment details: Name on Card, Card Number, CVC, Expiration date
    fake = Faker()
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="name-on-card"]').send_keys(name_1)
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="card-number"]').send_keys(fake.credit_card_number())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="cvc"]').send_keys(fake.credit_card_security_code())
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-month"]').send_keys(str(random.randint(1,12)))
    driver.find_element(By.CSS_SELECTOR, 'input[data-qa="expiry-year"]').send_keys('1999')

    # 14. Click 'Pay and Confirm Order' button
    driver.execute_script("window.scrollBy(0,500);")
    driver.find_element(By.CSS_SELECTOR, 'button[data-qa="pay-button"]').click()

    # 15. Verify success message 'Your order has been placed successfully!'
    success_message = driver.find_element(By.CSS_SELECTOR, '.col-sm-9 p').text.strip()
    assert success_message == 'Congratulations! Your order has been confirmed!'
    driver.close()
