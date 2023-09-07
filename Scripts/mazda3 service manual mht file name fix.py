# I don't remember where I found this along with an MHTML rip of the Mazda service manual, but thank you!

import pathlib

start = pathlib.Path('2019 Mazda3 Service Manual')

for file in start.glob('**\\**\\**\\*-*-*.mht'):
    with file.open("rb") as r:
        insides = r.read().decode('ascii', 'ignore')
    start = insides.index('<h3')
    start += insides[start:].index('>') + 1
    substr = insides[start:]
    substr = substr[:substr.index('<')]
    newname = substr.replace('=', '').replace('\r\n', '').replace('))', ')')
    newpath = file.parent / (newname.replace('/', '+').replace(':', '') + '.mht')
    print(file, newpath)
    try:
        file.replace(newpath)
    except Exception as e:
        print(e)