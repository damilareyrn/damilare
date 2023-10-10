import string

# read the file.
file = "C:\\Users\\Admin\\Desktop\\damilare website\\name.txt"
try:
    with open(file, "r") as file:
        text = file.read()

        # tokenize the word in the file by removing the space and
        # punctuation marks
        # split the text into words
        words = text.split()

        # remove punctuation from words
        translator = str.maketrans('', '', string.punctuation)
        words = [word.translate(translator) for word in words]

        # code block to start counting
        word_count = {}
        for word in word_count:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        # sort the dictionary by values in descending order
        sorted_word_count = dict(
            sorted(word_count.items(), key=lambda x: x[1],
                   reverse=True))
        # Display the word frequency
        for word, count in sorted_word_count.items():
            print(f"{word}:  {count}")
except FileNotFoundError:
    print("file not found")

