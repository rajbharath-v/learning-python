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
        self.amount=0
        self.path={"poonthamalle":0,"karaiyanchavadi":3,"saec":5,"paruthipattu":8,"jbestate":10,"avadi":15}
        self.save=[]
    def ticket_id(self):
        return "tkt"+str(random.randint(1000,9999))
    
    def datetime(self):
        return datetime.datetime.now()
    def calculation(self):
        self.kilometer=abs(self.path[self.fromplace]-self.path[self.distination])
        amount=self.kilometer*10
        print("kilometer of travelling is",self.kilometer)
        print("total amount is ",amount)
    def save_record(self):   
        record=(self.ticketid,
            self.fromplace,
            self.distination,
            self.datetimes.strftime("%Y-%m-%d %H:%M:%S"),
            self.amount,
            self.count)
        self.save.append(record)
        
    def  ticket_generate(self):
        while True:
            print("*********WELCOME TO THE CHENNAI MTC*****")
            print("***AVAILABLE STOPS***")
            for place,distance in self.path.items():
                print(f" {place}-{distance}km")
            self.fromplace=input("Enter the starting place ")
            self.distination=input("enter the distination place")
            self.count=int(input("enter the count of ticket"))
            if self.fromplace not in self.path or self.distination not in self.path:
               print("!!!!This stop are not available in this bus !!!")
            else:
              print("------bill------")
              print("ticketid",self.ticketid)
              print(self.datetimes.strftime("%Y-%m-%d %H:%M:%S"))
              print("from",self.fromplace," to ->",self.distination)
            
              print("no of ticket count",self.count)
              self.calculation()
              self.save_record()
              print("******SAY0NORAAAA*****")
        
def main():
    ticket=busticket()
    print("1.ticket printing \n 2.history")
    choice=input("enter the choice")
    if choice=='1':
        ticket.ticket_generate()
    elif choice=='2':
        if len(ticket.save_record.record) == 0:
            print("No history available.")
        else:
            print("History of tickets:")
            for records in ticket.save_record.record:
                print(records)
    else :  
        print("Invalid choice! Please enter 1 or 2.")
        
          
        
          
    
        
    
    
        
main()      
