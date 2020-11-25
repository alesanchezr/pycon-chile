people = ['Amanda','Bob','Tom','Samuel','Vincent']

# friends = []
# for name in people:
#     if len(name) == 3:
#         friends.append(name)
# print(friends)

friends = [name for name in people if len(name) == 3]
print(friends)

great_friends = ["Mr "+name for name in friends]
print(great_friends)