from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class WebScraper:
    def __init__(self, driver_path, headless=False):
        self.driver_path = driver_path
        self.headless = headless
        self.browser = self._init_driver()

    def _init_driver(self):
        options = Options()
        if self.headless:
            options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        service = Service(executable_path=self.driver_path)
        return webdriver.Chrome(service=service, options=options)

    def open_page(self, url):
        self.browser.get(url)

    def click_button(self, xpath):
        try:
            button = WebDriverWait(self.browser, 100).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            button.click()
        except Exception as e:
            print(f"An error occurred while trying to click the button: {e}")

    def fill_textbox(self, xpath, input_value):
        try:
            textbox = WebDriverWait(self.browser, 100).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            textbox.clear()  # Clear any existing text in the textbox
            textbox.send_keys(input_value)
        except Exception as e:
            print(f"An error occurred while trying to fill the textbox: {e}")

    def login(self, username_xpath, password_xpath, submit_button_xpath, username, password):
        try:
            # Wait for the username textbox to be visible
            self.fill_textbox(username_xpath, username)

            # Wait for the password textbox to be visible and fill it
            self.fill_textbox(password_xpath, password)

            # Wait for the submit button to be clickable and click it
            self.click_button(submit_button_xpath)
        except Exception as e:
            print(f"An error occurred during the login process: {e}")

    def extract_data(self):
        # Placeholder for method to extract data from the page
        pass

    def close_browser(self):
        self.browser.quit()

    def scrape(self, url):
        try:
            self.open_page(url)
            self.extract_data()
        finally:
            pass
            #self.close_browser()


# Example usage
if __name__ == "__main__":
    driver_path = "/opt/homebrew/bin/chromedriver"  # Adjust to your chromedriver path
    url = "https://www.naukri.com"  # Replace with the target URL
    search_button_xpath = r'//*[@id="root"]/div[7]/div/div/div[6]'  # Replace with the actual XPath
    search_textbox_xpath = r'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input'  # Replace with the actual XPath
    input_value = "DevOps Architect"  # Replace with the desired input value

    login_button_xpath = r'//*[@id="root"]/div[7]/div/div/div[6]'  # Replace with the actual XPath
    loginuser_textbox_xpath = r'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input'  # Replace with the actual XPath
    loginpass_textbox_xpath = r'//*[@id="root"]/div[7]/div/div/div[1]/div/div/div/div[1]/div/input'  # Replace with the actual XPath

    login_user_val = "abc@gmail.com"
    login_pass_val = ""

    login_user_input_xpath = ""
    login_pass_input_xpath = ""

    scraper = WebScraper(driver_path)
    scraper.open_page(url)
    # scraper.fill_textbox(search_textbox_xpath, input_value)
    # scraper.click_button(search_button_xpath)


    login_button_xpath = r"//*[@id='login_Layer']"
    login_submit_xpath = r"//*[@id='root']/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button"
    scraper.click_button(login_button_xpath)

    time.sleep(2000)

    scraper.fill_textbox(login_user_input_xpath, login_user_val)
    scraper.fill_textbox(login_pass_input_xpath, login_pass_val)
    scraper.click_button(login_submit_xpath)

    input("hello 100:")
