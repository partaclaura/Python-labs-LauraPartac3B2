# The validate_dict function that receives as a parameter a set of tuples
# ( that represents validation rules for a dictionary that has strings as keys and values)
# and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value
# (not at the beginning or end) and ends with "suffix". The function will return True if the given dictionary
# matches all the rules, False otherwise.
#
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
# and d= {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
# => False because although the rules are respected for "key1" and "key2" "key3" that does not appear in the rules.

def validate_dict(s, d):
    for set_rule in s:
        if len(set_rule) < 4:
            return "Rule missing"
        if set_rule[0] in d.keys():
            words = d[set_rule[0]].split()
            if set_rule[1] != "" and words[0] != set_rule[1]:
                return False
            if set_rule[2] != "" and set_rule[2] not in words:
                return False
            if set_rule[3] != "" and words[len(words) - 1] != set_rule[3]:
                return False
        else:
            return False
    return True


in_set = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
in_dict = {"key1": "come inside , it's too cold out", "key3": "whatever"}
print(validate_dict(in_set, in_dict))
