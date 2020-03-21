text = input(" Input 7 or more characters and an odd number of characters.")
print("The old string: ",text)
n = int(len(text) / 2) - 1
print("Middle 3 characters:",text[n:n +3])
print("The new string:",text[0:n] +text[n:n +3].upper() + text[n +3:])