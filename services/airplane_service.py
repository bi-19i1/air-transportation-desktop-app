import imp
import os as os

from openpyxl import Workbook, load_workbook, worksheet
from storage import Storage

from ..models.airplane_model import Airplane
from ..settings import FILENAME, WB_NAME, WS_NAMES


class AirplaneService:
  def __init__(self, storage: Storage) -> None:
      self._storage = storage

  def create(self) -> Airplane:
    pass
