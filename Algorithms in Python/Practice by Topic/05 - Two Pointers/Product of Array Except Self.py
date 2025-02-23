from typing import List
# For every element in the input list, computes the product of all elements
# except the element itself.

# The product of all elements in the list except the element itself can
# be found simply by multiplying the L-R product to the left by the R-L 
# product to the right. Therefore, the function uses two passes and 
# computes two prefix products, one from left to right, and the other
# from right to left.
def product_of_array_except_self(nums: List[int]) -> List[int]:
    # Initialize variables to store intermediates and outputs
    prefix_product = [1]*len(nums) # Left to right
    results = [1]*len(nums)
    # Compute the L-R prefix product
    left = 1
    for i in range(len(nums)):
        prefix_product[i] = left
        left *= nums[i]
    # Compute the R-L prefix product and results
    right = 1
    for i in reversed(range(len(nums))):
        results[i] = right*prefix_product[i]
        right *= nums[i]

    return results

if __name__ == "__main__":
    s = '1 2 3 4'
    nums = [int(x) for x in s.split()]
    res = product_of_array_except_self(nums)
    print(" ".join(map(str, res)))
