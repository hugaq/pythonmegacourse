from difflib import get_close_matches
import json


def translate(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        return 'Did you mean {} instead?'.format(get_close_matches(word, dictionary.keys())[0])
    else:
        return 'This word doesn\'t exist in this dictionary.'


data = json.load(open('data.json'))
wort_to_look_ip = input('Please enter a word to look up:')
result = translate(wort_to_look_ip, data)

print('Definition of the word to be looked up:\n')
for i in range(len(result)):
    #n = i+1
    print(str(i+1)+':',result[i])
