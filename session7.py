#Create a Python script called insta_caption.py that takes a user's Instagram caption as input and prints the first 10 characters using string indexing.
# insta_caption.py

"""caption = input("Enter your Instagram caption: ")

print("First 10 characters:", caption[0:10])"""
#Write a function extract_artist(song_title) that takes a string in the format 'Song Name - Artist Name' (like you see on Spotify) and returns just the artist's name using string slicing.<br><br><em><strong>Hint:</strong> Use the index() method to find the position of the dash.</em>
"""def extract_artist(song_title):
    dash = song_title.index("-")
    artist = song_title[dash + 1:]
    return artist.strip()


song = input("Enter song title: ")

print("Artist:", extract_artist(song))"""
#Build a function reverse_message(message) that reverses any string passed to it, similar to how WhatsApp displays reversed text stickers.<br><br><em><strong>Constraint:</strong> Do not use Python's built-in reversed() or [::-1] slicing shortcut.</em>
"""def extract_artist(song_title):
    dash = song_title.index("-")
    artist = song_title[dash + 1:]
    return artist.strip()
song = input("Enter song title: ")
print("Artist:", extract_artist(song))"""
#Given a Flipkart product description string, write a Python script that extracts and prints the first word, last word, and the total number of words using string methods split(), indexing, and len().
"""def reverse_message(message):
    result = ""

    for i in range(len(message) - 1, -1, -1):
        result = result + message[i]

    return result
message = input("Enter your message: ")
print("Reversed message:", reverse_message(message))"""
#Create a function mask_phone_number(phone) that takes a 10-digit phone number as a string and returns it in the format '******1234', showing only the last 4 digits like Paytm does.<br><br><em><strong>Hint:</strong> Use string slicing and concatenation.</em>
"""description = input("Enter product description: ")

words = description.split()

print("First word:", words[0])
print("Last word:", words[-1])
print("Total words:", len(words))"""