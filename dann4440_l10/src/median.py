"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Max Dann
ID:      190274440
Email:   dann4440@mylaurier.ca
__updated__ = "2020-04-03"
-------------------------------------------------------
"""
fn = "numbers.txt"
fv = open(fn,"r",encoding = "utf-8")

def find_median(fv):
    #initialize list of numbers
    nums = []
    #read the file and add numbers to list
    line = fv.readline()
    while line!="":
        line = line.strip()
        #split the line to read every number individually
        current_line = line.split()
        for number in current_line:
            nums.append(int(number))
        line = fv.readline()
    #sort the list
    nums.sort()
    print(nums)
    #find the median
    if len(nums)%2!=0:
        mid = len(nums)//2
        median = nums[mid]
    else:
        mid1 = len(nums)//2
        mid2 = (len(nums)-1)//2
        median = (nums[mid1]+nums[mid2])/2
    return median

print(find_median(fv))