from selenium import webdriver
driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(5)
driver.get("https://www.qiushibaike.com/text/")
driver.switch_to.window(driver.current_window_handle)
for b in range(1,14):
    zuozhe = driver.find_elements_by_css_selector(".col1 h2")
    neirong = driver.find_elements_by_css_selector(".content>span")
    haoxiao = driver.find_elements_by_css_selector(".stats-vote")
    xiayiye = driver.find_element_by_css_selector(".next")
    for i in range(0,len(zuozhe)) :
        show_zuozhe=("作者："+zuozhe[i].text)
        show_neirong = ("笑话：" + neirong[i].text)
        show_haoxiao = (haoxiao[i].text)
        print(show_zuozhe)
        print(show_neirong)
        print(show_haoxiao)
    if b<14:
        a=xiayiye.click()
    else:
        break







