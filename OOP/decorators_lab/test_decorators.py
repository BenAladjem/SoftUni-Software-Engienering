user = {"name": "Asen", "is_admin":True}
user_not_admin = {"name": "Ivan", "is_admin": False}

# def read_book_content(user):
#     if user["is_admin"]:
#         print(f"{user ['name']} reads the book content")
#     else:
#         raise PermissionError("Only admins")
#
# def read_product_content(user):
#     if user["is_admin"]:
#         print(f"{user['name']} reads the book content")
#     else:
#         raise PermissionError("Only admins")


def admin_access(func):
    def wrapper(user):
        if user["is_admin"]:
            return func(user)

            raise PermissionError("Only admmins can access it")
    return wrapper

@admin_access
def read_book_content(user):
    print(f"{user ['name']} reads the book content")

@admin_access
def read_product_content(user):
    print(f"{user['name']} reads the book content")



read_book_content(user)
read_product_content(user_not_admin)