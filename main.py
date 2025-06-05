import requests
import time

def get_random_word():
    try:
        response = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        response.raise_for_status()
        word = response.json()[0]
        return word
    except Exception as e:
        print(f"Error: {e}")
        return None

def is_minecraft_name_available(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)

    if(response.status_code == 429):
        print("Take a break!")
        time.sleep(10)
        return is_minecraft_name_available(username)

    return response.status_code == 404

def save_available(username):
    with open("availables.txt", "a") as file:
        file.write(username + "\n")

def main():
    while True:
        word = get_random_word()
        if word and word.isalnum() and 3 <= len(word) <= 16:
            if is_minecraft_name_available(word):
                print(f"[✓] Available: {word}")
                save_available(word)
            else:
                print(f"[x] Taken: {word}")
        else:
            print(f"[!] Invalid: {word}")
        time.sleep(1)

if __name__ == "__main__":
    main()