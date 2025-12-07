from enum import Enum


class EventType(Enum):
  CREATE = "create"
  CREATE_MANY = "create many" # чтобы не спамить событиями
  UPDATE = "update"
  DELETE = "delete"