# TODO: Write a selection_sort_descend_trace() function that 
#       sorts the numbers list into descending order
largest_int = 0
def selection_sort_descend_trace(numbers):
    for i in range(len(numbers)-1):
        largest_int = i
        for j in range(i+1,len(numbers)):
            if numbers[largest_int] < numbers[j]:
                    largest_int = j
        numbers[i], numbers[largest_int] = numbers[largest_int], numbers[i]
        for k in numbers:
            print(k, end=" ")
        print()
    return numbers
            

if __name__ == "__main__":
    # TODO: Read in a list of integers into numbers, then call
    #       selection_sort_descend_trace() to sort the numbers
    numbers = [int(k) for k in input("").split()]
    selection_sort_descend_trace(numbers) 
