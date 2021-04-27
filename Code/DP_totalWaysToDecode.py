# A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:

# "A":1, "B":2, "C":3 "D":4 ...

# Determine the total number of ways the message can be decoded

# DP Top Down
def decode_ways(message):
    dp = [-1 for i in range(len(message) + 1)]
    dp[0] = 1
    dp[1] = 0 if message[0] == "0" else 1

    for i in range(1, len(message)):
        one_digit = int(message[i])
        #print(one_digit)
        two_digit = int(message[i - 1] + message[i])
        #print(two_digit)
        if one_digit >= 1:
            dp[i] += dp[i - 1]
        if two_digit >= 10 and two_digit <= 26:
            dp[i] = dp[i - 2]
    #print(dp)
    return dp[-1]


# Test
# message_1 = "2263" # (2, 2, 6, 3) or (22, 6, 3) or (2, 26, 3)
# message_2 = "21" # (21) or (2, 1)
# message_3 = "10" # (10)
# message_4 = "14523" # (1, 4, 5, 2, 3) or (14, 5, 2, 3) or (14, 5, 23), or (1, 4, 5, 23)
#
# print(decode_ways(message_1))
# print(decode_ways(message_2))
# print(decode_ways(message_3))
# print(decode_ways(message_4))


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
