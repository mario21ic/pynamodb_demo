from model import UserModel

# Create Table
UserModel.create_table(read_capacity_units=1, write_capacity_units=1)

# Insert
user = UserModel("John", "Denver")
user.save()

# Count
print("Count:",UserModel.count())

# Query
for user in UserModel.query("Smith", first_name__begins_with="J"):
    print(user.first_name)

# Get
try:
    user = UserModel.get("John", "Denver")
    print(user)
except UserModel.DoesNotExist:
    print("User does not exist")
