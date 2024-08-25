import random
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_verify_products_in_cart_after_login():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Click on 'Products' button
    driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()

    # 4. Verify user is navigated to ALL PRODUCTS page successfully
    assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()

    # 5. Enter product name in search input and click search button
    all_products = driver.find_elements(By.CSS_SELECTOR, '.single-products div.productinfo p')
    product_text = [driver.execute_script("return arguments[0].textContent;", product).strip() for product in all_products]
    random_product_text = random.choice(product_text)
    driver.find_element(By.CSS_SELECTOR, 'input#search_product').send_keys(random_product_text)
    driver.find_element(By.CSS_SELECTOR, 'button#submit_search').click()

    # 6. Verify 'SEARCHED PRODUCTS' is visible
    assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'Searched Products'.upper()

    # 7. Verify all the products related to search are visible
    time.sleep(1.5)
    searchedProduct = driver.find_element(By.CSS_SELECTOR, '.productinfo.text-center p')
    # searchedProduct.is_displayed()
    assert searchedProduct.text == random_product_text, f'random Product:{random_product_text},{searchedProduct}'

    # 8. Add those products to cart
    driver.execute_script('window.scrollBy(0, 500);')
    actions = ActionChains(driver)
    first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
    actions.move_to_element(first_product).perform()
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()
    time.sleep(1.5)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    # 9. Click 'Cart' button and verify that products are visible in cart
    driver.find_element(By.LINK_TEXT, 'Cart').click()
    added_products = driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(2) h4').text
    assert random_product_text in added_products

    # 10. Click 'Signup / Login' button and submit login details
    driver.find_element(By.LINK_TEXT, 'Signup / Login').click()
    driver.find_element(By.XPATH, '//input[@data-qa="login-email"]').send_keys('Tulika.singh_20240803222313@yahoo.com')
    driver.find_element(By.XPATH, '//input[@data-qa="login-password"]').send_keys('QA@123')
    driver.find_element(By.XPATH, '//button[@data-qa="login-button"]').click()

    # 11. Again, go to Cart page
    driver.find_element(By.LINK_TEXT, 'Cart').click()

    # 12. Verify that those products are visible in cart after login as well
    assert driver.find_element(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(2) h4').text == random_product_text
    driver.close()
