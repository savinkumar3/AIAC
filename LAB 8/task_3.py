import string

def is_sentence_palindrome(sentence):
    # Remove punctuation, spaces, and convert to lowercase
    cleaned = ''.join(
        ch.lower() for ch in sentence if ch.isalnum()
    )
    return cleaned == cleaned[::-1]

if __name__ == "__main__":
    sentence = input("Enter a sentence: ")
    if is_sentence_palindrome(sentence):
        print("The sentence is a palindrome.")
    else:
        print("The sentence is not a palindrome.")