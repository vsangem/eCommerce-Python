import random

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_verify_products_and_product_details():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Verify that home page is visible successfully
    homepage = driver.find_element(By.XPATH, '//h1').text
    assert 'Automation' in homepage and 'Exercise' in homepage, f'Text not found in header, got: {homepage}'

    # 4. Click on 'Products' button
    driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()

    # 5. Verify user is navigated to ALL PRODUCTS page successfully
    assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'All Products'.upper()

    # 6. The products list is visible
    products = driver.find_elements(By.CSS_SELECTOR, '.col-sm-4 div.product-image-wrapper')
    assert len(products) > 0, 'No products found on the page'
    random_product_index = random.randrange(0, len(products))
    print(f'Number of products visible: {len(products)}')

    # 7. Click on 'View Product' of first/any product
    driver.execute_script('arguments[0].scrollIntoView(true);', products[random_product_index])
    products[random_product_index].find_element(By.CSS_SELECTOR, 'div[class="choose"] ul li a').click()

    # 8. User is landed to product detail page
    driver.find_element(By.CSS_SELECTOR, '.newarrival').is_displayed()

    # 9. Verify that detail is visible: product name, category, price, availability, condition, brand
    product_name = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div h2')
    product_name.is_displayed()
    print('Product Name is: '+product_name.text)

    category = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p')
    category.is_displayed()
    print(category.text)

    price = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div span:nth-child(1)')
    price.is_displayed()
    print('Price is: '+price.text)

    availability = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p:nth-child(6)')
    availability.is_displayed()
    print(availability.text)

    condition = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p:nth-child(7)')
    condition.is_displayed()
    print(condition.text)

    brand = driver.find_element(By.CSS_SELECTOR, '.col-sm-7 div p:nth-child(8)')
    brand.is_displayed()
    print(brand.text)

    driver.close()