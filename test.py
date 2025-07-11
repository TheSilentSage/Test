import json

def load_user_data(filepath):
    try:
        file = open(filepath, 'r')
        data = json.load(file)
        file.close()
        return data
    except FileNotFoundError:
        print("Error: File not found")
    except:
        print("Unknown error occurred")

def process_users(users):
    total_age = 0
    for i in range(len(users)):
        total_age += users[i]['age']
        if users[i]['age'] > 18:
            print(users[i]['name'] + " is an adult")
        elif users[i]['age'] < 18:
            print(users[i]['name'] + " is a minor")
        else:
            print(users[i]['name'] + " is exactly 18 years old")

    average_age = total_age / len(users)
    return average_age

def save_results(filepath, avg_age):
    with open(filepath, 'w') as f:
        f.write("Average age: " + avg_age)

# Main logic
data = load_user_data("users.json")
avg = process_users(data)
save_results("results.txt", avg)
