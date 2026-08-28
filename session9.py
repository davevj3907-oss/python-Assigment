#Create a tuple called fav_apps containing the names of your 5 most-used mobile apps (for example: 'Instagram', 'Zomato', 'Spotify', 'WhatsApp', 'Flipkart') and print the tuple.
"""fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")
print(fav_apps)"""

#Access and print the 2nd and 4th app names from your fav_apps tuple using indexing.
'''fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")
print("2nd app:", fav_apps[1])
print("4th app:", fav_apps[3])'''

#Try to change the first element of your fav_apps tuple to 'YouTube' and observe the error message. Write a comment explaining why this happens based on tuple immutability.
fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")
fav_apps[0] = "YouTube"
# Error: TypeError
# Tuple is immutable, so its elements cannot be changed.

#Use tuple slicing to print the middle three app names from your fav_apps tuple.<br><br><em><strong>Hint:</strong> Use tuple[start:end] syntax to select a range of elements.</em>
'''fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")
print(fav_apps[1:4])
'''
#Create another tuple called new_apps with two more app names you want to try. Concatenate fav_apps and new_apps into a single tuple called all_apps and print the result.
fav_apps = ("Instagram", "Zomato", "Spotify", "WhatsApp", "Flipkart")

new_apps = ("YouTube", "Netflix")

all_apps = fav_apps + new_apps

print(all_apps)