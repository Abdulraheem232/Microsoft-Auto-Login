from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import dotenv
import time

dotenv.load_dotenv()

driver = webdriver.Edge()
driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=service%3A%3Aaccount.microsoft.com%3A%3AMBI_SSL+openid+profile+offline_access&response_type=code&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&redirect_uri=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin-oauth&client-request-id=679e60a9-6abd-426b-8e59-208f07887e62&x-client-SKU=MSAL.Desktop&x-client-Ver=4.61.3.0&x-client-OS=Windows+Server+2019+Datacenter&prompt=login&client_info=1&state=H4sIAAAAAAAEAA3Ny6JCQAAA0H9pa8Gk8Vi0GMaQiOSVHaOLiJs8Rl9_7_mBs6Mwm0FBXK-AD3b2wH7pOjiKimR8P8XQ75s4kgNNzaLoZ5LxWRYlouh-saFTDx8Yo6q1zA-vlin1eOcrir2CpJRFXOJcF5znXRtOgs1BwVoJX5neZL7z-lQDlBkiqrTyfx3g3RLxkvCSR9pWu8Wvlf0ynKQsVsU6VS76pkoNCVhKDxa4kW7Bsloxl4Jgb8wJg7W2jgSXlyGsQa9fxi3VpqXmMzfg8tIegTrDp529_cmkFqXgEfOFRy1HsRqaTIhnrd7FtDXxcH3b94Bc_U2B7soBYndUAtxzRVs2HiajJAuahEofDLBSbU2c5BV8ZrNYlc33hqvfaGF8oOEo6Oh43P0BbW09aloBAAA&msaoauth2=true&lc=1033&sso_reload=true")

time.sleep(3)

#enter the email and submit
emailinput = driver.find_element(By.XPATH, './/input[@class="form-control ltr_override input ext-input text-box ext-text-box"]')
emailinput.send_keys(os.environ["email"])
emailinput.submit()

time.sleep(3)

#enter the password and submit
passwordinput = driver.find_element(By.NAME, "passwd")
passwordinput.send_keys(os.environ["password"])
passwordinput.submit()

input("Press any key to exit the program...")
driver.quit()
