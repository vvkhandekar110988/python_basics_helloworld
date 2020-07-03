'''
message = input(">")
words = message.split(' ')
emojis = {
    ":)": ""
}
output = ""
for word in words:m
    output = emojis.get(word, word)
print(output)
'''
import emoji
print(emoji.emojize('Python is :smiling_imp:', use_aliases=True))
