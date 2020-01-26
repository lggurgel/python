import requests

while True:
    word = input('search: ')

    if word == '-1':
        break

    d = {'rel_syn':word}

    r = requests.get('https://api.datamuse.com/words', params=d)

    response = r.json()

    for w in response:
        print(w['word'])

    print('\n')