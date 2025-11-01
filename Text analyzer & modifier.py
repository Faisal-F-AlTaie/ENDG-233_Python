def get_num_of_characters(input_str):
    count = 0
    for char in input_str:
        count += 1
    return count

def get_num_of_words(input_str):
    words = input_str.split()
    return len(words)

def output_without_whitespace(input_str):
    no_space = ""
    for char in input_str:
        if not char.isspace():
            no_space += char
    return no_space


if __name__ == '__main__':
    user_input = input("Enter a sentence or phrase:\n")
    print("\nYou entered:", user_input)

    num_chars = get_num_of_characters(user_input)
    print("\nNumber of characters:", num_chars)

    num_words = get_num_of_words(user_input)
    print("\nNumber of words:", num_words)

    no_whitespace = output_without_whitespace(user_input)
    print("\nString with no whitespace:", no_whitespace)
