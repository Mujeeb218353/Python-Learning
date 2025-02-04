name = "Mujeeb Ur Rahman"

print("Length of name:", len(name))
print("Name in upper case:", name.upper())
print("Name in lower case:", name.lower())
print("Is name all upper case?:", name.isupper())
print("Is name all lower case?:", name.islower())
print("Name in capital case:", name.capitalize())
print("Name in title case:", name.title())
print("Count of 'a' in name (case sensitive):", name.count('a'))
print("Index of 'R' in name:", name.index('R'))
print("Replace 'Mujeeb' with 'Ahmed':", name.replace('Mujeeb', 'Ahmed'))
print("Does name start with 'Mujeeb'?:", name.startswith('Mujeeb'))
print("Does name end with 'Rahman'?:", name.endswith('Rahman'))
print("Is name numeric?:", name.isnumeric())
print("Is name alpha?:", name.isalpha()) # will return false because of space
print("Is name alphanumeric?:", name.isalnum()) # will return false because of space
print("Split name by space:", name.split(' '))
print("Join name with '-':", '-'.join(name))
print("Strip whitespace from name:", name.strip()) # will remove leading and trailing spaces
print("Find 'Ur' in name:", name.find('Ur'))
print("Count of 'u' in name (case insensitive):", name.lower().count('u'))
print("Count of 'U' in name (case insensitive):", name.upper().count('U'))
print("Swap case of name:", name.swapcase()) # will swap upper case to lower case and vice versa
print("Is name title case?:", name.istitle())
print("Center name with width 30:", name.center(30)) # will center the name
print("Left justify name with width 30:", name.ljust(30)) # will left justify the name
print("Right justify name with width 30:", name.rjust(30)) # will right justify the name
print("Zero fill name to width 30:", name.zfill(30)) # will zero fill the name
print("Expand tabs in name (if any):", name.expandtabs()) # will expand tabs to spaces
print("Partition name by 'Ur':", name.partition('Ur')) # will partition the name into a tuple
print("Rpartition name by 'Ur':", name.rpartition('Ur')) # will partition the name into a tuple from the right
print("Count of spaces in name (case insensitive):", name.casefold()) # will casefold the name for case insensitive comparison