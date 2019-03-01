from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(7)
    driver.get("https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=")
    screen=driver.current_window_handle
    driver.switch_to.window(screen)

    while True:
        job_list = driver.find_elements_by_css_selector(".item_con_list li .p_top a h3")
        for job in job_list:
            job.click()
            driver.switch_to.window(driver.window_handles[1])
            job_zhiwei = driver.find_element_by_css_selector(".name")
            job_gongsi = driver.find_element_by_css_selector(".company")
            job_xinzi = driver.find_element_by_css_selector(".salary")
            print("职位：" + job_zhiwei.text)
            print("公司：" + job_gongsi.text)
            print("薪资：" + job_xinzi.text)
            driver.close()
            driver.switch_to.window(screen)
            time.sleep(5)

        xiayiye= WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'.item_con_pager .pager_container > *:last-child')))
        xiayiye_class = xiayiye.get_attribute("class")
        if "pager_next_disabled" in xiayiye_class:
            break
        else:
            xiayiye.click()
            driver.switch_to.window(driver.current_window_handle)
            time.sleep(5)

finally:
    time.sleep(10)