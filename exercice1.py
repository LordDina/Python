def test_distinct(sequence):

    for i in range(len(sequence)):
        for j in range(i + 1, len(sequence)):
            if sequence[i] == sequence[j]:
                return False
    return True

print(test_distinct([1, 5, 7, 9]))         
print(test_distinct([2, 4, 5, 5, 7, 9]))  
