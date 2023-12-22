from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Setup WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to the website
driver.get("https://www.pragmaticplay.com/en/games/gates-of-olympus/?gamelang=en&cur=USD")

# Optionally locate a reference element
# reference_element = driver.find_element_by_id("referenceElementId")

# Create ActionChain and move to specific position then click
actions = ActionChains(driver)
actions.move_by_offset(10, 20)  # Specify x and y offset values
actions.click()
actions.perform()

# Close the browser
driver.quit()