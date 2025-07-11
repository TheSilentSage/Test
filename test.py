import json

def load_user_data(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Error: File not found")
        return None
    except json.JSONDecodeError:
        print("Error: Invalid JSON format")
        return None
    except:
        print("Unknown error occurred")
        return None

def process_users(users):
    if not users:
        return 0  # Handle empty list to avoid ZeroDivisionError

    total_age = 0
    for user in users:
        total_age += user['age']
        if user['age'] > 18:
            print(user['name'] + " is an adult")
        elif user['age'] < 18:
            print(user['name'] + " is a minor")
        else:
            print(user['name'] + " is exactly 18 years old")

    try:
        average_age = total_age / len(users)
    except ZeroDivisionError:
        average_age = 0  # Or handle the case appropriately
    return average_age

def save_results(filepath, avg_age):
    with open(filepath, 'w') as f:
        f.write("Average age: " + str(avg_age))

# Main logic
data = load_user_data("users.json")
if data:
    avg = process_users(data)
    save_results("results.txt", avg)
