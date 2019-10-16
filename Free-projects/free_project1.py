from random import choice

subjects = ['COUNT', 'STRANGER', 'LOOK', 'CHURCH', 'CASTLE', 'PICTURE',
            'EYE', 'VILLAGE', 'TOWER', 'FARMER', 'WAY', 'GUEST', 'DAY',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['CLOSED', 'SILENT', 'STRONG', 'GOOD', 'NARROW', 'NEAR',
              'NEW', 'QUIET', 'FAR', 'DEEP', 'LATE', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ALSO ', 'WHETHER ', ' NOR ', ' BUT ', ' IF ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase(subjects):
    text = choice(operators) + ' predicates ' + choice(subjects)
    if text == 'A EYE':
        text = 'AN EYE'
    return text + 'IS'

print('')
print(phrase(subjects) + choice(predicates) + choice(conjunctions) +
       phrase(operators) + choice(predicates) + '.')
print('')
