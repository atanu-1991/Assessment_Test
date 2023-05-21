# Consider a string to be valid if all characters of the string appear the same number of times. It is also valid if
# he can remove just one character at the index in the string, and the remaining characters will occur the same
# number of times. Given a string, determine if it is valid. If so, return YES , otherwise return NO .

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# Example input 1 - s = “abc”. This is a valid string because frequencies are { “a”: 1, “b”: 1, “c”: 1 }
# Example output 1- YES
# Example input 2 - s “abcc”. This string is not valid as we can remove only 1 occurrence of “c”. That leaves
# character frequencies of { “a”: 1, “b”: 1 , “c”: 2 }
# Example output 2 - NO

def count_char_frequency(word: str) -> dict:
    '''
    This function will split the word and will store each character and
    count of character in a dictionary as a key, value pair
    input: word: string input
    return: return dictionary as a output
    '''

    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def string_validation(word: str) ->bool:
    '''
    This function will check whether the given word is valid or not
    '''

    char_count = count_char_frequency(word=word)

    # counting the unique count of the character in the word
    unique_char_count = set(char_count.values())

    # check the count of each character in the word
    if len(unique_char_count) == 1:
        print(f"input= {word}")
        print("Output= YES")
        print(f"Explanation: This is a valid string because frequencies are: {char_count}")

    elif len(unique_char_count) == 2:
        if (max(list(unique_char_count)) - min(list(unique_char_count)) == 1):
            for key, value in char_count.items():
                if value == max(list(unique_char_count)):
                    char_count[key] = value - 1
                    print(f"input= {word}")
                    print("Output= YES")
                    print(f"Explanation: This string is valid as we can remove only 1 occurrence of {key} \n That leaves character frequencies of {char_count}")

        else:
            for key, value in char_count.items():
                if value == max(list(unique_char_count)):
                    char_count[key] = value - 1
                    print(f"input= {word}")
                    print("Output= NO")
                    print(f"Explanation: This string is not valid as we can remove only 1 occurrence of '{key}' \n That leaves character frequencies of {char_count}")


    else:
        print(f"input= {word}")
        print("Output= NO")
        print(f"Explanation: All the character in the string does not have same frequencies: {char_count}")



if __name__ == "__main__":
    input_word = input("Enter The Word: ")
    string_validation(input_word)


