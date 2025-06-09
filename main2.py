from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("https://cutoff.tneaonline.org/")

input("🔒 Solve the CAPTCHA and press Enter once the first page loads...")

data = []

# Number of pages to iterate
total_pages = 155

for page_num in range(1, total_pages + 1):
    print(f"📄 Scraping Page {page_num}...")

    # Wait for table to be present
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "table-responsive-sm"))
    )

    # Scrape current page
    table_div = driver.find_element(By.CLASS_NAME, "table-responsive-sm")
    table = table_div.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")[1:]  # skip header

    for row in rows:
        cols = row.find_elements(By.TAG_NAME, "td")
        if len(cols) >= 13:
            data.append({
                "College Code": cols[0].text,
                "College Name": cols[1].text,
                "Branch Code": cols[2].text,
                "Branch Name": cols[3].text,
                "OC": cols[4].text,
                "BC": cols[5].text,
                "BCM": cols[6].text,
                "MBC": cols[7].text,
                "MBCDNC": cols[8].text,
                "MBCV": cols[9].text,
                "SC": cols[10].text,
                "SCA": cols[11].text,
                "ST": cols[12].text
            })

    # Click next page number if not on the last page
    if page_num < total_pages:
        try:
            # Scroll to page buttons if needed (optional)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(0.5)

            page_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, str(page_num + 1)))
            )
            page_link.click()
            time.sleep(1.5)  # give time for next page to load
        except Exception as e:
            print(f"⚠️ Failed to click page {page_num + 1}: {e}")
            break

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("tnea_cutoffs_all_2022.csv", index=False)
print("✅ Saved all data to 'tnea_cutoffs_all_2022.csv'")
