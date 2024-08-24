import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_product_quantity_in_cart():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click 'View Product' for any product on home page
    driver.execute_script('window.scrollBy(0, 500);')
    driver.find_element(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper div[class="choose"] ul li a').click()

    # 5. Verify product detail is opened
    driver.find_element(By.CSS_SELECTOR, '.newarrival').is_displayed()

    # 6. Increase quantity to 4
    quantity = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div input:nth-child(3)')
    quantity.clear()
    quantity.send_keys('4')

    # 7. Click 'Add to cart' button
    driver.find_element(By.CSS_SELECTOR, '.btn.btn-default.cart').click()

    # 8. Click 'View Cart' button
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) a').click()

    # 9. Verify that product is displayed in cart page with exact quantity
    assert driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(4) button').text.strip() == '4'
    driver.close()
