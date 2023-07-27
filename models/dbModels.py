from .db import db

# """
# class Recipe:
#     id:int primary key
#     title:str 
#     description:str (text)
# """

# class Recipe(db.Model):
#     id = db.Column(db.Integer(), primary_key=True)
#     title = db.Column(db.String(), nullable=False)
#     description = db.Column(db.Text(), nullable=False)

#     def __repr__(self):
#         return f"<Recipe {self.title} >"

#     def save(self):
#         """
#         The save function is used to save the changes made to a model instance.
#         It takes in no arguments and returns nothing.

#         :param self: Refer to the current instance of the class
#         :return: The object that was just saved
#         :doc-author:jod35
#         """
#         db.session.add(self)
#         db.session.commit()

#     def delete(self):
#         """
#         The delete function is used to delete a specific row in the database. It takes no parameters and returns nothing.

#         :param self: Refer to the current instance of the class, and is used to access variables that belongs to the class
#         :return: Nothing
#         :doc-author:jod35
#         """
#         db.session.delete(self)
#         db.session.commit()

#     def update(self, title, description):
#         """
#         The update function updates the title and description of a given blog post.
#         It takes two parameters, title and description.

#         :param self: Access variables that belongs to the class
#         :param title: Update the title of the post
#         :param description: Update the description of the blog post
#         :return: A dictionary with the updated values of title and description
#         :doc-author:jod35
#         """
#         self.title = title
#         self.description = description

#         db.session.commit()


# user model

"""
class User:
    id:integer
    email:string
    password:string
    first_name: string
    last_name: string
    gender: string
    job_role: string
    department: string
    address: string
    is_admin: BOOLEAN
"""


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False, unique=True)
    last_name = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.Text(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    job_role = db.Column(db.String(), nullable=False)
    department = db.Column(db.String(), nullable=False)
    address = db.Column(db.String(), nullable=False)
    is_admin = db.Column(db.Boolean(), default=False)

    def __repr__(self):
        """
        returns string rep of object
        """
        return f"<User {self.first_name}>"
    def save(self):
        db.session.add(self)
        db.session.commit()