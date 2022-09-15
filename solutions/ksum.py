"""
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def k_sum(k: int, nums: list) -> bool:
    for i in range(len(nums)):
        if k in map(lambda x:x+nums[i], nums[i+1:]):
            return True
    return False

def main():
    print(k_sum(17, list([10, 15, 3, 7]))) # True
    print(k_sum(19, list([0, 3, 6]))) # False
    print(k_sum(0, list([5, 3, 5, 1, 0]))) # False
    print(k_sum(500, list([100, 200, 300, 400, 500]))) # True
    
if __name__=="__main__":
    main()