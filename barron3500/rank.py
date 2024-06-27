import json
from wordfreq import word_frequency

# Load the words from the text file
with open('word.txt', 'r') as file:
    words = file.read().splitlines()

# Calculate frequency for each word and create a list of dictionaries
words_data = [{'word': word, 'frequency': word_frequency(word, 'en')} for word in words]

# Sort words by frequency in descending order
sorted_words = sorted(words_data, key=lambda x: x['frequency'], reverse=True)

# Output to a new JSON file
output_file = 'word_frequencies.json'
with open(output_file, 'w') as file:
    json.dump(sorted_words, file, indent=4)

print(f"Word frequencies have been written to {output_file}.")

