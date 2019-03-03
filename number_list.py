
def find_reverse(numbers):
    #TODO: find the reverse of the list
    return numbers[::-1]
def find_max(numbers):
    #TODO: find the maximum of the list
    return max(numbers)

def find_min(numbers):
    #TODO: find the minimum of the list
    return min(numbers)

def find_sum(numbers):
    #TODO: find the sum of all the numbers in the list
    return sum(numbers)

def find_average(numbers):
    #TODO: find the average of all the numbers in the list
    return sum(numbers)/len(numbers)

def find_descending(numbers):
    #TODO: numbers sorted in descending order

    return sorted(numbers,reverse = True)
def second_smallest(numbers):
    #TODO: find the second smallest
    min_1 = 10000
    min_2 = 10000
    master = set(numbers)

    for num in master:
       if num <= min_1:
          min_2 = min_1
          min_1 = num
       elif num < min_2:
          min_2 = num
    return min_2

def kth_smallest(numbers, k):
    #TODO: find the kth smallest number in the list
    
    number = set(numbers)
    number = sorted(number)
    return number[k-1]

if __name__ == '__main__':
    # If you are testing, place your print statements here
    pass
