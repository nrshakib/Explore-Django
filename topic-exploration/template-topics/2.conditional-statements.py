# Used when you want to show different content depending on a condition.

# if condition

# Syntax: 

# {% if condition %}
#     ...
# {% endif %}

# example:

# {% if user %}
#     <h1>Welcome {{ user.name }}</h1>
# {% endif %}

# if ... else

# {% if user %}
#     <p>Welcome!</p>
# {% else %}
#     <p>Please log in.</p>
# {% endif %}


# if ... elif ... else

# {% if age >= 18 %}
#     <p>Adult</p>
# {% elif age >= 13 %}
#     <p>Teenager</p>
# {% else %}
#     <p>Child</p>
# {% endif %}

# Logical Operators

# and:
# {% if age >= 18 and is_student %}
#     <p>Adult student</p>
# {% endif %}

# or:
# {% if is_admin or is_staff %}
#     <p>Access granted</p>
# {% endif %}

# not:
# {% if not user %}
#     <p>Please log in.</p>
# {% endif %}

# in:
# {% if "Django" in skills %}
#     <p>You know Django.</p>
# {% endif %}