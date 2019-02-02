from difflib import get_close_matches
import json


def translate(word, dictionary):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif len(get_close_matches(word, dictionary.keys())) > 0:
        choice = input('Did you mean {} instead?\n'.format(get_close_matches(word, dictionary.keys())[0]))
        if choice == 'yes':
            return translate(get_close_matches(word, dictionary.keys())[0], dictionary)
        else:
            return 'Sorry, try again.'
    else:
        return 'This word doesn\'t exist in this dictionary.'


data = json.load(open('data.json'))
wort_to_look_ip = input('Please enter a word to look up:')
result = translate(wort_to_look_ip, data)

if result[0] == 'D' or result[0] == 'T':
    print(''.join(result))
else:
    print('\n\nDefinition of',wort_to_look_ip,':\n')
    for i in range(len(result)):
        print(str(i+1)+':',result[i])
