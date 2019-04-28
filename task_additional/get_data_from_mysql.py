import pymysql
import pandas
db = pymysql.connect("localhost","user01","123456","population_data")
#db.cursor().execute("select * from test6")
sqlcmd = "select * from test6"
result = pandas.read_sql(sqlcmd,db)
print(result)
db.cursor().close()
db.close()

total_pop = result.iloc[:,1]
male_pop = result.iloc[:,2]
female_pop = result.iloc[:,3]
city_pop = result.iloc[:,4]
country_pop = result.iloc[:,5]

MFrate = [male_pop[i] / female_pop[i] for i in range(len(male_pop))]

# using matplotlib to draw curves
import matplotlib.pyplot as plt

x = [2018-i for i in range(20)]
x_str = [str(x[i]) for i in range(20)]
plt.figure()
plt.style.use('seaborn-poster')
plt.plot(x, MFrate)
plt.title('Male and Female rate in China')
plt.xlabel('year')
plt.ylabel('Rate')
plt.figure()
fig, ax = plt.subplots()
plt.style.use('seaborn-poster')
ax.barh(x_str, total_pop)
plt.title('Population in China')
plt.xlabel('year')
plt.ylabel('Population / 10 thousand')
plt.show()
