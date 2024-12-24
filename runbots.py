from selenium import webdriver
import pandas as pd
import time
import os

# Load Roblox accounts from Excel
data = pd.read_excel('AdjustedRobloxAccounts.xlsx')  # Ensure this file is in the same directory
usernames = data['names'].tolist()
passwords = data['passwords'].tolist()

# Function to log in and join the game
def run_bot(username, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run Chrome in headless mode for better performance
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    try:
        # Navigate to login page
        driver.get("https://www.roblox.com/login")
        time.sleep(2)

        # Enter username and password
        driver.find_element("id", "login-username").send_keys(username)
        driver.find_element("id", "login-password").send_keys(password)
        driver.find_element("id", "login-button").click()
        time.sleep(5)

        # Navigate to Murder Mystery 2
        driver.get("https://www.roblox.com/games/142823291/Murder-Mystery-2")
        time.sleep(5)

        print(f"Bot for {username} successfully logged in and joined the game!")
    except Exception as e:
        print(f"Error for {username}: {e}")
    finally:
        driver.quit()

# Run the bots
if __name__ == "__main__":
    for username, password in zip(usernames, passwords):
        run_bot(username, password)
