import pytest
from domain.models import Calculator, operation_factory
from domain.exceptions import ArgumentoInvalidoException


def test_calculator_sums_with_2_parms():
  # arrange
  a = 10
  b = 20
  expectation = 30

  # act
  result = Calculator(a, b).calculate(operation_factory('+'))

  # assert
  assert result == expectation

def test_calculator_sums_with_2_positive_parms():
  # arrange
  a = 2
  b = 2
  expectation = 4

  # act
  result = Calculator(a, b).calculate(operation_factory('+'))

  # assert
  assert result == expectation

def test_calculator_sums_with_2_negatives_parms():
  # arrange
  a = -2
  b = -2
  expectation = -4

  # act
  result = Calculator(a, b).calculate(operation_factory('+'))

  # assert
  assert result == expectation

def test_calculator_sums_with_2_mixed_parms():
  # arrange
  a = -2
  b = 2
  expectation = 0

  # act
  result = Calculator(a, b).calculate(operation_factory('+'))

  # assert
  assert result == expectation

def test_calculator_sums_with_notnumber_fail_with_argumentoinvalidoexception():
  # arrange
  a = 'notnumber'
  b = 2

  # assert
  with pytest.raises(ArgumentoInvalidoException):
    # act
    result = Calculator(a, b)

  # assert
  with pytest.raises(ArgumentoInvalidoException):
    # act
    result = Calculator(b, a)