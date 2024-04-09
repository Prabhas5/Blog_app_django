#selection sort

def selection(arr:list):
    if len(arr)<2:
        return arr
    pivot=arr[-1]
    small=selection([x for x in arr if x<pivot])
    large=selection([x for x in arr if x>pivot])
    return small+[pivot]+large
print(selection([6,4,2,6,1,7,8,9,1,4,6]))