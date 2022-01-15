from enum import Enum


class Order:
  def __init__(self, customer, airplane, route, cargo) -> None:
      self.customer = customer
      self.airplane = airplane
      self.route = route
      self.cargo = cargo
      self.status = Status.PREPARE

class Status(Enum):
  DONE = 'Завершен'
  PREPARE = 'Подготовка'
