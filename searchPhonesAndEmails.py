import re, pyperclip

phoneRegex = re.compile(r'''(
(\d{2}|\+\d{2}|\(\d{2}\)|\+\(\d{2}\))?
(0)
(\s|-|\.)?
(50|66|95|99|67|68|96|97|98|63|93|73|77|32|33|\(\d{2}\))
(\s|-|\.)?
(\d{3})
(\s|-|\.)?
(\d{2})
(\s|-|\.)?
(\d{2})
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '38'+"".join([groups[2],groups[4],groups[6],groups[8],groups[10]])
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопійовано в буфер обміну:')
    print('\n'.join(matches))
else:
    print('Телефоннні номери та електронні адреси не знайдені!')
