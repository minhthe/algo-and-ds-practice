'''https://www.jiuzhang.com/solution/maximum-sum-of-two-numbers/#tag-lang-python'''
def MaximumSum(self, A):
        sum_pq_map = defaultdict(list) # sum of digits : priority queue
        for num in A:
            digits_sum = self.get_digits_sum(num)
            heappush(sum_pq_map[digits_sum], num)
            if len(sum_pq_map[digits_sum]) > 2:
                heappop(sum_pq_map[digits_sum])
                
        ans = float('-inf')
        for pq in sum_pq_map.values():
            if len(pq) == 2:
                ans = max(ans, sum(pq))
        return ans if ans != float('-inf') else -1
            
def get_digits_sum(self, num):
        s = 0
        while num:
            s += num % 10
            num //= 10
        return s