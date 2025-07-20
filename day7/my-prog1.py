# new_words = [(word, i) for i, word in enumerate(words)]
# print(new_words)
# new_words = [(sorted(word[0]), word[1]) for word in new_words]
# new_words = sorted(new_words, key=lambda x: x[0])
# print(new_words)
# for word in new_words:
#     print(words[word[1]])

# eat tea tan ate nat bat


words = list(input().split())
res = {}
for word in words:
    key = ''.join(sorted(word))
    if key in res:
        res[key].append(word)
    else:
        res[key] = [word]
print(*res.values())
