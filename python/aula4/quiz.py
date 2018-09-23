names =  list(input('Enter names separared by commas: ').split(','))
assignments = list(input('Enter assignment counts separared by commas: ').split(','))
grades = list(input('Enter grades separared by commas: ').split(','))

print(names)
print(assignments)
print(grades)

# string de mensagem a ser usada para cada aluno
# DICA: use .format() com esta string no seu loop for

for name, assignment, grade in zip(names, assignments, grades):
    potencial =  int(grade) + int(assignment) * 2
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to submit before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n".format(name, assignment, grade, potencial)
    print(message)

# escreva um loop for que realize uma iteração em cada conjunto de nomes, tarefas e notas para imprimir a mensagem de cada aluno