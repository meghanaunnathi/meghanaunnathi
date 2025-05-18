from abc import ABC
class vehicle(ABC):
    def speed(self):
        pass
class bike(vehicle):
      def speed(self):
          print("bike is running with 90 kmph")
class bus(vehicle):
    def speed(self):
        print("bus is running with 60 kmph")
class train(vehicle):
    def speed(self):
        print("train is running with 99 kmph")
b=bike()
b.speed()
b1=bus()
b1.speed()
t=train()
t.speed()
