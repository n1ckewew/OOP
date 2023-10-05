w=input('Введите предложение')
def longest_word(string):
    words=string.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest = word
    return longest
string=w
print(longest_word(string))