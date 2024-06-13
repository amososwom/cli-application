import uuid

# Generate a UUID and convert it to string
unique_id = uuid.uuid4() #.hex
print(str(unique_id)[0:7])
print(unique_id.hex[0:7])