"""
-------------------------------------------------------
[t01]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-02-04"
-------------------------------------------------------
""" 
from Queue_circular import Queue
from Food import Food

def main():
    q = Queue(2)
    
    f1 = Food("bread",1,True,6)
    f2 = Food("milk",5,True,77)
    f3 = Food("Cow",2,False,69)
    print("Check empty should be true:",q.is_empty())
    print("Is full should be false:",q.is_full())
    q.insert(f1)
    print("Inserted f1, peek it:",q.peek())
    q.insert(f2)
    print("length is:",len(q))
    print("inserted f2, queue should now be full (true):",q.is_full())
    print("it should also not be empty(false):",q.is_empty())
    v = q.remove()
    print("removed the front value",v)
    q.insert(f3)
    for v in q:
        print(v)
main()