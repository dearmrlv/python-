from selenium import webdriver
import json

class Popdata():
    # self.data contains all the data
    # self.years contains the years that the data crosses
    # self.population contains the data of population of each year
    # to use this class, you should first use the method .get_data() to get the data
    # use method .getting_total_population to save the data of population
    # use method .getting_years to save the data of years in attribute .years
    # or you can simply use the method data_init to complete the work mentioned above
    def __init__(self):
        self.type = 1

    def get_data(self, chromedriver_address):
        # boot a web page
        # firstly you have to locate your chrome driver
        driver = webdriver.Chrome(chromedriver_address)
        # get the access to the url
        url = "http://data.stats.gov.cn/easyquery.htm?cn=C01&zb=A0301&sj=2018"
        driver.get(url)
        # find the droplist leading to the years
        droplist = driver.find_element_by_id("divdroplist")
        # the html file doesn't contain <section> tag. it needs a click to show the data
        droplist.click()
        # find the last 20 years' data we need
        li = droplist.find_elements_by_tag_name("li")  # the droplist is recorded in this array
        li[2].click()
        # find the data we need
        tables = driver.find_elements_by_class_name("public_table")[3]
        tr = tables.find_elements_by_xpath("//tbody/tr")[15:20]
        # save the data to a dictionary
        td = {}
        for i in range(len(tr)):
            tmp = tr[i].find_elements_by_tag_name("td")
            # containing the lists in the dictionary in order to use the .append() method
            td[i] = ['']
            for j in range(len(tmp)):
                td[i].append(tmp[j].text)
            # in td[i], the first element[0] is always None,
            # and the element[1] are the head name of the data in the list,
            # and the following data corresponds to the year from 1999 to 2018
        self.data = td
        self.total_population = self.data[0]
        self.male_population = self.data[1]
        self.female_population = self.data[2]
        self.city_population = self.data[3]
        self.country_population = self.data[4]
        self.years = [i+1999 for i in range(20)]

    def save2json(self, json_name):
        self.json_name = json_name
        json_str = json.dumps(self.data, indent=4)
        with open(json_name, 'w') as json_file:
            json_file.write(json_str)
