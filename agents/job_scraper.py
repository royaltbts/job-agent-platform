from playwright.sync_api import sync_playwright

def scrape_indeed(keyword, location="India", limit=10):
    keyword = keyword.replace(" ", "+")
    url = f"https://in.indeed.com/jobs?q={keyword}&l={location}"

    results = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, timeout=60000)

        # Wait for job cards
        try:
            page.wait_for_selector("div.job_seen_beacon", timeout=15000)
        except:
            print("No job listings found on page load.")
            return results

        job_cards = page.locator("div.job_seen_beacon")
        count = job_cards.count()

        for i in range(min(count, limit)):
            card = job_cards.nth(i)

            # Title
            try:
                title = card.locator("h2.jobTitle").inner_text()
            except:
                title = "N/A"

            # Company
            try:
                company = card.locator("span.companyName").inner_text()
            except:
                company = "N/A"

            # Location
            try:
                loc = card.locator("div.companyLocation").inner_text()
            except:
                loc = "N/A"

            # Correct job link selector
            try:
                job_link = card.locator("a.jcs-JobTitle").first.get_attribute("href")
                if job_link:
                    job_link = "https://in.indeed.com" + job_link
                else:
                    job_link = ""
            except:
                job_link = ""

            results.append({
                "title": title,
                "company": company,
                "location": loc,
                "link": job_link
            })

        browser.close()

    return results


# Test
if __name__ == "__main__":
    jobs = scrape_indeed("SAP procurement", "Hyderabad", limit=5)
    print("Jobs found:", len(jobs))
    for job in jobs:
        print(job)

