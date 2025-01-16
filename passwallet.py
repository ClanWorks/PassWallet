import os
import base64
from cryptography.fernet import Fernet

# Path to store the encrypted password file
VAULT_FILE = "passwallet.enc"
KEY_FILE = "passwallet.key"

def load_or_create_key():
    """Load encryption key or create a new one if it doesn't exist."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)
        print("New encryption key created.")
    else:
        with open(KEY_FILE, "rb") as key_file:
            key = key_file.read()
    return Fernet(key)

def load_vault():
    """Load and decrypt the vault contents."""
    if not os.path.exists(VAULT_FILE):
        return {}
    with open(VAULT_FILE, "rb") as vault_file:
        encrypted_data = vault_file.read()
    decrypted_data = cipher.decrypt(encrypted_data).decode("utf-8")
    return eval(decrypted_data)  # Safely parse the string back into a dictionary

def save_vault(vault):
    """Encrypt and save the vault contents."""
    encrypted_data = cipher.encrypt(str(vault).encode("utf-8"))
    with open(VAULT_FILE, "wb") as vault_file:
        vault_file.write(encrypted_data)

def add_password(service, username, password):
    """Add a new password entry to the vault."""
    vault[service] = {"username": username, "password": password}
    save_vault(vault)
    print(f"Password saved for {service}.")

def get_password(service):
    """Retrieve password for a given service."""
    entry = vault.get(service)
    if entry:
        print(f"Service: {service}")
        print(f"Username: {entry['username']}")
        print(f"Password: {entry['password']}")
    else:
        print(f"No entry found for {service}.")

def main():
    print("Welcome to PassWallet 🔒")
    while True:
        print("\nOptions:")
        print("1. Add a new password")
        print("2. Retrieve a password")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            service = input("Enter the service name: ").strip()
            username = input("Enter the username: ").strip()
            password = input("Enter the password: ").strip()
            add_password(service, username, password)
        elif choice == "2":
            service = input("Enter the service name: ").strip()
            get_password(service)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    cipher = load_or_create_key()
    vault = load_vault()
    main()

