from domain.exceptions import ArgumentoInvalidoException
import abc

class Calculator(object):
  def __init__(self, a, b):
    if not type(a) in [float, int] or not type(b) in [float, int]:
      raise ArgumentoInvalidoException

    self.a = a
    self.b = b

  def calculate(self, operation):
    return operation.execute(self.a, self.b)

class OperationStrategy(abc.ABC):
  def execute(self, a, b):
    raise NotImplementedError("this is abstract!")

class SumConcreteStrategy(OperationStrategy):
  def execute(self, a, b):
    return a + b

def operation_factory(operator):
  operations = {
    '+' : SumConcreteStrategy()
  }

  return operations[operator]