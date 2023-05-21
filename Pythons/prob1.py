# Question 1: -
# Write a program that takes a string as input, and counts the frequency of each word in the string, there might
# be repeated characters in the string. Your task is to find the highest frequency and returns the length of the
# highest-frequency word.

# Note - You have to write at least 2 additional test cases in which your program will run successfully and provide
# an explanation for the same.

# Example input - string = “write write write all the number from from from 1 to 100”
# Example output - 5
# Explanation - From the given string we can note that the most frequent words are “write” and “from” and
# the maximum value of both the values is “write” and its corresponding length is 5

def find_highest_frequency_word(string_input: str):
    '''Find the length of highest frequency word in the given string'''

    # Split the string into words
    words = string_input.split()

    # counting the frequency of each word using a dictionary
    word_count = {}
    for word in words:
        if word.lower() in word_count:
            word_count[word.lower()] += 1
        else:
            word_count[word.lower()] = 1


    # Find the word with the highest frequency
    max_count = max(word_count.values())
    highest_count_word = [word for word, count in word_count.items() if count == max_count]


    # Find the highest-count word, length of the highest-count word and returns the highest_count_word list
    if len(highest_count_word) == 1:
        return len(highest_count_word[0]), highest_count_word[0], highest_count_word
    else:
        max_len = max([len(word) for word in highest_count_word])
        max_word = [word for word in highest_count_word if len(word) == max_len]
        return max_len, max_word, highest_count_word
    

if __name__ == "__main__":
    input_txt = input("Enter The Text: ")
    word_len, word, highest_count_word = find_highest_frequency_word(input_txt)
    print(f"Output: {word_len}")
    print(f"Explanation: From the given string we can note that the most frequent words are {highest_count_word} \n and the maximum value of both the values is {word} and its corresponding length is {word_len}")
