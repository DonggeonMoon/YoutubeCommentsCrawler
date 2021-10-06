from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.youtube.com/watch?v=Bk7Spztj-oc")
driver.implicitly_wait(3)


prev_height = driver.execute_script("return document.body.scrolHeight")

for i in range(0, 500):
    driver.execute_script("window.scrollBy(0, 10000)")
    print(i)

for i in range(1, 30):
    print(driver.find_element_by_css_selector('#contents > ytd-comment-thread-renderer:nth-child(' + str(i) + ') > #comment > #body > #main > #header > #header-author > h3').text)
    print("----------------------------")
    print(driver.find_element_by_css_selector('#contents > ytd-comment-thread-renderer:nth-child(' + str(i) + ') > #comment > #body > #main > #header > #header-author > yt-formatted-string').text)
    print("----------------------------")
    print(driver.find_element_by_css_selector('#contents > ytd-comment-thread-renderer:nth-child(' + str(i) + ') > #comment > #body > #main > #expander').text)
    print("----------------------------")

print("완료")
