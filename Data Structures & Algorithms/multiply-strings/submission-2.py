class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        nums = {"0": 0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}

        prod = 0
        inner_prod = 0

        n1 = len(num1) - 1
        n2 = len(num2) - 1

        for i in range(n1, -1, -1):
            for j in range(n2, -1, -1):
                # print(nums.get(num1[i]))
                # print(nums.get(num2[j]))
                inner_prod += 10**(n2-j) * nums.get(num1[i]) * nums.get(num2[j])
                # print(prod)
            # print(inner_prod)
            prod += 10**(n1-i) * inner_prod
            inner_prod = 0
        
        print(prod)

        prod_str = str(prod)
        # for i in range(len(prod)):
        # prod_str.append(nums.get(prod[i]))

        return prod_str