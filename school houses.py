#school houses
#anton
#25/06/24
teachers = ['Mrs Clark and Mrs Coates', 'Mr Cowie and Mrs Watson', 'Mr Filler and Mrs Reid', 'Mr Jamieson and Miss Maddox']
name = input('enter your name')

house = input('enter your school house')
while not house == 'Blackfriars' or 'Collyhill' or 'Sillerton' or 'Straloch':
    print('Invalid house')
    house = input('enter your school house')

if house == 'Blackfriars':
    print('Hello', name,', your house is', house,' and you guidance teachers are', teachers[0],)
elif house == 'Collyhill':
    print('Hello', name,', your house is', house,' and you guidance teachers are', teachers[1],)
elif house == 'Sillerton':
    print('Hello', name,', your house is', house,' and you guidance teachers are', teachers[2],)
else:
    print('Hello', name,', your house is', house,' and you guidance teachers are', teachers[3],)
