# Django is a Python framework

# Advantages of Django: 
#     i) reusability of components
#     ii) Ready to use features like, :
#             login system, db connection, CRUD operation
#     iii) Vaste community


# Django follows the MVT design pattern (Model View Template).

# Model - The model provides  data from the database. [ Data ]
# The models are usually located in a file called models.py.

# In Django, the data is delivered as an Object Relational Mapping (ORM)



# View - A view is a function or method that takes http requests as arguments, imports the relevant model(s), 
#        and finds out what data to send to the template, and returns the final result. [ Logics ]

# In simple words, view is used to write logics to manipulate data.
# The views are usually located in a file called views.py.



# Template - A template is a file where the data will be displayed. [Layout]
# The templates of an application is located in a folder named templates.



# MVT Workflow:
#     i) User sends a request (URL)
#     ii) URL calls the View
#     iii) View interacts with Model to get data
#     iv) View sends data to template
#     v) Template renders HTML
#     vi) HTML is sent as response to the user.