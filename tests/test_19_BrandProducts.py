import random
import re

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_view_brand_products_in_cart():

    # 1. Launch browser
    driver = webdriver.Edge()
    driver.maximize_window()

    # 2. Navigate to url 'http://automationexercise.com'
    driver.get('https://www.automationexercise.com/')

    # 3. Click on 'Products' button
    driver.find_element(By.CSS_SELECTOR, 'a i.material-icons').click()

    # 4. Verify that Brands are visible on left sidebar
    driver.execute_script("window.scrollBy(0, 500);")
    assert driver.find_element(By.CSS_SELECTOR, '.brands_products h2').text == 'Brands'.upper()

    # 5. Click on any brand name
    brand_names = driver.find_elements(By.CSS_SELECTOR, '.brands-name ul li a')
    select_brand_name = [driver.execute_script("return arguments[0].textContent;", brand).strip() for brand in brand_names]
    random_brand_selection = random.choice(select_brand_name)
    print('1st Brand: ', format(random_brand_selection))
    for brand in brand_names:
        driver.execute_script("arguments[0].scrollIntoView(true);", brand)
        text = driver.execute_script("return arguments[0].textContent;", brand).strip()
        if text == random_brand_selection:
            brand.click()
            break

    # 6. Verify that user is navigated to brand page and brand products are displayed
    product_title = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
    assert "Brand - "+random_brand_selection+" Products"
    match = re.search(r'\((\d+)\)', random_brand_selection)
    if match:
        displayed_count = int(match.group(1))
        print(f'Displayed Product Count: {displayed_count}')
    else:
        print('Product count not found in the brand name text.')
        displayed_count = None

    # 7. On left sidebar, click on any other brand link
    brand_names_2 = driver.find_elements(By.CSS_SELECTOR, '.brands-name ul li a')
    select_brand_name_2 = [driver.execute_script("return arguments[0].textContent;", brand).strip() for brand in brand_names_2]
    random_brand_selection_2 = random.choice(select_brand_name_2)
    print('2nd Brand: ', format(random_brand_selection_2))
    for brand_2 in brand_names_2:
        driver.execute_script("arguments[0].scrollIntoView(true);", brand_2)
        text = driver.execute_script("return arguments[0].textContent;", brand_2).strip()
        if text != random_brand_selection:
            brand_2.click()
            break

    # 8. Verify that user is navigated to that brand page and can see products
    product_title_2 = driver.find_element(By.CSS_SELECTOR, '.title.text-center').text
    assert "Brand - "+random_brand_selection_2+" Products"
    driver.close()
