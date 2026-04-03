from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
password: Shreyas
driver.get("https://www.amazon.in/ap/signin")

wait = WebDriverWait(driver, 10)

# Enter email/mobile
email_field = wait.until(EC.visibility_of_element_located((By.ID, "ap_email")))
email_field.send_keys("your_email_or_mobile")

# Click Continue
driver.find_element(By.ID, "continue").click()

# Enter password
password_field = wait.until(EC.visibility_of_element_located((By.ID, "ap_password")))
password_field.send_keys("your_password")

# Click Sign In
driver.find_element(By.ID, "signInSubmit").click()

# Wait until homepage loads or account element appears
wait.until(EC.presence_of_element_located((By.ID, "nav-link-accountList")))

print("Login successful")

driver.quit()
