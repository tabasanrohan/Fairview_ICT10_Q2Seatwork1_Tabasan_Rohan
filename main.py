
from pyscript import document, display


club_members = [
    "Joan Evangelista"
    "Rohan Tabasan"
    "John Doe"
    "Jane Doe" 
    "Sabine Agacita"
]


def check_candidate(event):

    first_name = document.getElementById("firstname").value.strip()
    last_name = document.getElementById("lastname").value.strip()

    full_name = f"{first_name} {last_name}".strip()
    full_name_lower = full_name.lower()

    members_lower = list(map(str.lower, club_members))
    is_member = full_name_lower in members_lower

    messages = [
        f"Sorry {full_name}, your name is not on the list.",
        f"Congratulations {full_name}! You are now part of the ICT club."
    ]

    display(messages[is_member], target="message")

# x = "This is an editable copy. Use this environment every time we have discussions for our demo."


# colors = ["red", 'pink', 'purple', 'green']
# colors[2] = "black"
# colors.append('yellow')

# display(colors,target="output1")

#conversion

#x = ('3.15', 'seventeen', '5', ('Hello, world'))
#y = list(x)
#display(y,target="output1")

#sample = 'Grade 10 Ruby'
#x = list(sample)

#display(x,target="output1")

#first_list = ['Name', 'Age', "Section",]
#second_list = ['Rohan', '16', 'Ruby']
#combine = first_list + second_list

#display(combine,target="output1")

#fruits = ['cherry', 'berry', 'banana', 'orange']
#del fruits[2]
#fruits.remove(1)
#element_pop = fruits.pop()

#display(fruits, target="output1")
#display(element_pop, target="output1")

#conversion - transforms data type to another
#.append() - adds item to the end
#.insert() - adds item to a given index
#del - deletes item by index
#.remove() - deletes item by value
#pop() - removes and returns an item (by index, or last if none is given)
#.clear

#a = ['Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Friday']
##sort
#a.sort()
#a.reverse

#display(a, target="output1")