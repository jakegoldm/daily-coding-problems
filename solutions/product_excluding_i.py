"""
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index 
i of the new array is the product of all the numbers in the original array 
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
[2, 3, 6].

Follow-up: what if you can't use division?
"""

def proudct_excluding_i(input:list) -> list:
    output = [0 for i in range(len(input))]
    for i in range(len(input)):
        product = 1
        for j in range(len(input)):
            if (i != j): product *= input[j]
        output[i] = product
    return output

def main():
    input = [1, 2, 3, 4, 5]
    print(input)
    output = proudct_excluding_i(input)
    print(output)

if __name__=="__main__":
    main()