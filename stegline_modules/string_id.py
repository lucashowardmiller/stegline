import re
from typing import List

"""Used to id common ctf strings"""

# foo{bar}
generic_flag_brackets = re.compile('.*{.*}')
# SKY-STEG-1234
sky_flag_format = re.compile('[NCLSKYnclsky]{3}-[a-zA-Z]{4}-[0-9]{4}')
# flag-foo
flag_generic = re.compile('[FLAGflag]{4}-.*')


def return_ctf_flags(strings: List) -> List:
    """Takes a list of strings and returns a list of unique strings that match a regex for strings"""
    flag_regex_list = [generic_flag_brackets, sky_flag_format, flag_generic]
    matched_strings = []
    for item in strings:
        for regex in flag_regex_list:
            matched_strings.extend(re.findall(regex, item))

    # conversion between list and set eliminates duplicates
    return list(set(matched_strings))
