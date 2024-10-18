"""
Filter Messages

You are about to write a bit more code in a single function than you have before.

Do not try to write it all at once. Start with the outermost loop, and work your way inwards. Add extra print() statements and run your code often to make sure it's doing what you expect. Just make sure to remove the extra print() statements before submitting your code.

Running your code often to make sure each line is doing what you expect is called "debugging". All programmers, even seasoned professionals, break large problems down into small ones that they can debug line by line.
Assignment

We need to filter the profanity out of our game's live chat feature! Complete the filter_messages function. It takes a list of chat messages as input and returns 2 new lists:

    A list of the same messages but with all instances of the word dang removed.
    A list containing the number of dang words that were removed from the message at that particular index.

Here are some examples:

messages = ["dang it bobby!", "look at it go"]
filter_messages(messages) # returns ["it bobby!", "look at it go"], [1, 0]

messages2 = ["That's the bloody dang Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a dang razor!"]
filter_messages(messages2) # returns ["That's the bloody Reaper of Mars...", "Pax au Telemanus!", "I was never taught how to use a razor!"], [1, 0, 1]

Here are the steps for you to follow:

    Create the 2 empty lists that you'll return at the end. One for the filtered messages, and one for counts of words removed.
    For each message in the input list:
        Split the message into a list of words using the .split() string method (see below for help).
        Create a new empty list for all the non-bad words for this message.
        Create a counter variable and set it to 0. We'll increment this when we remove words from this message.
        For each word in the message:
            If the word is dang, increment the counter
            If it is not dang, add the word to the non-bad word list you created
        Join the list of non-bad words into a single string using the .join() method (see below for help)
        Append the new clean message to the final list of filtered messages
        Append the count of bad words removed to its list
    Return the filtered messages first, then the counters

Tips

Because we are working with strings that need to be converted to lists and vice versa, here are some very helpful Python methods we can use to make our lives much easier.
Split a string into a list of words

The .split() method in Python is called on a string and returns a list by splitting the string based on a given delimiter. If no delimiter is provided, it will split the string on whitespace. Here's a quick example:

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]

Join a list of strings into a single string

The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"
"""

def filter_messages(messages):
    # Create the 2 empty lists that you'll return at the end. 
    # One empty list for the filtered messages.
    filtered_messages = []
    # One empty list for counts of words removed.
    removed_word_count = []
    # For each message in the input list: 
    for message in messages:
        # Split the message into a list of words using the .split() string method .
        words = message.split()
        # Create a new empty list for all the non-bad words for this message.
        filtered_words = []
        # Create a counter variable and set it to 0. We'll increment this when we remove words from this message.
        counter = 0

        # For each word in the message:
        for word in words:
            if word == 'dang':
                # If the word is dang, increment the counter.
                counter += 1
            else:
                # If it is not dang, add the word to the non-bad word list you created.
                filtered_words.append(word)

        # Join the list of non-bad words into a single string using the .join()
        filtered_words = " ".join(filtered_words)
        # Append the new clean message to the final list of filtered messages.
        filtered_messages.append(filtered_words)
        # Append the count of bad words removed to its list.
        removed_word_count.append(counter)
    # Return the filtered messages first, then the counters.
    return (filtered_messages, removed_word_count)


"""
Input:
 * messages: ['darn it', "this dang thing won't work", 'lets fight one on one']
Expecting:
 * filtered messages: ['darn it', "this thing won't work", 'lets fight one on one']
 * words removed: [0, 1, 0]
Actual:
 * filtered messages: ['darn it', "this thing won't work", 'lets fight one on one']
 * words removed: [0, 1, 0]
Pass
---------------------------------
Input:
 * messages: ['well dang it', 'dang the whole dang thing', 'kill that knight, dang it', 'get him!', 'donkey kong', 
'oh come on, get them', 'run away from the dang baddies']
Expecting:
 * filtered messages: ['well it', 'the whole thing', 'kill that knight, it', 'get him!', 'donkey kong', 'oh come on, get them', 'run away from the baddies']
 * words removed: [1, 2, 1, 0, 0, 0, 1]
Actual:
 * filtered messages: ['well it', 'the whole thing', 'kill that knight, it', 'get him!', 'donkey kong', 'oh come on, get them', 'run away from the baddies']
 * words removed: [1, 2, 1, 0, 0, 0, 1]
Pass
============= PASS ==============
2 passed, 0 failed
"""