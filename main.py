import sys

from PySide6.QtWidgets import QApplication, QDialog, QInputDialog, QMainWindow

from models import Airplane, Cargo, Customer, Order, Route
from windows.airplane_edit_window import Airplane_Dialog
from windows.cargo_edit_window import Cargo_Dialog
from windows.customer_edit_window import Customer_Dialog
from windows.main_window import Ui_Form
from windows.order_edit_window import Order_Dialog


class AirplaneEditWindow(QDialog):
  def __init__(self, parent, airplane = Airplane()) -> None:
      super().__init__(parent)
      self.ui = Airplane_Dialog()
      self.ui.setupUi(self)
      self.airplane = airplane
      self.initData()
      self.ui.buttonBox.accepted.connect(self.saveData)

  def initData(self):
    self.ui.lne_name.setText(self.airplane.name)
    self.ui.lne_capacity.setText(self.airplane.capacity)
    self.ui.lne_flightRange.setText(self.airplane.flightRange)

  def saveData(self):
    self.airplane.name = self.ui.lne_name.text()
    self.airplane.capacity = self.ui.lne_capacity.text()
    self.airplane.flightRange = self.ui.lne_flightRange.text()

    self.airplane.save()

class CargoEditWindow(QDialog):
  def __init__(self, parent, entity = Cargo()) -> None:
      super().__init__(parent)
      self.ui = Cargo_Dialog()
      self.ui.setupUi(self)
      self.entity = entity
      self.initData()
      self.ui.buttonBox.accepted.connect(self.saveData)

  def initData(self):
    self.ui.lne_name.setText(self.entity.weight)
    self.ui.lne_capacity.setText(self.entity.size)

  def saveData(self):
    self.entity.weight = self.ui.lne_name.text()
    self.entity.size = self.ui.lne_capacity.text()

    self.entity.save()


class CustomerEditWindow(QDialog):
  def __init__(self, parent, entity = Customer()) -> None:
      super().__init__(parent)
      self.ui = Customer_Dialog()
      self.ui.setupUi(self)
      self.entity = entity
      self.initData()
      self.ui.buttonBox.accepted.connect(self.saveData)

  def initData(self):
    self.ui.lne_name.setText(self.entity.fullname)
    self.ui.lne_capacity.setText(self.entity.address)
    self.ui.lne_flightRange.setText(self.entity.phone)


  def saveData(self):
    self.entity.fullname = self.ui.lne_name.text()
    self.entity.address = self.ui.lne_capacity.text()
    self.entity.phone = self.ui.lne_flightRange.text()


    self.entity.save()


class OrderEditWindow(QDialog):
  def __init__(self, parent, entity = Order()) -> None:
      super().__init__(parent)
      self.ui = Order_Dialog()
      self.ui.setupUi(self)
      self.entity = entity
      self.initData()
      self.ui.buttonBox.accepted.connect(self.saveData)

  def initData(self):
    self.ui.lne_name.setText(self.entity.customer)
    self.ui.lne_capacity.setText(self.entity.airplane)
    self.ui.lne_flightRange.setText(self.entity.route)
    self.ui.lne_flightRange_2.setText(self.entity.cargo)
    self.ui.lne_flightRange_4.setText(self.entity.status)


  def saveData(self):
    self.entity.customer = self.ui.lne_name.text()
    self.entity.airplane = self.ui.lne_capacity.text()
    self.entity.route = self.ui.lne_flightRange.text()
    self.entity.cargo = self.ui.lne_flightRange_2.text()
    self.entity.status = self.ui.lne_flightRange_4.text()



    self.entity.save()


class RouteEditWindow(QDialog):
  def __init__(self, parent, entity = Route()) -> None:
    super().__init__(parent)
    self.ui = Order_Dialog()
    self.ui.setupUi(self)
    self.entity = entity
    self.initData()
    self.ui.buttonBox.accepted.connect(self.saveData)

  def initData(self):
    self.ui.lne_name.setText(self.entity.pointFrom)
    self.ui.lne_capacity.setText(self.entity.pointTo)
    self.ui.lne_flightRange.setText(self.entity.distance)
    self.ui.lne_flightRange_2.setText(self.entity.timeFrom)
    self.ui.lne_flightRange_4.setText(self.entity.timeTo)


  def saveData(self):
    self.entity.pointFrom = self.ui.lne_name.text()
    self.entity.pointTo = self.ui.lne_capacity.text()
    self.entity.distance = self.ui.lne_flightRange.text()
    self.entity.timeFrom = self.ui.lne_flightRange_2.text()
    self.entity.timeTo = self.ui.lne_flightRange_4.text()



    self.entity.save()




