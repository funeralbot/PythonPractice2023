friends = {"Bob", "Rolf", "Anne"}

abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad) #calls the difference funtion inside the friends set

print(local_friends)

local_friends = abroad.difference(friends) #empty set is called

print(local_friends)

local = {"Rolf"}

abroad = {"Bob", "Anne"}

friends = local.union(abroad) # the union functions combines two sets together

print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}

science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) #show which two different sets have the same elements inside

print(both)