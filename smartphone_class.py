# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"


# Derived class representing a Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, os, storage):
        super().__init__(brand, model)
        self.os = os  # Operating System
        self.storage = storage  # Storage in GB

    def phone_info(self):
        return f"{self.device_info()}, OS: {self.os}, Storage: {self.storage}GB"

    def make_call(self, number):
        return f"Calling {number} using {self.brand} {self.model}..."


# Creating instances of the Smartphone class
phone1 = Smartphone("Apple", "iPhone 14", "iOS", 128)
phone2 = Smartphone("Samsung", "Galaxy S21", "Android", 256)

# Displaying phone information
print(phone1.phone_info())
print(phone2.phone_info())

# Making a call
print(phone1.make_call("123-456-7890"))
