from multiprocessing import AuthenticationError

from peewee import *

database = SqliteDatabase('db')
cursor = database.cursor()

# ----------------------------------------------------------

class BaseModel(Model):
  class Meta:
    database = database

class Airplane(BaseModel):
  id = AutoField()
  name = CharField()
  capacity = CharField()
  flightRange = CharField()

class Cargo(BaseModel):
  id = AutoField()
  weight = CharField()
  size = CharField()

class Customer(BaseModel):
  id = AutoField()
  fullname = CharField()
  address = CharField()
  phone = CharField()

class Order(BaseModel):
  id = AutoField()
  customer = CharField()
  airplane = CharField()
  route = CharField()
  cargo = CharField()
  status = CharField()

class Route(BaseModel):
  id = AutoField()
  pointFrom = CharField()
  pointTo = CharField()
  distance = CharField()
  timeFrom = CharField()
  timeTo = CharField()


# -----------------------------------------------------------
def create_tables():
    with database:
        database.create_tables([Airplane, Cargo, Customer, Order, Route])

# def getFullTable():
#   database.connect()
#   tables = database.get_tables()
#   for table in tables:
#     return cursor.execute("SELECT * FROM " + table);

create_tables()