class MainWindow(QMainWindow):
    def __init__(self):
      super(MainWindow, self).__init__()
      self.ui = Ui_Form()
      self.ui.setupUi(self)
      self.setWindowTitle('Airplane transportation');
      self.ui.btn_airplane_add.clicked.connect(self.addAirpalne)
      self.ui.btn_airplane_change.clicked.connect(self.changeAirplane)
      self.ui.btn_airplane_del.clicked.connect(self.deleteAirplane)

      self.ui.btn_cargo_add.clicked.connect(self.addCargo)
      self.ui.btn_cargo_change.clicked.connect(self.changeCargo)
      self.ui.btn_cargo_del.clicked.connect(self.deleteCargo)

      self.ui.btn_custom_add.clicked.connect(self.addCustomer)
      self.ui.btn_custom_change.clicked.connect(self.changeCustomer)
      self.ui.btn_custom_del.clicked.connect(self.deleteCustomer)

      self.ui.btn_order_add.clicked.connect(self.addOrder)
      self.ui.btn_order_change.clicked.connect(self.changeOrder)
      self.ui.btn_order_del.clicked.connect(self.deleteOrder)

      self.ui.btn_route_add.clicked.connect(self.addRoute)
      self.ui.btn_route_change.clicked.connect(self.changeRoute)
      self.ui.btn_route_del.clicked.connect(self.deleteRoute)

    def deleteRoute(self):
      id = self.showDialog()
      entity = Route.get(Route.id == id)
      entity.delete_instance()

    def changeRoute(self):
      for entity in Route.select():
        print(str(entity.id) + ' | ' + entity.pointFrom + ' | ' + entity.pointTo + ' | ' + entity.distance + ' | ' + entity.timeFrom + ' | ' + entity.timeTo)
      id = self.showDialog()
      entity = Route.get(Route.id == id)
      RouteEditWindow(self, entity).show()

    def addRoute(self):
      RouteEditWindow(self).show()

    def deleteOrder(self):
      id = self.showDialog()
      entity = Order.get(Order.id == id)
      entity.delete_instance()

    def changeOrder(self):
      for entity in Order.select():
        print(str(entity.id) + ' | ' + entity.customer + ' | ' + entity.airplane + ' | ' + entity.route + ' | ' + entity.cargo + ' | ' + entity.status)
      id = self.showDialog()
      entity = Order.get(Order.id == id)
      OrderEditWindow(self, entity).show()

    def addOrder(self):
      OrderEditWindow(self).show()


    def deleteCustomer(self):
      id = self.showDialog()
      entity = Customer.get(Customer.id == id)
      entity.delete_instance()

    def changeCustomer(self):
      for entity in Customer.select():
        print(str(entity.id) + ' | ' + entity.fullname + ' | ' + entity.address + ' | ' + entity.phone )
      id = self.showDialog()
      entity = Customer.get(Customer.id == id)
      CustomerEditWindow(self, entity).show()

    def addCustomer(self):
      CustomerEditWindow(self).show()

    def deleteCargo(self):
      id = self.showDialog()
      entity = Cargo.get(Cargo.id == id)
      entity.delete_instance()

    def changeCargo(self):
      for entity in Cargo.select():
        print(str(entity.id) + ' | ' + entity.weight + ' | ' + entity.size)
      id = self.showDialog()
      entity = Cargo.get(Cargo.id == id)
      CargoEditWindow(self, entity).show()

    def addCargo(self):
      CargoEditWindow(self).show()

    def deleteAirplane(self):
      id = self.showDialog()
      airplane = Airplane.get(Airplane.id == id)
      airplane.delete_instance()

    def addAirpalne(self):
      AirplaneEditWindow(self).show()

    def changeAirplane(self):
      for entity in Airplane.select():
        print(str(entity.id) + ' | ' + entity.name + ' | ' + entity.capacity + ' | ' + entity.flightRange )
      id = self.showDialog()
      airplane = Airplane.get(Airplane.id == id)
      AirplaneEditWindow(self, airplane).show()

    def showDialog(self):
      text, ok = QInputDialog.getText(self, 'Air',
          'Введите ID:')
      if ok:
          return text


if __name__ == "__main__":
  app = QApplication(sys.argv)

  window = MainWindow()
  window.show()

  sys.exit(app.exec())
