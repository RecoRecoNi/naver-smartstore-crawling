import os
import time
from selenium.webdriver.support import expected_conditions as EC
from src.utils import OpenPyXL
from src.utils import get_driver
from src.crawling_stratege import get_review_in_page

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
url = "https://smartstore.naver.com/blackbeans/products/310288062"

driver = get_driver(user_agent = user_agent)
driver.get(url)
time.sleep(5)


if not os.path.exists('./results'):
    os.mkdir('./results')
    
save_data = get_review_in_page(driver)
OpenPyXL.save_file(save_data)
