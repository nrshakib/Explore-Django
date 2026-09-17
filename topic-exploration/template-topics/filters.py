# template filters are used to modify or transform values

# Basic syntax: {{ value|filter }}
# Filter with an argument: {{ value|truncatechars:50 }}
# Multiple filters: {{ name|lower|capfirst }}




# Text Filters

# lower: Converts text to lowercase
# {{ name|lower }} : SHAKIB → shakib

# upper: Converts text to uppercase
# {{ name|upper }} : shakib → SHAKIB

# capfirst: Capitalizes the first character.
# {{ name|capfirst }}

# title: Capitalizes the first character of each word.
# {{ text|title }}

# truncatechars: Limits the number of characters.
# {{ description|truncatechars:50 }}

# truncatewords: Limits the number of words.
# {{ description|truncatewords:5 }}

# wordcount: Returns the number of words.
# {{ description|wordcount }}

# cut: Removes a specific character.
# {{ name|cut:" " }}




# default value filters
# Useful when a value might be empty or None

# default: Uses a fallback value when the value is false/empty.
# {{ name|default:"Unknown" }}

# default_if_none: Uses a fallback only when the value is None.
# {{ name|default_if_none:"No name" }}

# Difference
# default            → empty/false values
# default_if_none    → only None




# List & Collection Filters

# length: Returns the number of items.
# {{ users|length }}

# first: Returns the first item.
# {{ users|first }}

# last: Returns the last item.
# {{ users|last }}

# join: Joins items together.
# {{ skills|join:", " }}  [ item inside quotes "" indicate which should separate the values]

# Example:
# ["Python", "Django", "React"]
# Output: Python, Django, React

# slice: Slices a list.
# {{ users|slice:":3" }}  [ Returns the first 3 items. ]




# Number Filters

# add: Adds a value.
# {{ number|add:"5" }}  [ If number = 10:  output: 15 ]

# floatformat: Controls decimal points.
# {{ price|floatformat:2 }} [10.5 → 10.50] [float allows till 2 decimal points]

# filesizeformat: Converts bytes to a readable file size.
# {{ file_size|filesizeformat }} [Example: 1024 → 1.0 KB]




# Date & Time Filters

# date: Formats a date.
# {{ date|date:"Y-m-d" }} [Example: 2026-09-17]

# Common formats:
# {{ date|date:"d/m/Y" }}
# {{ date|date:"M d, Y" }}
# {{ date|date:"F j, Y" }}

# time: Formats a time.
# {{ time|time:"H:i" }}

# timesince: Shows the time since a date.
# {{ post.created_at|timesince }} [Example: 3 days, 2 hours]

# timeuntil: Shows the time remaining until a date.
# {{ event.date|timeuntil }}




# HTML & Text Processing Filters

# safe: Prevents Django from escaping HTML.
# {{ html_content|safe }}

# For example: html_content = "<strong>Hello</strong>"
# Without safe: <strong>Hello</strong>
# With safe: Hello (in bold)


# striptags: Removes HTML tags.
# {{ content|striptags }}

# linebreaks: Converts line breaks into HTML paragraphs.
# {{ text|linebreaks }}

# linebreaksbr: Converts line breaks into <br>.
# {{ text|linebreaksbr }}



# Others

# urlencode: Encodes a value for use in a URL.
# <a href="/search/?q={{ query|urlencode }}">
#     Search
# </a>


# yesno: Converts Boolean values to custom text.
# {{ is_active|yesno:"Active,Inactive" }}