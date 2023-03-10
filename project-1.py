import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Successful Employee Login to OranageHRM portal
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
uname = driver.find_element(By.XPATH,"//input[@name='username']")
uname.send_keys("Admin")
passwd = driver.find_element(By.XPATH, "//input[@name='password']")
passwd.send_keys("admin123")
time.sleep(5)
# Click log in button to login the website.
login = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
login.click()
time.sleep(5)
print("The user is logged in successfully")

# Invalid Employee login to OrangeHRM portal
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
uname = driver.find_element(By.XPATH,"//input[@name='username']")
uname.send_keys("Admin")
passwd = driver.find_element(By.XPATH, "//input[@name='password']")
passwd.send_keys("admin456")
time.sleep(5)
# Click log in button to login the website.
login = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
login.click()
time.sleep(5)
invalid_login = driver.find_element(By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
print(invalid_login)
time.sleep(5)

# Add a new employee in the PIM module
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(5)
uname = driver.find_element(By.XPATH,"//input[@name='username']")
uname.send_keys("Admin")
passwd = driver.find_element(By.XPATH, "//input[@name='password']")
passwd.send_keys("admin123")
time.sleep(5)
# Click log in button to login the website.
login = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']")
login.click()
time.sleep(5)
PIM = driver.find_element(By.XPATH,"//a[contains(@href,'/web/index.php/pim/viewPimModule')]")
PIM.click()
time.sleep(10)
addEmp = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary']")
addEmp.click()
time.sleep(5)
firstName = driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Anjali")
lastName = driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("Kaira")
time.sleep(2)
save = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']").click()
time.sleep(5)
print("Employee is added successfully")
time.sleep(2)

# Edit an existing employee in the PIM module
PIM = driver.find_element(By.XPATH,"//a[contains(@href,'/web/index.php/pim/viewPimModule')]")
PIM.click()
time.sleep(5)
editEmp = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[4]/div/div[9]/div/button[2]/i").click()
# if editEmp.text == "Anjali":
#     editEmp.click()
time.sleep(5)
firstName = driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active orangehrm-firstname'and @name='firstName']").send_keys(" Goud")
save_edit = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
save_edit.click()
time.sleep(10)
print("Employee details are edited successfully")
time.sleep(5)

# Delete and existing employee in the PIM module
PIM = driver.find_element(By.XPATH,"//a[contains(@href,'/web/index.php/pim/viewPimModule')]")
PIM.click()
time.sleep(5)
driver.execute_script("window")
delEmp = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[9]/div/button[1]/i")
delEmp.click()
del_confirm = driver.find_element(By.XPATH,"//button[@class='oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin']")
del_confirm.click()
time.sleep(10)
print("Employee deleted successfully")
time.sleep(5)