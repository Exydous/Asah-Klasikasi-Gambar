from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

url = 'https://www.tokopedia.com/sony-center-official/review'

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
driver.get(url)

data = []

for i in range(350):  # maks 350 halaman
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    containers = soup.find_all('article', attrs={'class': 'css-1pr2lii'})
    
    for container in containers:
        try:
            username = container.find('span', attrs={'class': 'name'}).text.strip()
        except:
            username = None
        
        try:
            product_name = container.find('p', attrs={'data-unify': 'Typography'}).text.strip()
        except:
            product_name = None
        
        try:
            review = container.find('span', attrs={'data-testid': 'lblItemUlasan'}).text.strip()
        except:
            review = None
        
        try:
            rating_element = container.find('div', attrs={'data-testid': 'icnStarRating'})
            if rating_element and rating_element.has_attr('aria-label'):
                stars_text = rating_element['aria-label']  # contoh: "bintang 5"
                stars = int(stars_text.split()[-1])        # ambil angka terakhir
            else:
                stars = None
        except:
            stars = None

        # ✅ Simpan sebagai dictionary
        if review:
            data.append({
                'username': username,
                'product_name': product_name,
                'review': review,
                'rating': stars
            })

    # Klik tombol halaman berikutnya
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Laman berikutnya']")
        driver.execute_script("arguments[0].click();", next_button)
        time.sleep(3)
    except Exception as e:
        print(f"Tidak ada halaman berikutnya pada iterasi {i}. Selesai scraping.")
        break

# ✅ Simpan ke CSV
with open('tokopedia_reviews.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['username', 'product_name', 'review', 'rating'])
    writer.writeheader()
    writer.writerows(data)

print(f"Scraping selesai. Total data: {len(data)}")
driver.quit()