import string, random

plik = open('the_longest_txt_ever.txt', "w", encoding='utf-8')
v = ""
for i in range(1024):
    v += random.choice(string.ascii_letters)

i = 0
while True:
    i += 1
    plik.write(v)
    if (i%100 == 0):
        plik.seek
plik.close