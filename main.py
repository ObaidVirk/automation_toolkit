from todo_manager import todo_menu
from file_organizer import organize_downloads
from scraper import scrape_quotes
from api_fetcher import fetch_motivation


def main():
    while True:
        print("\n===== Automation Toolkit =====")
        print("1. To-Do Manager")
        print("2. Organize Downloads Folder")
        print("3. Scrape Quotes")
        print("4. Fetch Motivational Quote (API)")
        print("5. Exit")

        choice = input("Select option: ")

        if choice == "1":
            todo_menu()

        elif choice == "2":
            organize_downloads()

        elif choice == "3":
            scrape_quotes()

        elif choice == "4":
            fetch_motivation()

        elif choice == "5":
            print("Exiting Toolkit...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
