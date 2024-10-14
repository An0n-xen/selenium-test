from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def google_search(search_term):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode (optional)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to Google
        driver.get("https://www.google.com")

        # Find the search box
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )

        # Enter the search term
        search_box.send_keys(search_term)
        search_box.send_keys(Keys.RETURN)

        # Wait for search results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search"))
        )

        # Print the title of the search results page
        print(f"Search results page title: {driver.title}")

        # Optionally, you can extract and print the search results here
        # For example:
        results = driver.find_elements(By.CSS_SELECTOR, "div.g")
        for result in results[:5]:  # Print first 5 results
            print(result.text)
            print("---")

    finally:
        # Close the browser
        driver.quit()


if __name__ == "__main__":
    search_term = "AI tools site;www.crushbase.com"
    google_search(search_term)
