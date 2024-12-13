languages = ['Python','Python', 'SQL', 'Java', 'C++', 'Javascript']
if 'Java' in languages:
    languages.remove('Java')
if 'Swift' in languages:
    languages.remove('Swift')
print(languages)
languages.pop()
temp = languages.pop(1)
print(temp)
languages.append(temp)
print(languages)
del languages[0]
languages.clear()
print(languages)