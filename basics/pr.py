def prime(n):
    count=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            break
        else:
            count+=i
    print(f' the prime number between 1 to   ',count)      
            
        
n=100
prime(n)
