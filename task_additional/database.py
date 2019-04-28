import pymysql
# here I use the package pymysql give operation order to mysql through
# which a table will be established in the database called population_data
import json

class Database():
    def __init__(self, json_name):
        # requirement for data:
        # data = PopData()
        # data.data_init()
        with open(json_name, encoding='utf-8') as f:
            self.data = json.load(f)
        self.db = pymysql.connect("localhost","user01","123456","population_data")
        self.cursor = self.db.cursor()

    def save_data(self, table_name):
        self.table_name = table_name
        self.cursor.execute("create table "+table_name+"(id int not null auto_increment primary key,"
                                                 "total_population int unsigned,"
                                                 "male_population int unsigned,"
                                                 "female_population int unsigned,"
                                                 "city_population int unsigned,"
                                                 "country_population int unsigned)engine=innodb default charset=utf8;")
        for i in range(len(self.data['0'])-2):
            # self.cursor.execute("insert into " + table_name + "('total_population',"
            #                                                   "'male_population',"
            #                                                   "'female_population',"
            #                                                   "'city_population',"
            #                                                   "'country_population')"
            #                                                   "values("+self.data[0][i+2]+"," + self.data[1][i+2]+"," + self.data[2][i+2]+"," + self.data[3][i+2]+",)")
            # self.cursor.execute("insert into "+table_name+"(total_population) values("+self.data['0'][i+2]+");")
            self.cursor.execute("insert into "+table_name+"(total_population, male_population, female_population, city_population, country_population) "
                                                          "values("+self.data['0'][i+2]+','+self.data['1'][i+2]+','+self.data['2'][i+2]+','+self.data['3'][i+2]+','+self.data['4'][i+2]+");")
            # insert_info = ("insert into %s values (%s,%s,%s,%s,%s)")
            # info = (table_name,self.data['0'][i+2],self.data['1'][i+2],self.data['2'][i+2],self.data['3'][i+2],self.data['4'][i+2])
            # self.cursor.execute(insert_info,info)
            print(self.cursor.fetchone())
        self.db.commit()
        self.cursor.close()
        self.db.close()