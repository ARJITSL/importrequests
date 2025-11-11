import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Make GET request to the API
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError if status != 200

        users = response.json()

        if not users:
            print("No users found in the API response.")
            return

        # Loop through each user and print details
        user_count = 0
        for i, user in enumerate(users, start=1):
            name = user.get("name")
            username = user.get("username")
            email = user.get("email")
            city = user.get("address", {}).get("city")

            # BONUS: Only print if city starts with 'S'
            if city and city.lower().startswith('s'):
                user_count += 1
                print(f"User {user_count}:")
                print(f"  Name: {name}")
                print(f"  Username: {username}")
                print(f"  Email: {email}")
                print(f"  City: {city}")
                print("-" * 25)

        if user_count == 0:
            print("No users found whose city name starts with 'S'.")

    except requests.exceptions.RequestException as e:
        print(f"Error while fetching data: {e}")

# Run the function
if __name__ == "__main__":
    fetch_users()
