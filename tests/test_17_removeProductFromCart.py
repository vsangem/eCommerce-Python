import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_remove_products_from_cart():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Add products to cart
    actions = ActionChains(driver)
    driver.execute_script("window.scrollBy(0, 1000);")
    first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[4]
    actions.move_to_element(first_product).perform()
    time.sleep(1)
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[4].click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()
    second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[5]
    actions.move_to_element(second_product).perform()
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[5].click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    # 5. Click 'Cart' button
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 6. Verify that cart page is displayed
    assert driver.find_element(By.CSS_SELECTOR, '.breadcrumb li:nth-child(2)').text == 'Shopping Cart'

    # 7. Click 'X' button corresponding to particular product
    delete_buttons = driver.find_elements(By.CSS_SELECTOR, ".cart_quantity_delete")
    for button in delete_buttons:
        button.click()
        time.sleep(1)

    # 8. Verify that product is removed from the cart
    assert driver.find_element(By.CSS_SELECTOR, 'span#empty_cart p b').text.__contains__('Cart is empty!')
    driver.close()