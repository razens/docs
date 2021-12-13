# Extract, map, reduce
from functool import reduce

volume = reduce(lambda x, y: x * y, map(int, input.strip().split()))
printf(f"{volume=}")

# Filter
names = ["Jhon", "Nike", "Mikle", "Leo", "Alex"]
names_starts_with_a = filter(lambda name: name.startswith("A"), names)
print(tuple(names_starts_with_a))

# Copy list value
indexes = [1,2]
another_index = indexes[:]
# Revert
another_indexes[::-1]

# all true
a,b,c,d,e = True
if all(a,b,c,d,e):
    print("ok")
#any true
if any(a,b,c,d,e):
    print("ok")

# Config
group_to_method = {
    "admin": process_admin_request,
    "manager": process_manager_request,
    "client": process_client_request
}
group_to_method[user.group](user, request)
