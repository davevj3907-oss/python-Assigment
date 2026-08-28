#Create a Python list called my_fav_apps containing 5 apps you use daily (for example: 'Instagram', 'Zomato', 'Spotify', etc.) and print the list.
my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "WhatsApp"]
print(my_fav_apps)

#Use the append() method to add a new app (one you started using recently) to your my_fav_apps list, then print the updated list.
my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "WhatsApp"]
my_fav_apps.append("Netflix")
print(my_fav_apps)

#Insert 'WhatsApp' at the second position in your my_fav_apps list using the insert() method and print the result.<br><br><em><strong>Hint:</strong> Remember, list indices start from 0.</em>
my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "WhatsApp"]
my_fav_apps.insert(1, "WhatsApp")
print(my_fav_apps)

#Remove an app you no longer use from your my_fav_apps list using the remove() method, then use the pop() method to remove the last app and print the list after each operation.
my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "WhatsApp"]
my_fav_apps.remove("Zomato")
print("After remove:", my_fav_apps)
my_fav_apps.pop()
print("After pop:", my_fav_apps)

#Sort your my_fav_apps list in alphabetical order using the sort() method, then reverse the order to show your least used app first and print both results.<br><br><em><strong>Constraint:</strong> Use only list methods, not built-in sorted().</em>
my_fav_apps = ["Instagram", "Zomato", "Spotify", "YouTube", "WhatsApp"]
my_fav_apps.sort()
print("Alphabetical order:", my_fav_apps)
my_fav_apps.reverse()
print("Reverse order:", my_fav_apps)