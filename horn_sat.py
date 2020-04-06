import sys
import re
def satisfability(expression):
    implicaciones, negativas = lectura(expression)

    # Paso 1
    verdaderos, falsos = inicializar(implicaciones, negativas)

    # Paso 2
    for implicacion in implicaciones:
        verdaderos, falsos = implicacionSatisfacible(implicacion,
                                                            verdaderos, falsos)

        # Verificando si la las implicaciones ya son todas verdaderas
    for implicacion in implicaciones:
        if not implicacionSatisfacible(implicacion, verdaderos, falsos):
            print("\nLa fórmula no es satisfacible")
            return

    for negativa in negativas:
        if not negativaSatisfacible(negativa, falsos):
            print("\nLa fórmula no es satisfacible")
            return

    print("\n\nVerdaderos:", verdaderos, "\nFalsos:", falsos)

def implicacionSatisfacible(implicacion, verdaderos, falsos, verificacion = False):
    '''
    Se cambia a verdadero el lado derecho de la implicación en caso de que la
    implicación sea falsa
    '''
    satisfacible = True
    for literal in implicacion[:-1]:
        satisfacible = satisfacible and literal in verdaderos
    satisfacible = not satisfacible
    satisfacible = satisfacible or implicacion[-1] in verdaderos
    if not verificacion: # sirve para la primera vez que se cambia cada literal
        if not satisfacible:
            falsos.remove(implicacion[-1])
            verdaderos.add(implicacion[-1])
        return verdaderos, falsos
    return satisfacible # en caso de que esté en modo verificación para saber
                        # si se puede avanzar al siguiente paso


def negativaSatisfacible(negativa, falsos):
    satisfacible = False
    for variable in negativa:
        satisfacible = satisfacible or variable in falsos
    return satisfacible

def inicializar(implicaciones, negativas):
    '''
    Como primer paso, todos los literales son falsos
    '''
    verdaderos = set()
    falsos = set()
    for clausula in implicaciones:
        for variable in clausula:
            falsos.add(variable)
    for clausula in negativas:
        for variable in clausula:
            falsos.add(variable)
    return verdaderos, falsos

def lectura(expression):
    '''
    Se una línea del archivo de texto input_horn_sat.txt y se convierte en
    variables manejables con este código
    '''
    expression = expression.split(') and (')
    expression = [exp.replace('(', '').replace(')', '') for exp in expression]
    implicaciones = []
    negativas = []
    for exp in expression:
        if 'not' in exp:
            nega = tuple(exp.split(' or '))
            nega = tuple([neg.split('not ')[1] for neg in nega])
            negativas.append(nega)
        elif 'si' in exp:
            impli = [a for a in exp.split(' and ')]
            if len(exp.split(' si ')) == 2:
                impli[-1] = impli[-1].split(' si ')[0]
                impli.append(exp.split(' si ')[1])
            else:
                impli[-1] = exp.split('si ')[-1]
            impli = tuple(impli)
            implicaciones.append(impli)
    implicaciones.sort(key = len)
    return implicaciones, negativas

for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    print("\nTEST #", i+1, "\n\n"+line)
    satisfability(line)
    print("------------------------\n")
