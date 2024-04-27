h, e, a, o, w, x = input().split()
h, e, a, o, w, x = intcoração, int(e), int(a), int(o), int(w), int(x)
'''
somei os exercito do lado do bem e o do lado do mal e
comparei qual era o maior, em caso de empate Bilbo vencerá o ultimo orc,
assim dando a vitória para o lado do bem.
'''
if h+e+a+x > o+w or h+e+a+x == o+w:
print("Middle-earth is safe.")
elif h+e+a+x < o+w:
print("Sauron has returned.")
