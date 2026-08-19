class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Bad solution
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        heap = []
        for key, value in freq.items():
            heapq.heappush(heap, [-value, key])

        count = 0
        cooldowns = deque([])
        while cooldowns or heap:
            if (cooldowns and (count - cooldowns[-1][0] > n)) and (not heap or -cooldowns[-1][1][0] > -heap[0][0]) :

                maxFreq = cooldowns.pop()[1]
                maxFreq[0] += 1
                print(maxFreq[1])
                if maxFreq[0]:
                    cooldowns.appendleft([count,maxFreq])
                count += 1
                continue
            if heap:
                maxFreq = heapq.heappop(heap)
                maxFreq[0] += 1
                print(maxFreq[1])
                if maxFreq[0]:
                    cooldowns.appendleft([count, maxFreq])
            count += 1
        return count







            