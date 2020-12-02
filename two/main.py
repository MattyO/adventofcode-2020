import collections
import re

def is_valid(item):
    result = re.search("(?P<min_count>[0-9]+)-(?P<max_count>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)", item)

    min_count , max_count = int(result.group('min_count')), int(result.group('max_count'))
    letter, password = result.group('letter'), result.group('password')

    password_counts = collections.Counter(password)

    return min_count <= password_counts[letter] <= max_count

def is_valid_two(item):
    result = re.search("(?P<index_one>[0-9]+)-(?P<index_two>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)", item)

    index_one, index_two= int(result.group('index_one')), int(result.group('index_two'))
    letter, password = result.group('letter'), result.group('password')

    return (password[int(index_one) - 1] == letter) ^ (password[int(index_two) - 1] == letter)
