vstup = 'maturujeme v pythone'
key = 'abc'
#potrebujem novy kluc
new_key = key*(len(vstup)//len(key)) + key[:len(vstup)%len(key):]
print(len(new_key), len(vstup))
vystup = ''
for i in range (len(vstup)):
    #ak to co idem sifrovat je v malej anglickej abecede pokracuj
    if 97 <= ord(vstup[i]) and ord(vstup[i]) <= 122:
        posun = ord(new_key[i]) - 96
        # vstup[i] idem posunut o posun
        vystup += chr(((ord(vstup[i]) - 97 + posun) % 26 + 97))
    else:
        vystup += vstup[i]

print(vystup)