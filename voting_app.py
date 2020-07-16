# Instructions
# Enter number of candidates: 2
# Enter 2 candidates now:
# Nicolas David
# Candidates are: ['Nicolas', 'David']
# Voting is live... please wate for the results...
# voting has been finishen... and wait over
# here are the results
# Nicolas : 22
# David : 67
# The winner is ...
# David : 67

import random

num = int(input('Enter number of candidates: '))
cand = input(f'Enter {num} candidates now:\n').split()
print('Candidates are:', cand)
print('Voting is live... please wate for the results...')
print('voting has been finishen... and wait over')
print('here are the results')
votes = []
for x in range(0, num):
    c = random.randrange(1, 100, 3)
    votes.append(c)

for i in range(num):
    print(cand[i], ':', votes[i])
print('The winner is ...')

maximum = max(votes)
count = 0
for r in range(num):
    if votes[r] == maximum:
        count = r
print(cand[count], ':', maximum)
