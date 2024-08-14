import json

def remove_field_from_json_and_save(input_file, output_file, field):
    # load to JSON data from the input file
    with open(input_file, 'r') as file:
        data = json.load(file)

    # Iterate through each object and delete the specified key
    for obj in data:
        if field in obj:
            del obj[field]
    
    # Write the modified 
