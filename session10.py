#Create a dictionary called my_playlist with three songs as keys and their durations in minutes as values, then print the dictionary.
my_playlist = {
    "Kesariya": 4,
    "Apna Bana Le": 3,
    "Tum Hi Ho": 4
}
print(my_playlist)

#Add a new song and its duration to your my_playlist dictionary, then update the duration of one existing song.
my_playlist = {
    "Kesariya": 4,
    "Apna Bana Le": 3,
    "Tum Hi Ho": 4
}

my_playlist["Heeriye"] = 3
my_playlist["Kesariya"] = 5
print(my_playlist)

#Write a function display_friends() that takes a dictionary of Instagram usernames as keys and their follower counts as values, and prints each username with their followers in the format: 'username: 2.3K followers'.
def display_friends(friends):
    for username, followers in friends.items():
        print(username + ":", followers, "followers")
friends = {
    "raj": "2.3K",
    "priya": "5.1K",
    "amit": "1.8K"
}
display_friends(friends)

#Given a dictionary called food_order = {'Pizza': 2, 'Burger': 1, 'Fries': 3}, use the keys(), values(), and items() methods to print: a) all food items, b) all quantities, and c) each item with its quantity.
food_order = {
    "Pizza": 2,
    "Burger": 1,
    "Fries": 3
}

print("Food items:", food_order.keys())

print("Quantities:", food_order.values())
print("Items with quantity:")
for item, quantity in food_order.items():
    print(item, ":", quantity)

#Build a function update_cart(cart, item, qty) that adds a new item to a Flipkart-style cart dictionary or updates the quantity if the item already exists, then returns the updated cart.<br><br><em><strong>Hint:</strong> Use the dictionary's update() method or direct assignment for adding/updating entries.</em>
def update_cart(cart, item, qty):

    if item in cart:
        cart[item] = cart[item] + qty
    else:
        cart[item] = qty

    return cart
cart = {
    "Mobile": 1,
    "Headphones": 2
}
cart = update_cart(cart, "Mobile", 2)
print(cart)