import pymysql
import pandas
db = pymysql.connect("localhost","user01","123456","population_data")
#db.cursor().execute("select * from test6")
sqlcmd = "select * from forest"
result = pandas.read_sql(sqlcmd,db)
print(result)
db.cursor().close()
db.close()

forestry_land = result.iloc[:,1]
forestry_area = result.iloc[:,2]
forestry_area_man_made = result.iloc[:,3]
forest_coverage_rate = result.iloc[:,4]
forest_stock = result.iloc[:,5]

# using matplotlib to draw curves
import matplotlib.pyplot as plt

x = [2017-i for i in range(14)]
x_str = [str(x[i]) for i in range(14)]

plt.style.use('seaborn-poster')
tmp_x = x_str[::-1]
tmp_y = forestry_area[::-1]
#plt.plot(x_str, forestry_area)
plt.plot(tmp_x, tmp_y)
plt.title('forestry area in China')
plt.xlabel('year')
plt.ylabel('forestry area / 10 thousand hectares')
# plt.figure()
fig, ax = plt.subplots()
plt.style.use('seaborn-poster')
ax.barh(x_str, forest_stock)
plt.title('forest stock in China')
plt.ylabel('year')
plt.xlabel('forest stock / 100 million cubic meters')
plt.show()
