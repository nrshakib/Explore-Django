# {% filter %}: Applies filters to an entire block.

# {% filter upper %}
#     hello django
# {% endfilter %}    # Result: HELLO DJANGO

# Multiple filters:

# {% filter lower|truncatewords:5 %}
#     Some very long text here
# {% endfilter %}



# {% autoescape %}: Controls automatic HTML escaping.

# {% autoescape off %}
#     {{ html_content }}
# {% endautoescape %}


# {% verbatim %}: Prevents Django from interpreting template syntax.

# {% verbatim %}
#     {{ this_will_not_be_processed }}
# {% endverbatim %}

# Useful when documenting Django templates or displaying template syntax.


# {% templatetag %}: Displays Django template syntax characters.
# {% templatetag openvariable %}
# Output: {{


# {% querystring %}: Used to manipulate query-string parameters.
# {% querystring page=3 %}
# Useful for pagination and filtering.


# {% spaceless %}: Removes unnecessary whitespace between HTML tags.

# {% spaceless %}
#     <div>
#         <p>Hello</p>
#     </div>
# {% endspaceless %}


# {% resetcycle %}: Resets a previously defined cycle.  [ Rarely needed. ]

# {% cycle 'odd' 'even' as row_class %}
# {% resetcycle row_class %}


# Debugging: {% debug %}: Displays debugging information.
# Useful during development.


# Lorem Ipsum: {% lorem %}: Generates placeholder text.
# Mostly useful for testing UI.

# {% lorem %}
# Generate words: {% lorem 5 w %}
# Generate paragraphs: {% lorem 2 p %}
