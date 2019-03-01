from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("./chromedriver.exe")
try:
    driver.implicitly_wait(7)
    driver.get("https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=")
    screen=driver.current_window_handle
    driver.switch_to.window(screen)

    while True:
        job_list = driver.find_elements_by_css_selector(".item_con_list li")
        for job in job_list:
            job_link = driver.find_element_by_css_selector(".p_top a h3")
            job_link.click()
            driver.switch_to.window(driver.window_handles[1])
            job_zhiwei=driver.find_element_by_css_selector(".name")
            job_gongsi=driver.find_element_by_css_selector(".company")
            job_xinzi=driver.find_element_by_css_selector(".salary")
            print("职位："+job_zhiwei.text)
            print("公司："+job_gongsi.text)
            print("薪资："+job_xinzi.text)
            driver.close()
            driver.switch_to.window(screen)
            time.sleep(6)

finally:
    quit()






