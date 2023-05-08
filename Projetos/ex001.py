## QUESTÃO 1
L1 = list("Guilherme")
L2 = list("Sebastião")
L3 = list("Guilherme Sebastião")

## QUESTÃO 2
C1 = set(L1)
C2 = set(L2)
C3 = set(L3)

## QUESTÃO 3 e 4
COMP1 = len(L1), len(C1)
COMP2 = len(L2), len(C2)
COMP3 = len(L3),len(C3)

## QUESTÃO 5
## Comp1 são diferente pois o nome Guilherme repete a letra 'e' e no set age igual um conjunto ele remove duplicatas, para isso ele remove as letras repetidas ##
## Comp2 são iguais porque Sebastião não repete nenhuma letra todas são diferentes logo seu conjunto igual ##
## Comp 3 são diferentes pois o conjunto C3 remove as letras repetidas ##

## QUESTÃO 6 
LisUniao = len(L1 + L2)

## QUESTÃO 7
ConjUniao = len(C1 | C2)

## QUESTÃO 8
LisInter = set(L1) & set(L2)

## QUESTÃO 9
ConjInter = C1 & C2

## QUESTÃO 10
L4 = list("Matilde")
L5 = list("Bruzon")

C4 = set(L4)
C5 = set(L5)

LisUniao2 = len(L4 + L5)

ConjUniao2 = len(C4 | C5)