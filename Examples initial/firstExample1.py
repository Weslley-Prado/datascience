
# Inicialize o dict com uma lista vazia para cada id de usuário:

friendships = {user[“id”]: [] for user in users}

# Em seguida, execute um loop pelos pares de amigos para preenchê-la:
for i, j in friendship_pairs:

friendships[i].append(j) # Adicione j como amigo do usuário i
friendships[j].append(i) # Adicione i como amigo do usuário j

def number_of_friends(user):

“““Quantos amigos tem o _user_”””

user_id = user[“id”]

friend_ids = friendships[user_id]

return len(friend_ids)

total_connections = sum(number_of_friends(user)

for user in users)