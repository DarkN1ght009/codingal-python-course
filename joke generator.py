import requests

def get_random_joke():
    """Fetch a random joke from the Official Joke API."""
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        response = requests.get(url)
        # Check if the request was successful (Status Code 200)
        response.raise_for_status() 
        
        joke_data = response.json()
        # Returning a formatted string with the setup and punchline
        return f"\n{joke_data['setup']}\n... {joke_data['punchline']}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: Could not connect to the API. ({e})"

def main():
    print("--- Welcome to the Random Joke Generator! ---")
    
    while True:
        user_input = input("\nPress Enter for a joke, or type 'q' to quit: ").strip().lower()
        
        if user_input in ("q", "exit", "quit"):
            print("Thanks for laughing! Goodbye!")
            break
        
        joke = get_random_joke()
        print(joke)

if __name__ == "__main__":
    main()