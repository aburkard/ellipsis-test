from user_management import UserManager
from data_processing import process_data
from utils import generate_random_id
import config


def main():
    manager = UserManager()
    manager.add_user("alice", "password123")
    manager.add_user("bob", "qwerty")

    print(manager.authenticate("alice", "password123"))
    print(manager.get_user_info("bob"))

    data = [1, 2, 3, 4, 5]
    processed_data = process_data(data)
    print(processed_data)

    print(generate_random_id())

    print(f"Max users: {config.MAX_USERS}")


if __name__ == "__main__":
    main()
