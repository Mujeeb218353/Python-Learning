dictionary = {
    "Walking": "Chalna",
    "Running": "Dourna",
    "Eating": "Khana",
    "Sleeping": "Sona",
    "Coding": "Coding"
}

english_word = input("Enter an English word: ")
print(dictionary.get(english_word, "Translation not found"))