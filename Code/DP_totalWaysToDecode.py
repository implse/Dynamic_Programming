# A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:

# "A":1, "B":2, "C":3 "D":4 ...

# Determine the total number of ways the message can be decoded


# Dynamic Programming : Time O(n) / Space O(n)
from collections import defaultdict

def decode_ways(message):
    cache = defaultdict(int)
    cache[len(message)] = 1

    for i in reversed(range(len(message))):
        if message[i].startswith("0"):
            cache[i] = 0
        elif i == len(message) - 1:
            cache[i] = 1
        else:
            if int(message[i:i + 2]) <= 26:
                cache[i] = cache[i + 2]
            cache[i] += cache[i + 1]
    return cache[0]

#Test
message_1 = "2263" # (2, 2, 6, 3) or (22, 6, 3) or (2, 26, 3)
message_2 = "21" # (21) or (2, 1)
message_3 = "10" # (10)
message_4 = "14523" # (1, 4, 5, 2, 3) or (14, 5, 2, 3) or (14, 5, 23), or (1, 4, 5, 23)

print(decode_ways(message_1))
print(decode_ways(message_2))
print(decode_ways(message_3))
print(decode_ways(message_4))


# Dynamic Programming Bottom Up : Time O(n) / Space O(n)
def decode_ways(message):
    dp = [0 for i in range(len(message) + 1)]
    dp[0] = 1
    if message[0] == "0":
        return 0
    else:
        dp[1] = 1
    for i in range(2, len(message) + 1):
        if message[i - 1] == "0":
            if message[i - 2] == "1" or message[i - 2] == "2":
                dp[i] = dp[i - 2]
            else:
                return 0
        else:
            if message[i - 2] == "1" or message[i - 2] == "2" and int(message[i - 1]) < 7:
                dp[i] = dp[i - 2] + dp[i - 1]
            else:
                dp[i] += dp[i - 1]
    return dp[len(message)]



# Test
message_1 = "2263" # (2, 2, 6, 3) or (22, 6, 3) or (2, 26, 3)
message_2 = "21" # (21) or (2, 1)
message_3 = "10" # (10)
message_4 = "14523" # (1, 4, 5, 2, 3) or (14, 5, 2, 3) or (14, 5, 23), or (1, 4, 5, 23)

print(decode_ways(message_1))
print(decode_ways(message_2))
print(decode_ways(message_3))
print(decode_ways(message_4))


# Brute Force : Time Complexity 0(2^n) / Space Complexity O(n)
def decode_ways(message):
    if message.startswith("0"):
        return 0
    if len(message) <= 1:
        return 1

    total_ways = 0

    if int(message[:2]) <= 26:
        total_ways += decode_ways(message[2:])

    total_ways += decode_ways(message[1:])

    return total_ways


# Test
message_1 = "2263" # (2, 2, 6, 3) or (22, 6, 3) or (2, 26, 3)
message_2 = "21" # (21) or (2, 1)
message_3 = "10" # (10)
message_4 = "14523" # (1, 4, 5, 2, 3) or (14, 5, 2, 3) or (14, 5, 23), or (1, 4, 5, 23)

print(decode_ways(message_1))
print(decode_ways(message_2))
print(decode_ways(message_3))
print(decode_ways(message_4))
