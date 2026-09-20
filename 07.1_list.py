lists = [21,5,54,78,65]

# greatest = max(list)
# print(greatest)

greater = lists[0]

for list in lists:
    if list > greater:
        greater = list
print(greater)