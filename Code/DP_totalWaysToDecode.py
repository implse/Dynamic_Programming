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
    ways = 0

    def helper_decode(message, position):
        # Base case
        if position == 0:
            if message[position] == "0":
                return 0
            else:
                return 1
        if position == -1:
            return 1

        # Recursive Part
        # Case 1 : message = "10" or "20"
        if message[position] == "0":
            if message[position - 1] in ["1", "2"]:
                return helper_decode(message, position - 2)
            else:
                return 0 # message == "0"
        # Case 2 : message range from "11" to "19" and "21" to "26"
        if message[position - 1] == "1" or (message[position - 1] == "2" and int(message[position]) < 7):
            ways = helper_decode(message, position - 1) + helper_decode(message, position - 2)
        else:
            ways = helper_decode(message, position - 1) # message range from "1" to "9"
        return ways

    return helper_decode(message, len(message) - 1)

"""
# Test
message_1 = "2263" # (2, 2, 6, 3) or (22, 6, 3) or (2, 26, 3)
message_2 = "21" # (21) or (2, 1)
message_3 = "10" # (10)
message_4 = "14523" # (1, 4, 5, 2, 3) or (14, 5, 2, 3) or (14, 5, 23), or (1, 4, 5, 23)

print(decode_ways(message_1))
print(decode_ways(message_2))
print(decode_ways(message_3))
print(decode_ways(message_4))
"""
