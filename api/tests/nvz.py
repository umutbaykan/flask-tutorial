import os
import tempfile
import json
import glob


seed_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seeds')
for file_path in glob.glob(os.path.join(seed_path, '*')):
    if os.path.isfile(file_path):
        collection = os.path.basename(file_path).split('.')[0]
        with open(file_path, 'r') as f:
            data = json.load(f)
            print(collection, data)                    


# # Load the JSON data from the users.json file
# with open(users_file_path, 'r') as f:
#     users_data = json.load(f)

# # Access the users data as a dictionary
# users = users_data['users']
