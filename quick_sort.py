#take high as pivot


comparisons=[0]
def sort(numbers,left,right):
    pivot=right
    i=left-1
    for j in range(left,right):
        comparisons[0]+=1
        if numbers[j]<numbers[pivot] and i!=j:
            i+=1
            numbers[j],numbers[i]=numbers[i],numbers[j]
    numbers[pivot],numbers[i+1]=numbers[i+1],numbers[pivot]
    return i+1

def partition(numbers,left,right):
    if left<right:
        pivot=sort(numbers,left,right)
        partition(numbers,left,pivot-1)
        partition(numbers,pivot+1,right)
    
numbers=[]

with open("QuickSort.txt",'r') as f:
    
    for line in f.readlines():
        str1=line.split("\n")
        numbers.append(int(str1[0]))
partition(numbers,0,len(numbers)-1)
print(numbers,comparisons)

