# https://leetcode.com/problems/exclusive-time-of-functions/

def exclusive_time(n, logs):
    stack = []
    results = [0] * n

    for log in logs:
        tmp = log.split(':')
        fn_id, action, timestamp = int(tmp[0]), tmp[1], int(tmp[2])

        if action == 'start':
            if stack:
                # pause the current running function, leave it in stack
                results[stack[-1][0]] += timestamp - stack[-1][1]
                stack[-1][1] = timestamp
            stack.append([fn_id, timestamp]) # add new function to stack
        else:
            # end current running function
            start_fn_id, start_time = stack.pop()
            results[start_fn_id] += timestamp - start_time + 1
            if stack:
                stack[-1][1] = timestamp + 1 # resume a function
    return results


logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
assert exclusive_time(2, logs) == [3,4]

logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
assert exclusive_time(1, logs) == [8]

logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
assert exclusive_time(2, logs) == [7,1]