from popdata import Popdata
from database import Database

data = Popdata()
chromedriver_address ='/home/lzy/Downloads/chromedriver'
data.get_data(chromedriver_address)
data.save2json("test3.json")
db = Database("test3.json")
db.save_data("test6")
