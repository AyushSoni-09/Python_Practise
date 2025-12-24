def groupAnagram(words):
    group={}

    for word in words:
        key=''.join(sorted(word))

        if key not in group:
            group[key] =[]

        group[key].append(word)

    return list(group.values())

words=["eat" , "tea" , "tan" , "ate", "nat" , "bat"]
print(groupAnagram(words))
