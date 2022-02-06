from typing import List
from collections import defaultdict

from test_framework import generic_test, test_utils

''' Still iterating:
This can be solved by looping a max of 4 times per recursive call. 
'''
def phone_mnemonic(phone_number: str) -> List[str]:
    num_to_letters = load_letter_mapping()
    return phone_mnemonic_helper(phone_number, num_to_letters)

def phone_mnemonic_helper(phone_number, num_to_letters) -> List[str]:
    if len(phone_number) == 1:
        return num_to_letters[phone_number] # empty list in some cases
    result = []
    front_letters = num_to_letters[phone_number[0]]
    downstream_mnemonics = phone_mnemonic_helper(phone_number[1:], num_to_letters)
    for front in front_letters:
        for downstream in downstream_mnemonics:
            result.append(front + downstream)
    return result
    

def load_letter_mapping():
    num_to_letters = defaultdict(list)
    num_to_letters["0"] = ["0"]
    num_to_letters["1"] = ["1"]
    num_to_letters["2"] = ["A", "B", "C"]
    num_to_letters["3"] = ["D", "E", "F"]
    num_to_letters["4"] = ["G", "H", "I"]
    num_to_letters["5"] = ["J", "K", "L"]
    num_to_letters["6"] = ["M", "N", "O"]
    num_to_letters["7"] = ["P", "Q", "R", "S"]
    num_to_letters["8"] = ["T", "U", "V"]
    num_to_letters["9"] = ["W", "X", "Y", "Z"]
    return num_to_letters

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'phone_number_mnemonic.py',
            'phone_number_mnemonic.tsv',
            phone_mnemonic,
            comparator=test_utils.unordered_compare))
