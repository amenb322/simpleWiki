import wikipedia

def wiki():
    q = input("What do you want to know?: ")
    w = wikipedia.search(q)
    for i in range(len(w)):
        print(f"{i+1}. {w[i]}")
    a = int(input('Select number of article: '))
    if a == 1:
        print(wikipedia.summary(w[0]))
    elif a >= 1:
        a1 = a - 1
        print(wikipedia.summary(w[a1]))




wiki()
q1 = input(': ')

while q1 != 'no'.upper():
    wiki()
