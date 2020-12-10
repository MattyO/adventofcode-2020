from itertools import tee, groupby
import functools
import collections
import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def voltage_difference(adapter_list):

    adapter_list = sorted([0] + list(adapter_list))
    return sum(map(lambda t: t[1] - t[0], pairwise(adapter_list))) + 3

def arangements(adapter_list):
    adapter_list = sorted(list(adapter_list) + [0])
    groups_of_one = []
    memo = []
    differences = list(map(lambda t: t[1] - t[0], pairwise(adapter_list)))
    groups_of_one  = functools.reduce(lambda x,y: str(x)+str(y),  [str(d) for d in differences]).split("3")
    max_group_length = max([len(g) for g in groups_of_one])
    perms = {**{0: 0, 1:0}, **{2: 2, 3: 4, 4: 7}}
    return functools.reduce(lambda x, y: x * y, filter(lambda i: i > 0, map(lambda g: perms[len(g)], groups_of_one)))

