from selenium import webdriver
import time
# boot a webpage driver
driver = webdriver.Chrome('/home/lzy/Downloads/chromedriver')
# get the access to the url
url = "http://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0301&sj=2018"
driver.get(url)
# li1 = driver.find_element_by_id("treeZhiBiao_13")
# js = "var q=document.documentElement.scrollTop=10000"
time.sleep(2)
js = "var q=document.getElementsByClassName('main-left')[0].scrollTop = 10000"
driver.execute_script(js)
time.sleep(2)
a = driver.find_element_by_id("treeZhiBiao_13_a")
a.click()
time.sleep(2)
# a2 = driver.find_element_by_id("treeZhiBiao_42")
# a2.click()
li1 = driver.find_element_by_id("treeZhiBiao_13")
tmp = li1.find_elements_by_class_name('level2')
tmp[20].click()
# tmp = li1.find_elements_by_xpath("//ul/li")
# tmp[73].click()
droplist = driver.find_element_by_id("divdroplist")
# the html file doesn't contain <section> tag. it needs a click to show the data
droplist.click()
# find the last 20 years' data we need
li = droplist.find_elements_by_tag_name("li")  #the droplist is recorded in this array
li[2].click()
tables = driver.find_elements_by_class_name("public_table")[3]
tr = tables.find_elements_by_xpath("//tbody/tr")[18:24]
td = {}
for i in range(len(tr)):
    tmp = tr[i].find_elements_by_tag_name("td")
    # containing the lists in the dictionary in order to use the .append() method
    td[i] = ['']
    for j in range(len(tmp)-5):
        td[i].append(tmp[j].text)

import json
json_str = json.dumps(td, indent=4)
with open("forest.json",'w') as json_file:
    json_file.write(json_str)