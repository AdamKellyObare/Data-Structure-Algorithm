def remove_duplicates(sequence):
    return list(dict.fromkeys(sequence))

input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  
# Output: [2, 3, 4, 5, 6, 7]