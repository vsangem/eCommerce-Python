import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def test_Add_Product_to_cart():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click 'Products' button
    driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()

    # 5. Hover over first product and click 'Add to cart'
    actions = ActionChains(driver)
    first_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[0]
    actions.move_to_element(first_product).perform()
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[0].click()

    # 6. Click 'Continue Shopping' button
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(3) button').click()

    # 7. Hover over second product and click 'Add to cart'
    second_product = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')[1]
    actions.move_to_element(second_product).perform()
    driver.find_elements(By.CSS_SELECTOR, '.product-overlay div a')[1].click()
    time.sleep(2)

    # 8. Click 'View Cart' button
    driver.find_element(By.CSS_SELECTOR, '.modal-content div:nth-child(2) a ').click()

    # 9. Verify both products are added to Cart
    added_products = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr')
    number_of_products_add = len(added_products)
    print('Number of Items Added in the Cart is: ', number_of_products_add)

    # 10. Verify their prices, quantity and total price
    product_price = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(3) p')
    first_product_price = product_price[0].text.strip()
    assert first_product_price.__contains__('500'),f'Expected price 500, but got {first_product_price}'
    second_product_price = product_price[1].text.strip()
    assert second_product_price.__contains__('400'), f'Expected price 400, but got {second_product_price}'
    product_quantity = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(4) button')
    first_product_quantity = product_quantity[0].text.strip()
    assert first_product_quantity == '1'
    second_product_quantity = product_quantity[1].text.strip()
    assert second_product_quantity == '1'
    total_price = driver.find_elements(By.CSS_SELECTOR, '.table.table-condensed tbody tr td:nth-child(5) p')
    first_product_total_price = total_price[0].text.strip()
    assert first_product_total_price.__contains__('500'), f'Expected price 500, but got {first_product_total_price}'
    second_product_total_price = total_price[1].text.strip()
    assert second_product_total_price.__contains__('400'), f'Expected price 500, but got {second_product_total_price}'
    driver.close()