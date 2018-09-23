#functions.

def cylinder_volume(height, radius):
    pi = 3.14159
    return height * pi * radius ** 2

# this prints something, but does not return anything
def show_plus_ten(num):
    print(num + 10)

# this returns something
def add_ten(num):
    return(num + 10)

print('Calling show_plus_ten...')
return_value_1 = show_plus_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_1))

print('\nCalling add_ten...')
return_value_2 = add_ten(5)
print('Done calling')
print('This function returned: {}'.format(return_value_2))

def cylinder_volume(height, radius=5):
    pi = 3.14159
    return height * pi * radius ** 2

print(cylinder_volume(10, 7))  # pass in arguments by position
print(cylinder_volume(height=10, radius=7))  # pass in arguments by name

# Quiz: Funcao de densidade populacional
# Escreva uma funcao chamada population_density que aceita dois argumentos, population e land_area, 
# e devolve uma densidade populacional calculada a partir desses valores. 
# Eu inclui dois casos de teste que voce pode usar para verificar se sua funcao funciona corretamente. 
# Uma vez que voce ja escreveu sua funcao, use o botao de execucao de teste para testar seu codigo.


# write your function here


def population_density(population, land_area):
  return population / land_area

# test cases for your function
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}, actual result: {}".format(expected_result2, test2))


# Quiz: readable_timedelta
# Escreva uma funcao chamada readable_timedelta que receba um argumento, um numero inteiro days, 
# e devolva uma string que diz quantas semanas e dias esse numero representa. 
# Por exemplo, readable_timedelta(10) deve devolver, "1 week(s) and 3 day(s)."

# write your function here
def readable_timedelta(days):
  """
  Print the number of weeks and days in a number of days.

  Parameters:
  days -- number of days to convert (int)

  Returns:
  string of the number of weeks and days included in days
  """
  weeks = 0
  resting_days = 0
  if days < 7:
    resting_days = days
  else:
    weeks = days / 7
    resting_days = days % 7
  return "{} week(s) and {} day(s).".format(int(weeks), resting_days)

# test your function
#print(readable_timedelta(10))
#print(readable_timedelta(1)) #0 week(s) and 1 day(s).
#print(readable_timedelta(7)) #1 week(s) and 0 day(s).
print(readable_timedelta(9)) #1 week(s) and 2 day(s).
#print(readable_timedelta(6839)) #977 week(s) and 0 day(s).

#solution

def readable_timedelta2(days):
    # use integer division to get the number of weeks
    weeks = days // 7
    # use % to get the number of days that remain
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)

print(readable_timedelta2(20))

#lambda


def multiply(x, y):
    return x * y

print(multiply(4, 7))

multiply = lambda x, y: x * y


print(multiply(4, 7))


numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)
    

averages = list(map(mean, numbers))
print(averages)

numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

mean2 = lambda x : sum (x)  / len(x)

averages = list(map(mean2, numbers))
print(averages)


cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

#def is_short(name):
#    return len(name) < 10
    
is_short = lambda name : len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

#Iteradores E Geradores
#
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

#Quiz: Chunker
#Se voce tem um iteravel que e grande demais para caber na memoria por completo 
# (ex. ao lidar com arquivos grandes), ser capaz de pegar e utilizar apenas pedacos a cada vez pode ser muito valioso.
#Implemente uma funcao de gerador, chunker, que recebe um iteravel e retorna um pedaco de tamanho especifico por vez.
#Recorrendo a funcao assim:

def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))


# Gerador de expressoes
# Aqui esta um conceito legal que combina geradores e compreensao de listas! 
# Na verdade, voce pode criar um gerador da mesma maneira que normalmente escreveria uma compreensao da lista, 
# utilizando parenteses em vez de colchetes. Por exemplo:

sq_list = [x**2 for x in range(10)]  # isto produz uma lista de quadrados

sq_iterator = (x**2 for x in range(10))  # isto produz um iterador de quadrados

#Isso pode ajuda-lo a economizar tempo e criar um codigo eficiente!