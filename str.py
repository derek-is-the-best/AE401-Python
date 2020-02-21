letters='0123456789'
print(letters[5])
print(letters[-2])
print(letters[1:6])
print(letters[9:])
print(letters[:9])
print(letters[-3:])
print(letters[1:8:3])
print(letters[::3])

letters='i Am THe bEsT'
print(letters.capitalize()) 
print(letters.title())
print(letters.upper())
print(letters.lower())
print(letters.swapcase()) 


string = 'hahahahaha heyheyheyheyhey hohohoho hihihihihihi'
print(string.split())
print(string.split('h'))
print(string.split('i',1))

string = '  eopoopopop  '
print(string.strip())
print(string.lstrip()) 
print(string.rstrip()) 
print (string.strip(' 0'))

string = "hahaha"
sub="i"
print(string.count(sub))

string = 'this is a dog'
print(string.replace('is', 'was'))
print(string.replace('is', 'was',1))
