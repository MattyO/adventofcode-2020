from pprint import pprint
import functools
import re

def parse(filename):
    with open(filename) as f:
        lines = f.readlines()

    nodes = []
    for line in lines:
        result = re.search("(?P<parent_bag>[\w\s]+) bags contain (?P<children_bags>[0-9\w\s,]+)\.", line)
        parent_bag = result.group("parent_bag")
        children_bag_string = result.group('children_bags')
        children_bags = []

        if children_bag_string != 'no other bags':
            for bag_string in children_bag_string.split(","):
                cr = re.search("(?P<num>[0-9]+) (?P<bag_name>[\w\s]+) bag", bag_string)
                children_bags.append((cr.group('bag_name'), cr.group('num')))

        nodes.append((parent_bag, children_bags))

    return nodes


def get_child_names(node):
    return list(map(lambda c: c[0], node[1]))

def get_nodes_with_children(nodes, child_name):
    return list(filter(lambda node: child_name in get_child_names(node), nodes))


def get_node(nodes, name):
    return next(filter(lambda n: n[0] == name, nodes))

def get_parents(nodes, name):
    parent_nodes = get_nodes_with_children(nodes, name)
    if parent_nodes == []:
        return []

    return [pn[0] for pn in parent_nodes] + list(functools.reduce(lambda x, y: x+y, [get_parents(nodes, pnode[0]) for pnode in parent_nodes]))

def count_children(nodes, name):
    node = get_node(nodes, name)
    #print(node)
    return sum(int(c[1]) for c in node[1]) + sum(int(c[1]) * count_children(nodes, c[0]) for c in node[1])
