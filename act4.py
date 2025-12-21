def reverse_word_order(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    return reversed_sentence


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    result = reverse_word_order(sentence)
    print("Reversed order sentence:")
    print(result)