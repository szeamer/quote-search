import re

#extract all the quotes from a file

def extract_quotes(filepath):
    filetext = open(filepath, 'r').read()
    print(filetext)
    quotelist = re.findall('“(.*)”', filetext)
    for quote in quotelist:
        print('"'+quote+'"')
    with open("harrypotterquotes.txt", "w") as f:
        for quote in quotelist:
            f.write('"'+quote+'"\n')

extract_quotes("harrypotter.txt")
