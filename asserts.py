

def even_evens(l):
    count = 0
    
    for i in l:
        if ((i % 2) == 0 and i != 0):
            count += 1
        
    return ((count%2) == 0 and count != 0)



assert even_evens([]) == False, "Empty list should return false."
assert even_evens([3]) == False, "List with one odd number should return false."
assert even_evens([2]) == False, "List with one even number should return false."
assert even_evens([2, 3, 4]) == True, "List with two even numbers should return true."
assert even_evens([2, 5, 4, 6]) == False, "List with three evens should return false."
assert even_evens([1, 1, 1, 1]) == False, "List with even number of odds should return false."
assert even_evens([0, 0, 0, 0]) == False, "List with even number of zeros should return false."

	
print("All tests pass")