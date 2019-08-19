def count_positives_sum_negatives(arr):
    counter=0
    sum=0
    i=0
    if len(arr) == 0:
        return []
    else:    
        while i<len(arr):
            if arr[i] > 0:
                counter+=1
            elif arr[i] < 0:
                sum+=arr[i]
            i+=1    
    return [counter, sum] 