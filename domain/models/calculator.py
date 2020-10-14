from domain.exceptions import ArgumentoInvalidoException

class Calculator(object):
  def __init__(self, a, b):
    if not isinstance(a, float) and not isinstance(a, int):
      raise ArgumentoInvalidoException

    self.a = a
    self.b = b

  def sum(self):
    return self.a + self.b