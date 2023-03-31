from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Set up the webdriver (make sure you have the appropriate webdriver executable in your PATH)
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to Amazon's homepage
driver.get("https://www.amazon.ca")

# Find the search bar and enter a search query
search_bar = driver.find_element("id","twotabsearchtextbox")
search_bar.send_keys("bed")
search_bar.send_keys(Keys.RETURN)
time.sleep(2)
assert "bed" in driver.title

# Find the first search result and click on it
first_result = driver.find_element("xpath","//div[@class='s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_3']//span[@class='a-size-base-plus a-color-base a-text-normal']")
first_result.click()
time.sleep(2)
#assert "bed" in driver.title

add_to_cart_button = driver.find_element("id","add-to-cart-button")
add_to_cart_button.click()
time.sleep(2)

driver.back()
buy_now_button = driver.find_element("id","buy-now-button")
buy_now_button.click()
time.sleep(3)

driver.back()



best_sellers_button = driver.find_element("xpath","//div[@id='nav-subnav']/a[1]/span[@class='nav-a-content']")
best_sellers_button.click()
time.sleep(2)


# Close the browser
driver.quit()