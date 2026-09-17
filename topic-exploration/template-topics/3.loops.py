# The for tag is used to iterate through lists, QuerySets, dictionaries, etc.

# for loop

# syntax:
# {% for item in items %}
#     ...
# {% endfor %}

# example:
# {% for user in users %}
#     <p>{{ user.name }}</p>
# {% endfor %}


# for ... empty
# Displays something when the collection contains nothing.

# {% for user in users %}
#     <p>{{ user.name }}</p>
# {% empty %}
#     <p>No users found.</p>
# {% endfor %}


# Nested Loops

# {% for category in categories %}
#     <h2>{{ category.name }}</h2>

#     {% for product in category.products %}
#         <p>{{ product.name }}</p>
#     {% endfor %}

# {% endfor %}


# Loop Variable
# Django provides special variables inside a for loop.


# forloop.counter = counts the iteration one by one, starts from 1
# {{ forloop.counter }}

# forloop.counter0 = counts the iteration one by one, starting from 0
# {{ forloop.counter0 }}

# forloop.revcounter = Counts backwards from the total
# {{ forloop.revcounter }}

# forloop.revcounter0 = Counts backwards starting from 0
# {{ forloop.revcounter0 }}


# forloop.first = True on the first iteration and executes something based on that
# {% if forloop.first %}
#     <strong>First user</strong>
# {% endif %}

# forloop.last = True on the last iteration and executes something based on that
# {% if forloop.last %}
#     <strong>Last user</strong>
# {% endif %}

# forloop.parentloop = Used inside nested loops to access the outer loop.
# {% for category in categories %}

#     {% for product in category.products %}
#         {{ forloop.parentloop.counter }}
#     {% endfor %}

# {% endfor %}