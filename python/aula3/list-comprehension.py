# Quiz: Extraindo os primeiros nomes
# Use uma compreensao de listas para criar uma nova lista first_names, que contem apenas os primeiros nomes em names em letras minusculas.
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split(" ")[0] for name in names]
print(first_names)

#Quiz: Multiplos de tres
#Use uma compreensao de listas para criar uma lista multiples_3, contendo os 20 primeiros multiplos de 3.

multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)

#Quiz: Filtro de nomes por pontuacoes
#Use uma compreensao de lista para criar uma lista de nomes passed, que so incluem aqueles que marcaram pelo menos 65 pontos.

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name, score in scores.items() if score >= 65]
print(passed)