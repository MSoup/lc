class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        expected_num = 1
        # before entering arr
        for i in range(len(arr)):
            while expected_num != arr[i]:
                k -= 1
                if k == 0:
                    return expected_num
                expected_num += 1
            # bump expected 
            expected_num += 1
        return expected_num + k - 1