with open('camelot.txt') as song:
    print(song.read(2))
    print(song.read(8))
    print(song.read())

print('\n')
print('readline \n')
camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)