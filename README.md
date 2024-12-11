
# Microsoft Login Automation with Selenium (Chrome)

This project demonstrates how to automate the login process to a Microsoft account using Selenium WebDriver with Google Chrome. The script automatically logs into your Microsoft account by filling in the email and password fields, without requiring manual input.

## Requirements

Ensure you have the following dependencies installed:

- **Python 3.6+**
- **Selenium**: WebDriver for automating browser interactions.
- **Chrome WebDriver**: For interacting with Google Chrome.
- **python-dotenv**: To load environment variables securely.
- **pyautogui**: To dont get catched by website while login.

### Install dependencies:

```bash
pip install selenium python-dotenv pyautogui
```

### Setup Chrome WebDriver

1. **Download ChromeDriver**: Download the appropriate version of ChromeDriver that matches your installed version of Google Chrome. You can get it here:  
   [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/)

2. **Add ChromeDriver to your PATH**: Ensure the `chromedriver` binary is either in your system's PATH or specify its location directly in the script.

## Environment Setup

Make sure your **.env** file contains the following:

```
email=your_microsoft_email@example.com
password=your_microsoft_password
```

This file is used to securely store and load your Microsoft login credentials.

## Script Overview

The script performs the following actions:

1. Launches Chrome and navigates to the Microsoft login page.
2. Automatically fills in the email field with the email stored in the `.env` file and submits the form.
3. Waits for the password page, fills in the password field, and submits the form.
4. Waits for user input to terminate the session and close the browser.

## Example Usage

### 1. Clone the repository:

```bash
git clone https://github.com/yourusername/microsoft-login-selenium.git
cd microsoft-login-selenium
```

### 2. Install the required dependencies:

```bash
pip install selenium python-dotenv
```

### 3. Ensure your `.env` file is set up correctly:

```
email=your_email@example.com
password=your_password
```

### 4. Run the script:

```bash
python login_automation.py
```

This will open Google Chrome, navigate to the Microsoft login page, and automatically log you in with the credentials from the `.env` file.

### 5. Exit the Program:

After the script logs you in, it will ask you to press any key to exit and close the browser.

## Full Script (`login_automation.py`)

```python
from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import dotenv
import time
import pyautogui

dotenv.load_dotenv()
driver = webdriver.Chrome()
driver.get("https://login.microsoftonline.com/common/oauth2/v2.0/authorize?scope=service%3A%3Aaccount.microsoft.com%3A%3AMBI_SSL+openid+profile+offline_access&response_type=code&client_id=81feaced-5ddd-41e7-8bef-3e20a2689bb7&redirect_uri=https%3A%2F%2Faccount.microsoft.com%2Fauth%2Fcomplete-signin-oauth&client-request-id=679e60a9-6abd-426b-8e59-208f07887e62&x-client-SKU=MSAL.Desktop&x-client-Ver=4.61.3.0&x-client-OS=Windows+Server+2019+Datacenter&prompt=login&client_info=1&state=H4sIAAAAAAAEAA3Ny6JCQAAA0H9pa8Gk8Vi0GMaQiOSVHaOLiJs8Rl9_7_mBs6Mwm0FBXK-AD3b2wH7pOjiKimR8P8XQ75s4kgNNzaLoZ5LxWRYlouh-saFTDx8Yo6q1zA-vlin1eOcrir2CpJRFXOJcF5znXRtOgs1BwVoJX5neZL7z-lQDlBkiqrTyfx3g3RLxkvCSR9pWu8Wvlf0ynKQsVsU6VS76pkoNCVhKDxa4kW7Bsloxl4Jgb8wJg7W2jgSXlyGsQa9fxi3VpqXmMzfg8tIegTrDp529_cmkFqXgEfOFRy1HsRqaTIhnrd7FtDXxcH3b94Bc_U2B7soBYndUAtxzRVs2HiajJAuahEofDLBSbU2c5BV8ZrNYlc33hqvfaGF8oOEo6Oh43P0BbW09aloBAAA&msaoauth2=true&lc=1033&sso_reload=true")

time.sleep(3)

#enter the email and submit
emailinput = driver.find_element(By.XPATH, './/input[@class="form-control ltr_override input ext-input text-box ext-text-box"]').click()
pyautogui.typewrite(os.environ["email"])
pyautogui.press('enter')


time.sleep(3)

#enter the password and submit
passwordinput = driver.find_element(By.NAME, "passwd")
pyautogui.typewrite(os.environ['password'])
pyautogui.press('enter')

input("Press any key to exit the program...")
driver.quit()

```

## Contributing

Feel free to fork the repository and submit issues or pull requests. All contributions are welcome!
