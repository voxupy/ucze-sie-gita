import string


letters = string.ascii_lowercase
#lista liter alfabetu
char_list = []
new_word = []
new_word_list = []


#dodawanie liter do listy
for char in letters:
    char_list.append(char)

#inputy
word = input("podaj słowo: ")
shift = int(input("podaj enkrypcje: (1-9) "))


#dodawanie naszego słowa do listy 
for char in word:
    new_word_list.append(char)






def encryption(new_word_list, shift):

    for char in new_word_list:
        if char == " ":
            new_word.append(char)
        elif char in char_list:
            index = char_list.index(char)
            new_index = index + shift
            if new_index > 26:
                new_index -= 26

            new_word.append(char_list[new_index])
    
    return "".join(new_word)



print(encryption(new_word_list, shift))