from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace these variables with your actual lpulive login credentials
username = "12108147"
password = "Study@12345"

# Path to your webdriver, in this case, I'm using Chrome
driver_path = "https://lpulive.lpu.in/login"

# URL of the lpulive login page
login_url = "https://lpulive.lpu.in/login"

# Initialize Chrome WebDriver
driver = webdriver.Chrome(driver_path)

# Open the lpulive login page
driver.get(login_url)

# Find the username and password fields and input the login credentials
username_field = driver.find_element_by_id("txtUName")
password_field = driver.find_element_by_id("txtPass")

username_field.send_keys(username)
password_field.send_keys(password)

# Click the login button
login_button = driver.find_element_by_id("btnLogin")
login_button.click()

# Wait for the dashboard to load (adjust timeout as needed)
try:
    dashboard_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "dashboard"))
    )
    print("Login successful!")
except:
    print("Login failed.")

# Now you can perform actions on the dashboard or navigate to other pages as needed

# Remember to close the browser when done
# driver.quit()
