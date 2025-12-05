import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from core.keychain import get_key


# -------------------------------
# Retrieve LinkedIn credentials
# -------------------------------

LINKEDIN_EMAIL = get_key("LINKEDIN_EMAIL")
LINKEDIN_PASSWORD = get_key("LINKEDIN_PASSWORD")

if not LINKEDIN_EMAIL or not LINKEDIN_PASSWORD:
    raise ValueError("ERROR: LinkedIn credentials not found in macOS Keychain!")


SEARCH_TERMS = [
    "Analytics Manager",
    "Data Analyst",
    "Sales Operations",
    "Incentive Compensation Analyst",
    "Customer Success Manager",
    "Customer Success Lead",
    "Client Success Specialist",
    "Business Analyst"
]

LOCATION = "Hyderabad"


def start_browser():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")

    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )


def login(driver):
    print("\nLogging into LinkedIn...")
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)

    driver.find_element(By.ID, "username").send_keys(LINKEDIN_EMAIL)
    time.sleep(1)
    driver.find_element(By.ID, "password").send_keys(LINKEDIN_PASSWORD)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(5)

    print("Logged in successfully!\n")


def find_easy_apply_jobs(driver, keyword, location):
    # LinkedIn Easy Apply Filter = f_AL=true
    search_url = (
        f"https://www.linkedin.com/jobs/search/?keywords={keyword}"
        f"&location={location}&f_AL=true"
    )

    print(f"Searching jobs for: {keyword}")
    driver.get(search_url)
    time.sleep(5)

    jobs = driver.find_elements(By.CSS_SELECTOR, "a.base-card__full-link")

    print(f"→ Found {len(jobs)} Easy Apply jobs")

    job_links = []
    for job in jobs:
        link = job.get_attribute("href")
        if link and "linkedin.com/jobs" in link:
            job_links.append(link)

    return job_links


def open_jobs(driver, job_links):
    for link in job_links:
        print("Opening:", link)
        driver.execute_script("window.open(arguments[0]);", link)
        time.sleep(3)


def run():
    driver = start_browser()

    login(driver)

    all_links = []

    for term in SEARCH_TERMS:
        links = find_easy_apply_jobs(driver, term, LOCATION)
        all_links.extend(links)

        open_jobs(driver, links)

        print(f"Done for: {term}\n")

    print("\nAll Easy Apply jobs opened in new tabs!")
    print("➡ Review each tab and click 'Easy Apply' manually.")

    input("\nPress ENTER to close browser when finished...")
    driver.quit()


if __name__ == "__main__":
    run()

