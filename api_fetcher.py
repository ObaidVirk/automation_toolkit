import requests
import random


def fetch_motivation():
    # Primary API
    try:
        response = requests.get("https://zenquotes.io/api/random", timeout=5)
        response.raise_for_status()
        data = response.json()

        quote = data[0]["q"]
        author = data[0]["a"]

        print("\nMotivational Quote:")
        print(f"{quote} - {author}")
        return

    except:
        print("Primary API failed. Trying backup...")

    # Backup API
    try:
        response = requests.get("https://type.fit/api/quotes", timeout=5)
        response.raise_for_status()
        data = response.json()

        random_quote = random.choice(data)

        print("\nMotivational Quote:")
        print(f"{random_quote['text']} - {random_quote['author']}")

    except Exception as e:
        print("All APIs failed:", e)
