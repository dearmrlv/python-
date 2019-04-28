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
                                                 "a float(10,2),"
                                                 "b float(10,2),"
                                                 "c float(10,2),"
                                                 "d float(10,2),"
                                                 # "e float(5,2),"
                                                 "f float(10,2))engine=innodb default charset=utf8;")
        for i in range(len(self.data['0'])-3):
            # self.cursor.execute("insert into " + table_name + "('total_population',"
            #                                                   "'male_population',"
            #                                                   "'female_population',"
            #                                                   "'city_population',"
            #                                                   "'country_population')"
            #                                                   "values("+self.data[0][i+2]+"," + self.data[1][i+2]+"," + self.data[2][i+2]+"," + self.data[3][i+2]+",)")
            # self.cursor.execute("insert into "+table_name+"(total_population) values("+self.data['0'][i+2]+");")
            self.cursor.execute("insert into "+table_name+"(a, b, c, d, f) "
                                                          "values("+self.data['0'][i+3]+','+self.data['1'][i+3]+','+self.data['2'][i+3]+','+self.data['3'][i+3]+','+self.data['4'][i+3]+");")
            # insert_info = ("insert into %s values (%s,%s,%s,%s,%s)")
            # info = (table_name,self.data['0'][i+2],self.data['1'][i+2],self.data['2'][i+2],self.data['3'][i+2],self.data['4'][i+2])
            # self.cursor.execute(insert_info,info)
            print(self.cursor.fetchone())
        self.db.commit()
        self.cursor.close()
        self.db.close()

db = Database("forest.json")
db.save_data("forest")