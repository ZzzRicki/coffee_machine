import pytest
from coffee_machine import CoffeeMachine, CupSize, NoCupsException, NoSugarException, NoCoffeeException

def test_select_cup_size():
    machine = CoffeeMachine()
    assert machine.select_cup_size(CupSize.SMALL) == 3
    assert machine.select_cup_size(CupSize.MEDIUM) == 5
    assert machine.select_cup_size(CupSize.LARGE) == 7

def test_select_sugar():
    machine = CoffeeMachine()
    assert machine.select_sugar(2) == 2

def test_invalid_sugar_amount():
    machine = CoffeeMachine()
    with pytest.raises(ValueError, match="Cantidad de azúcar insuficiente"):
        machine.select_sugar(-1)
    with pytest.raises(ValueError, match="El máximo de azúcar disponible es 5"):
        machine.select_sugar(6)

def test_no_cups_exception():
    machine = CoffeeMachine()
    machine.cups = 0
    with pytest.raises(NoCupsException):
        machine.select_cup_size(CupSize.SMALL)

def test_no_sugar_exception():
    machine = CoffeeMachine()
    machine.sugar = 0
    with pytest.raises(NoSugarException):
        machine.select_sugar(1)

def test_no_coffee_exception():
    machine = CoffeeMachine()
    machine.coffee = 0
    with pytest.raises(NoCoffeeException):
        machine.select_cup_size(CupSize.SMALL)
