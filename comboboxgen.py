# Generates Combo Box HTML off of the text list of characters

file = open(f'smash_characters.txt','r')
file_list = file.readlines()

combo_string = ""

for i in file_list:
    combo_string = combo_string + "<option value='" + i.rstrip() + "'>" + i.rstrip() + "</option>\n"

print(combo_string)

# Printed code will have all of the Smash Ultimate roster formatted in a Combo dropdown box for the HTML template