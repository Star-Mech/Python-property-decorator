from circle import Circle

circle = Circle(42)
print(circle.radius)

print(circle.diameter)


circle.diameter = 100

print(circle.diameter)

print(circle.radius)


# from users import User
#
# john = User("John", "secret")
#
# print(john._hashed_password)
#
# print(john.password)
#
#
# john.password = "supersecret"
# print(john._hashed_password)


# from point import Point
#
# point = Point(12, 5)
#
# print(point.x)
#
# print(point.y)
#
# point.x = 42
#
# print(point.x)
#
# point.y = 100.0
#
# print(point.y)
#
# point.x = "one"
#
# # point.y = "1o"