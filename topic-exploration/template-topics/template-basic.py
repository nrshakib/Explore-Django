# Django templates combine normal HTML with Django Template Language (DTL).

# Variables display data passed from the Django view.

# Syntax: {{variable}}
# Example: <h1>{{ name }}</h1>

# user = {
#     "name": "Shakib",
#     "age": 25,
#     "language": [ "Js", "Python"]
# }

# Access Object Attributes / Dictionary Values

# {{ user.name }}
# {{ user.age }}

# Access List Items

# users = [
#     { 'name': 'Shakib', 'age':28 },
#     { 'name': 'Rijvi', 'age':30 }
# ]

# {{ users.0 }}
# {{ users.1 }}


# Template Comments

# single line comment
#->    {# This is a comment #}

# multiline comment

#->    {% comment %}
#     This is a comment.
#     It will not be rendered.
# {% endcomment %}