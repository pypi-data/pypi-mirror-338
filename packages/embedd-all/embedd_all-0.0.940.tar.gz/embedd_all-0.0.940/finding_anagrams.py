from typing import List, Dict
from collections import Counter, defaultdict

# Function to get a canonical form of a word
def canonical(word: str) -> str:
    return ''.join(sorted(word.replace(' ', '').lower()))

 # Function to find all anagrams using backtracking
def find_anagrams(dictionary_words: List[str], phrase_counter, current_anagram, start):
    if all(count == 0 for count in phrase_counter.values()):
        return [current_anagram[:]]
        
    anagrams = []
    for word in dictionary_words:
        word_count = Counter(word.lower())
        if all(phrase_counter[ch] >= word_count[ch] for ch in word_count):
                # Choose the word, add to the current set
            current_anagram.append(word)
                # Decrease the counts
            phrase_counter.subtract(word_count)
                # Explore further
            anagrams.extend(find_anagrams(dictionary_words, phrase_counter, current_anagram, start + 1))
                # Backtrack
            phrase_counter.update(word_count)
            current_anagram.pop()
        
    return anagrams

def solve(input: str) -> Dict[str, List[List[str]]]:
    sections = input.split('#')
    # Extract dictionary terms and phrases
    dictionary_words = sections[0].strip().split()
    phrases = sections[1].strip().split('\n')

    

    # Create a map of words by their canonical form
    word_dict = defaultdict(list)
    for word in dictionary_words:
        canonical_form = canonical(word)
        word_dict[canonical_form].append(word)

    result = {}
    for phrase in phrases:
        phrase = phrase.strip()
        if not phrase:
            continue
        phrase_counter = Counter(canonical(phrase).lower())
        anagrams = find_anagrams(dictionary_words, phrase_counter, [], 0)
        
        if anagrams:
            result[phrase] = anagrams
    
    return result


#Code Testing
import pytest


def strip_lines(s: str) -> str:
    return "\n".join(line.strip() for line in s.splitlines())


# List of test cases in the form [(input, output)]
TEST_CASES = [
    (
        strip_lines(
            """AWHILE
            REALISM
            SPEAK
            #
            WILLIAM SHAKESPEARE
            #"""
        ),
        {
            "WILLIAM SHAKESPEARE": [
                ["AWHILE", "REALISM", "SPEAK"],
                ["AWHILE", "SPEAK", "REALISM"],
                ["REALISM", "AWHILE", "SPEAK"],
                ["REALISM", "SPEAK", "AWHILE"],
                ["SPEAK", "AWHILE", "REALISM"],
                ["SPEAK", "REALISM", "AWHILE"],
            ],
        },
    ),
    (
        strip_lines(
            """ABC
            AND
            DEF
            DXZ
            K
            KX
            LJSRT
            LT
            PT
            PTYYWQ
            Y
            YWJSRQ
            ZD
            ZZXY
            #
            XK XYZZ Y
            #"""
        ),
        {
            "XK XYZZ Y": [
                ["KX", "Y", "ZZXY"],
                ["KX", "ZZXY", "Y"],
                ["Y", "KX", "ZZXY"],
                ["Y", "ZZXY", "KX"],
                ["ZZXY", "KX", "Y"],
                ["ZZXY", "Y", "KX"],
            ],
        },
    ),
]


@pytest.mark.parametrize("input,expected", TEST_CASES)
def test_solver(input, expected):
    results = solve(input)
    results_sorted = {phrase: sorted(anagrams) for phrase, anagrams in results.items()}
    assert results_sorted == expected


#Question
# It is often fun to see if rearranging the letters of a name gives an amusing anagram. For example, the letters of 'WILLIAM SHAKESPEARE' rearrange to form 'SPEAK REALISM AWHILE'.
# Write a program that will read in a dictionary and a list of phrases and determine which words from the dictionary, if any, form anagrams of the given phrases. Your program must find all sets of words in the dictionary which can be formed from the letters in each phrase (ignoring spaces). Each word from the dictionary can only be used once.
# The signature of your function should be:
# def solve(input: str) -> Dict[str, List[List[str]]]
# You may implement other functions called by your solve function if you wish.
# Input Spec
# Input will consist of two parts. The first part is the dictionary in alphabetical order, the second part is the set of phrases for which you need to find anagrams.
# Each part of the file will be terminated by a line consisting of a single '#'.
# Output Spec
# The output should be a map that contains a key for each of the specified phrases, mapped to a list of possible anagrams (order doesn't matter). If there are no anagrams for a particular phrase, don't include an entry for that phrase in the map.
# Each possible anagram is represented as a list of strings.
# Sample Input & Output
# Input:
# """IS THIS SPARTA # ATRAPS ATRAPS SI THIS IS SPARTA #"""
# Output:
# { "ATRAPS": [["SPARTA"]], "ATRAPS SI": [["IS", "SPARTA"], ["SPARTA", "IS"]], "THIS IS SPARTA": [ ["IS", "SPARTA", "THIS"], ["IS", "THIS", "SPARTA"], ["SPARTA", "IS", "THIS"], ["SPARTA", "THIS", "IS"], ["THIS", "IS", "SPARTA"], ["THIS", "SPARTA", "IS"], ] }


# Sample code to complete: Make sure to import all the packages you are using
# from typing import Dict, List


# def solve(input: str) -> Dict[str, List[List[str]]]:
#   return {}
