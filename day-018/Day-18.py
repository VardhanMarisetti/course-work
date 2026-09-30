# ## Data Abstraction


# How to define abstract class, abstract method

from abc import ABC, abstractmethod

class Head_Mahindra(ABC):  # abstract class
    @abstractmethod
    def air_bag(self):  # abstract method
        pass

    @abstractmethod
    def wind_shield(self):  # abstract method
        pass

    def insurance(self):  # concrete method
        print("Please choose insurance from Mahindra company")

class Hyd_Mahindra(Head_Mahindra):
    def air_bag(self):  # abstract method
        print("Using Nylon to design air bag")

    def wind_shield(self):  # abstract method
        print("0.7 inch thick")

class Noida_Mahindra(Head_Mahindra):
    def air_bag(self):  # abstract method
        print("Using Cotton to design air bag")

    def wind_shield(self):  # abstract method
        print("0.5 inch thick")

obj_hyd = Hyd_Mahindra()
obj_noid = Noida_Mahindra()

obj_hyd.insurance()

# obj_head = Head_Mahindra()
