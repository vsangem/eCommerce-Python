from selenium import webdriver
from selenium.webdriver.common.by import By


def test_search_a_product():
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

    # 6. Enter product name in search input and click search button
    searchProduct = 'Green Side Placket Detail T-Shirt'
    driver.find_element(By.CSS_SELECTOR, 'input#search_product').send_keys(searchProduct)
    driver.find_element(By.CSS_SELECTOR, 'button#submit_search').click()

    # 7. Verify 'SEARCHED PRODUCTS' is visible
    assert driver.find_element(By.CSS_SELECTOR, 'h2.title.text-center').text == 'Searched Products'.upper()

    # 8. Verify all the products related to search are visible
    searchedProduct = driver.find_element(By.CSS_SELECTOR, '.productinfo.text-center p')
    searchedProduct.is_displayed()
    assert searchedProduct.text.__contains__('Green Side Placket Detail')
    driver.close()
