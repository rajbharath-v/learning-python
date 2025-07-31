class cricket():
    def __init__(self):
       self.score=0
       self.wicket=0
       self.over=0
       self.ball=0
       self.line=[]
    def  add_run(self,run):
        if run not in [0,1,2,3,4,5,6]:
            print(" the entered run is not a corect numbered score")
        else:
            print("run added successfully")
            self.ball+=1
            self.score+=run
            self.line.append(run)
            self.update()
    def add_wicket(self):
        self.wicket+=1
        self.ball+=1
        self.line.append('w')
    def update(self):
        if self.ball==6:
            self.over+=1
            self.ball=0
    def show(self):
        print("---------------------")
        print("run",self.line)
        print("wicket",self.wicket)
        print("over:",self.over,".",self.ball)
        
         
def main():
    obj=cricket()
    print("cricket score")
    print("1.add run \n 2. add_wicket\n 3. update\n 4.show")
    choice=input("enter the choice between 1-4:")
    while True:
    
        if choice=='1':
            try:
                run = int(input("Enter runs scored (0,1,2,3,4,5,6): "))
                obj.add_run(run)
                
            except:
                print("Invalid input! Please enter a number.\n")
            
        elif choice=='2':
            obj.add_wicket()
            
        elif choice=='3':
            obj.update()
        elif choice=='4':
            obj.show()
        elif choice.lower() == 'exit':
            print("Exiting the cricket score tracker. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-4.")
        choice = input("Enter your choice (1-4) or type 'exit' ")

main()
           
    
