'''
strategy to be used here:
    - iterate

complexity:
    - o(k) time and O(1) space {k = num of logs and single pass is done}
'''

class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        # 1. set ans_id, ans_max_time, last_time
        ans_id = logs[0][0] # id with most time worked
        ans_max_time = logs[0][1] # max time worked by the id
        last_time = 0 # last time we went from

        # 2. iterate over the logs
        for id, leave_time in logs:
            duration = leave_time - last_time
            if duration > ans_max_time:
                ans_max_time = duration
                ans_id = id
            elif duration == ans_max_time:
                ans_id = min(ans_id, id)
            last_time = leave_time

        # 3. return the ans_id
        return ans_id
