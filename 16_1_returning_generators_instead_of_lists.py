def index_words(text):
    if text:
        yield 0

    for index, char in enumerate(text):
        if char == ' ':
            yield index + 1


g = index_words('foo bar stupid peter')
for letter in g:
    print(letter)

