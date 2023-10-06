students = {
1: {
'name': 'Bob',
'surname': 'Vazovski',
'age': 23,
'interests': ['biology, swimming']
},
2: {
'name': 'Rob',
'surname': 'Stepanov',
'age': 24,
'interests': ['math', 'computer games', 'running']
},
3: {
'name': 'Alexander',
'surname': 'Krug',
'age': 22,
'interests': ['languages', 'health food']
}
}
index=[]
age=[]
result_=[]
result__=[]
surnames=[]
for i in students:
    index.append(i)
    result__.append(students[i]['interests'])
    surnames.append(students[i]['surname'])
result___=[interests for _ in result__ for interests in _]
surnames_=[l_surname for __ in surnames for l_surname in __]
print('Общая длина всех фамилий студентов:', len(surnames_))
print('Полный список интересов всех студентов', result___)
for a in students.keys():
    age.append(students[i]['age'])
result=zip(index,age)
for res in result:
    result_.append(res)
print('Cписок пар «ID студента — возраст»:', result_)