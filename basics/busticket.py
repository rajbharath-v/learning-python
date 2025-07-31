import random
import datetime
class busticket():
    def __init__(self):
        self.fromplace=0
        self.distination=0
        self.datetimes=self.datetime()
        self.ticketid=self.ticket_id()
        self.count=0
        self.kilometer=0
        
        
        
        
    def ticket_id(self):
        return "tkt"+str(random.randint(1000,9999))
    
    def datetime(self):
        return datetime.datetime.now()
    def calculation(self):
        
        print("total of amount is ",self.kilometer*10*self.count)
        
    
    def  ticket_generate(self):
        print("*********WELCOME TO THE CHENNAI MTC*****")
        self.fromplace=input("Enter the starting place ")
        self.distination=input("enter the distination place")
        self.kilometer=int(input("enter the kilometer "))
        self.count=int(input("enter the count of ticket"))
        print("------bill------")
        print("ticketid",self.ticketid)
        print(self.datetimes.strftime("%Y-%m-%d %H:%M:%S"))
        print("from",self.fromplace," to ->",self.distination)
        print("kilometer of travelling is",self.kilometer)
        print("no of ticket count",self.count)
        self.calculation()
        
def main():
    ticket=busticket()
    ticket.ticket_generate()
        
main()      
