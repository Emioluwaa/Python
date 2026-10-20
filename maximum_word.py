def finding_max(words):
    longest = max(words, key = len)
    return longest, len(longest)


word = ('welcome', 'out', 'weather', 'mobile', 'breakfast', 'journey')
print(finding_max(word))

      





