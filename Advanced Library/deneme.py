from time import sleep
from faker import Faker
from os import system

system("clear")

fake = Faker(['en_US'])

while True:
    sleep(0.1)
    print()
    print(fake.name())
    print(fake.address())
    print()