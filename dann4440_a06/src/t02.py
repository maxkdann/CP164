"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-03-04"
-------------------------------------------------------
"""
#process:
#get input in main and call function
#validate input in main, skip function call if you can
#else call function and write numbers to a list
#print from the list
def main():
    
    start = int(input("Enter start value: "))
    final = int(input("Enter final value: "))
    order = input("Enter order")
    #call function
    valid = print_odds(start, final, order)
    
        
def print_odds(start,final,order):
    #check validity
    valid = True
    if final>start or start<-10000 or final>10000 or order!="A" or order !="D":
        valid = False  
    #define list of numbers to print later
    nums = []
    #two while loops, one for each order
    if order=="A":
        #increment start if not even
        if start%2==0:
            start+=1
        #ascending order
        while start<final:
            nums.append(start)
            start+=2
    else:
        #descending order
        if final%2==0:
            final-=1
        while final>start:
            nums.append(final)
            final-=2
    
    print(nums)
    return valid
    
main()