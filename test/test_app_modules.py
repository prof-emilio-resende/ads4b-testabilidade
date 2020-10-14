from app import config_app
from domain.logic import Fake

def test_app_overall_config():
  assert True

def test_app_modules_config():
  assert config_app() == True

def test_app_inner_modules_config():
  assert Fake().pretend() == True