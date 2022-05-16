from collections import Counter


class Solution:
    #today is truly problem solving day
    def minSetSize(self, arr) -> int:
        arr_count = Counter(arr)

        arr_count = sorted(arr_count.items(), key=lambda x: x[1], reverse=True)

        tot = 0
        num_of_set = 0

        for num in arr_count:
            if tot >= len(arr)/2:
                break
            tot += num[1]
            num_of_set += 1

        return num_of_set
