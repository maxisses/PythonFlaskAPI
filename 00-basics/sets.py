local = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne", "Manuel"}

local_friends = local.difference(abroad)

print(local_friends)

local_friends.add("Heinz")

print(local_friends)


friends = local.union(abroad)

print(friends)

friends = local.intersection(abroad)

print(friends)