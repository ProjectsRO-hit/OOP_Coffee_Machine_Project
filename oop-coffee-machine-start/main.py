from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo

print(logo)
is_machine_on = True

while is_machine_on:
    order = input("Welcome To Dermora's Cafe! What would you like to order,'latte', 'espresso' or  'cappuccino': ").lower()

