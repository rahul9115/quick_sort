#take high as pivot


comparisons=[0]

def ChoosePivot(a,end,start):

    length = end - start + 1
    median_index = length // 2 - 1 if length % 2 == 0 else length // 2
    median = start + median_index
    if a[start] <= a[median] <= a[end] or a[end] <= a[median] <= a[start]:
        a[start], a[median] = a[median], a[start]
    elif a[median] <= a[end] <= a[start] or a[start] <= a[end] <=  a[median]:
        a[start], a[end] = a[end], a[start]
    

def sort(numbers,left,right):
    pivot=left
    i=left
    ChoosePivot(numbers,right,left)
    for j in range(left+1,right+1):
        comparisons[0]+=1
       
        if numbers[j]<numbers[pivot] and i!=j:
            i+=1
            numbers[j],numbers[i]=numbers[i],numbers[j]
    numbers[pivot],numbers[i]=numbers[i],numbers[pivot]
    return i
# def sort(a,start, end):
        
#         pivot = start
#         ChoosePivot(a,end,start)
#         for i in range(start + 1, end + 1):
#             comparisons[0]+=1
#             if a[i] < a[start]:
#                 pivot += 1
#                 a[i], a[pivot] = a[pivot], a[i]
#         a[start], a[pivot] = a[pivot], a[start]
#         return pivot
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

