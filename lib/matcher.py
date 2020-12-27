import copy
import re
import collections

def Struct(**kwargs):
    return collections.namedtuple('Struct', ' '.join(kwargs.keys()))(**kwargs)

def match(pattern, string):
    match_types = {
        'int':      ('[0-9]+',      lambda i: int(i)),
        'string':   ('[a-zA-Z]+',   lambda i: i),
        'alpha':    ('[0-9a-z]+',   lambda i: i),
        'slug':     ('[0-9a-z\-]+', lambda i: i),
    }
    regex_pattern = copy.copy(pattern)
    groups = [ m for m in re.findall("<.*?>", pattern)]
    group_info = []
    for group in groups:
        group_name, group_type = group.split(":")
        group_name, group_type = group_name[1:], group_type[:-1]

        group_info.append((group_name, match_types.get(group_type, (group_type, lambda x: x))))

        new_regex = match_types.get(group_type, (group_type,))[0]
        regex_pattern = regex_pattern.replace(group, f'(?P<{group_name}>{new_regex})', 1)

    result = re.search(regex_pattern, string)
    if result is None:
        return Struct(**{ 'is_match': False, 'pattern': regex_pattern})

    result_hash =  { name: converter(result.group(name)) for name, (p, converter) in group_info  }
    result_hash['is_match'] = True

    return Struct(**result_hash)
