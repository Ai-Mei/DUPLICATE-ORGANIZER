import pyfiglet

print("\033[0;93m◊º•♡•º◊" * 12)
banner = pyfiglet.figlet_format("No Dups", font = "starwars")
print("\033[0;95m", banner)
print("\033[0;93m◊º•♡•º◊" * 12)
print("\n")

while True:
    # Ask user to input the number of words they are going to use.
    while True:
        try:
            no_of_words = int(input("\033[0;96mInput the number of words: "))
            print("\033[0;93m◊º•♡•º◊" * 12)
            print("\n")
            break
        except ValueError:
            print("\033[1;31m❌ Invalid input. Your answer must be a number.")
            continue

    def remove_duplicates(input_word):
        char_count = {}
        result_word = ""
        
        # Count the number of appearances of the character.
        for char in input_word:
            # Make the upper case and lowercase letters equal.
            char_lower = char.lower()
            char_count[char_lower] = char_count.get(char_lower, 0) + 1
        
        # Store the characters without duplicates.
        for char in input_word:
            char_lower = char.lower()
            if char_lower in char_count and char_count[char_lower] == 1:
                result_word += char


        return result_word.replace(" ", "")

    # Ask the user for input in terms of the initial no. input.
    output_words = []
    for i in range(no_of_words):
        input_word = input("\033[0;92mEnter a word: ")
        result_word = remove_duplicates(input_word)
        output_words.append(result_word)

    # Print the result strings without duplicates
    print("\n")
    print("\033[0;93m◊º•♡•º◊" * 12)
    print("\n\033[0;91mStrings without duplicates: \033[0;95m")
    for word in output_words:
        print(word)

    print("\n")
    print("\033[0;93m◊º•♡•º◊" * 12)

    while True:
        choice = input("\n\033[0;92mDo you input more words? Type yes or no: ").lower()
        if choice == "no":
            print("\n")
            print("\033[0;93m◊º•♡•º◊" * 12)
            print("\n")
            print("\033[0;97mThank you for using the program.".center(70))
            print("\033[0;91m(੭˃ᴗ˂)੭".center(70))
            print("\n")
            print("\033[0;93m◊º•♡•º◊" * 12)
            print("\n")
            exit()
        elif choice == "yes":
            print("\033[0;93m◊º•♡•º◊" * 12)
            print("\n")
            break
        else:
            print("\033[1;31m❌ Invalid input. Please type 'yes' or 'no'. \033[0m\n")



