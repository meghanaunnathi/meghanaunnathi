from abc import ABC,abstractmethod
class bank(ABC):
    bankname="RBI"
    def display(self):
        print("parent bank is",self.bankname)
    @abstractmethod
    def rateofintrest(self):
        pass
class sbi(bank):
    def print(self):
        print("this is SBI bank")
    def rateofintrest(self):
        print("it provides RI of 8%")
s=sbi()
s.display()
s.print()
s.rateofintrest()




