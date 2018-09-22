#zip
letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

items = ["bananas", "mattresses", "dog kennels", "machine", "cheeses"]
weights = [15, 24, 42, 120, 5]

combined = list(zip(items, weights))
print(combined)

items_new , weights_new = zip(*combined)
print(items_new)
print(weights_new)

#enumerate
print("without enumerate")
for i, item in zip(range(len(items)), items):
    print(i, item)
print("with enumerate")
for i, item in enumerate(items):
    print(i, item)

print('question_1')

# Use zip para gravar um loop for que cria uma string especificando o rotulo e 
# as coordenadas de cada ponto e acrescenta a lista points. 
# Cada string deve ser formatada como label: x, y, z. 
# Por exemplo, a string para a primeira coordenada deve ser F: 23, 677, 4.
#

x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here

for label, x,y,z in zip(labels, x_coord,y_coord,z_coord):
    points.append("{}: {}, {}, {}".format(label,x,y,z))


for point in points:
    print(point)

print("quiz - 2")
#Use zip para criar um dicionario cast que usa names como chave e heights como valores.

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))
print(cast)

#Descompacte a tupla cast em duas tuplas, names e heights.


cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# define names and heights here
names, heights = zip(*cast)

print(names)
print(heights)

print("quiz 3")

#Use zip para transpor data de uma matriz 4 por 3 para uma matriz 3 por 4
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))
print(data_transpose)

print("quiz 4")
#Use enumerate para modificar a lista cast para que cada elemento contenha o nome seguido da altura correspondente do personagem. Por exemplo, o primeiro elemento de cast deve mudar de "Barney Stinson" para "Barney Stinson 72".

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)