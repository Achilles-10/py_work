# 3.2
persons = ['Kobe Bryant','Steve Jobs','Jacky cheung']
print('\n' + persons[0] + ', ' + persons[1] +' and '+ persons[-1] + ', I sincerely invite you to join me.')
print(persons[0] + ": 'Sorry, I'm affraid that I can't be there.'")

persons[0] = 'Achilles Nancy'
print('\n' + persons[0] + ', ' + persons[1] + ' and '+ persons[-1] + ', I sincerely invite you to join me.')

print("\nGood news: I've find a bigger table.")
persons.insert(0,'Liase')
persons.insert(2,'Jason')
persons.append('Turning')
print(persons[0] + ', ' + persons[1] + ', ' + persons[2] +', ' + persons[-3] + ', ' + persons[-2] + ' and ' + persons[-1] +', I sincerely invite you to join me.')

print("\nBad news: I can only invite two of you.")
print(persons.pop() + ", I'm sorry.")
print(persons.pop() + ", I'm sorry.")
print(persons.pop() + ", I'm sorry.")
print(persons.pop() + ", I'm sorry.")

print('\n' + persons[0] + ', please remember to arrive on time.')
print(persons[1] + ', please remember to arrive on time.')

del persons[0],persons[0]
print(persons)
