import json

class Sheet:
    def __init__(self):
        self.notes = []

    def to_json(self):
        def serialize(obj):
            if isinstance(obj, list):  # Check if the object is a list
                return [serialize(item) for item in obj]  # Serialize each item in the list
            elif hasattr(obj, '__dict__'):
                return obj.__dict__  # Serialize custom objects
            return obj  # Return primitive types as is

        return json.dumps({key: serialize(value) for key, value in self.__dict__.items()})

    def save_to_json(self, file_path):
        with open(file_path, 'w') as json_file:
            json_file.write(self.to_json())  # Write the JSON string to the file
        print(f'Sheet JSON saved to {file_path}')  # Confirmation message

