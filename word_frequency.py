import string 

# Text
the_day = """
The Day of Decisions. It was a quiet morning, and the sun peeked through the curtains, casting a warm glow across the room. I see the clock ticking, its hands moving slowly, as if urging me to make a choice. I sit on the edge of my bed, my mind racing with thoughts. Should I stay or should I go?
The room feels heavy with silence, but outside, the world is alive with possibilities. I see a letter on the table, its envelope slightly worn, addressed to me. It's from my old friend, inviting me to a reunion. My heart flutters with excitement, but doubt creeps in. I sit for a moment, weighing the pros and cons.
Finally, I make up my mind. I run to the closet, pulling out my favorite jacket and shoes. The decision is made; I'm going. As I rush out the door, I see the familiar streets of my hometown, unchanged yet full of memories.
I sit at a small café, sipping coffee and reminiscing about the past. The bell above the door jingles, and there she is—my friend, smiling warmly. We catch up, laughing and sharing stories. The time flies by, and before I know it, the sun is setting.
As we part ways, I see the table where we sat, now empty but filled with the echoes of our conversation. I sit for a moment, reflecting on the day. It was a day of decisions, of seeing old friends and revisiting memories.
I run back home, feeling lighter and more at peace. The day was perfect, a reminder of the importance of taking chances and embracing the moments that matter. As I close the door behind me, I see the letter on the table once more, a symbol of the journey I took today.
I sit on the couch, content and grateful for the day's adventures. Life is full of choices, but sometimes, all it takes is a little courage to see where they lead.
"""

# Text Preprocessing
# .lower(): Converts the entire text to lowercase to ensure case-insensitive matching.
# .translate(...): Removes all punctuation from the string.
# str.maketrans('', '', string.punctuation) creates a translation table
# where every punctuation mark is mapped to None (i.e., removed).
# .split(): Splits the clean string into a list of individual words.

analise = the_day.lower().translate(str.maketrans('', '', string.punctuation)).split()
print(analise) 
# Prints the resulting list of words for verification.

# Function 
def words(word_list):
    # This function takes the list of words (analise) as its argument.
    
    # Getting user input for the word to count.
    try:
        # Prompts the user and converts the input to lowercase for accurate comparison.
        word_to_count = str(input("Enter a word to count: ")).lower()
    except EOFError: 
        # Handles cases where input might not be available (e.g., in automated scripts).
        print("Input error: Could not read word.")
        return

    # Count the word occurrences.
    word_count = 0
    for x in word_list:
        # Checks each word in the list against the user's input word.
        if x == word_to_count:
            word_count += 1
    
    # Display the result.
    if word_count > 0:
        # The word was found, display the count.
        print(f"Word: {word_to_count} exists {word_count} times.")
    else:
        # The word was not found.
        print(f"Word: {word_to_count} does not exist.")


# Function Call
# Calls the 'words' function, passing the processed list 'analise' to it.

words(analise)