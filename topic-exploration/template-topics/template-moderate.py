# Template Inheritance

# Instead of writing the same navbar, footer, HTML structure, etc. on every page, create a base template.

# {% extends %}: Specifies the parent template.
# {% extends "base.html" %}


# {% block %}: Defines sections that child templates can replace.

# base.html -->

# <!DOCTYPE html>
# <html>
# <head>
#     <title>
#         {% block title %}
#             My Website
#         {% endblock %}
#     </title>
# </head>
# <body>
#     <nav>
#         My Navbar
#     </nav>
#     {% block content %}
#     {% endblock %}
# </body>
# </html>


# home.html -->

# {% extends "base.html" %}
# {% block title %}
#     Home
# {% endblock %}
# {% block content %}
#     <h1>Welcome Home</h1>
# {% endblock %}



# Reusable Templates: These are used to avoid repeating HTML.

# {% include %}: Includes another template.  {% include "navbar.html" %}

# Example structure:

# templates/
# │
# ├── base.html
# ├── navbar.html
# ├── footer.html
# └── home.html

# Then:

# {% include "navbar.html" %}


# Include with Variables
# {% include "user_card.html" with user=user %}

# Multiple values:
# {% include "user_card.html" with user=user title="Profile" %}


# {% with %}: Creates a temporary variable.

# Instead of:

# {{ user.profile.full_name }}
# {{ user.profile.full_name }}
# {{ user.profile.full_name }}

# Use:

# {% with name=user.profile.full_name %}
#     <h1>{{ name }}</h1>
#     <p>{{ name }}</p>
# {% endwith %}


# URL Handling: Used when working with Django's URL system.

# {% url %}: Generates a URL using the URL's name.

# urls.py:
# path("about/", views.about, name="about") [ focus the name attribute ]

# Template:
# <a href="{% url 'about' %}"> [ the name attribute is used here ]
#     About
# </a>


# URL with Parameters

# urls.py:
# path( "user/<int:id>/", views.user, name="user" )

# Template:
# <a href="{% url 'user' id=user.id %}"> View User </a>  [ Or:  {% url 'user' user.id %} ]



# Static Files: Used for CSS, JavaScript, images, etc.

# {% load static %}: Load Django's static template library.


# {% static %}: Generate the static file URL.

# CSS
# <link rel="stylesheet" href="{% static 'css/style.css' %}">

# Image
# <img src="{% static 'images/logo.png' %}">

# JavaScript
# <script src="{% static 'js/app.js' %}"></script>



# Forms & Security: {% csrf_token %} : Protects POST forms against CSRF attacks.
# Important: Use it for Django POST forms.

# <form method="POST">
#     {% csrf_token %}
#     <input type="text" name="username"
#     <button type="submit">
#         Submit
#     </button>
# </form>


# Useful Utility Tags: These aren't used as frequently as if, for, extends, etc., but they're useful to know.


# {% firstof %}: Uses the first non-empty value.
# {% firstof username "Guest" %}
# Multiple values: {% firstof user.name profile.name "Unknown" %}


# {% cycle %}: Cycles through values one by one.

# {% for user in users %}
#     <div class="{% cycle 'odd' 'even' %}">
#         {{ user.name }}
#     </div>
# {% endfor %}

# Result: odd even odd even


# {% now %}: Displays the current date/time.
# {% now "Y-m-d" %}


# {% ifchanged %}: Checks whether a value changed since the previous loop iteration.

# {% for user in users %}
#     {% ifchanged user.country %}
#         <h2>{{ user.country }}</h2>
#     {% endifchanged %}
# {% endfor %}


# {% regroup %}: Groups items based on an attribute.

# {% regroup users by country as country_list %}
# {% for country in country_list %}
#     <h2>{{ country.grouper }}</h2>
#     {% for user in country.list %}
#         <p>{{ user.name }}</p>
#     {% endfor %}
# {% endfor %}



# {% widthratio %}: Calculates a proportional value.
# Useful for progress bars.

# {% widthratio value max_value max_width %}

# Example:

# {% widthratio progress 100 500 %}
# If progress = 50, result is: 250