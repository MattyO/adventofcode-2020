import collections

def is_valid(item):
    policy, password = item.split(":")
    count, letter = policy.split(" ")
    min_count, max_count = count.split("-")

    password_counts = collections.Counter(password)

    return int(min_count) <= password_counts[letter] <= int(max_count)

def is_valid_two(item):
    policy, password = item.split(":")
    count, letter = policy.split(" ")
    index_one, index_two = count.split("-")

    password = password.strip()

    return (password[int(index_one) - 1] == letter) ^ (password[int(index_two) - 1] == letter)
