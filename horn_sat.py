import sys
import re
def satisfability(expression):
    expression = expression.split(') and (')
    expression = [exp.replace('(', '').replace(')', '') for exp in expression]
    implicaciones = set()
    negativas = set()
    for exp in expression:
        if 'not' in exp:
            nega = tuple(exp.split(' or '))
            nega = tuple([neg.split('not ')[1] for neg in nega])
            negativas.add(nega)
        if 'si' in exp:
            impli = (exp.split(' and')[0], exp.split('and ')[1].split(' si')[0],
                        exp.split(' si ' )[1])
            implicaciones.add(impli)

    print("Implicaciones:", implicaciones, "\nNegativas:", negativas)

for line in sys.stdin:
    line = line.rstrip()
    satisfability(line)
