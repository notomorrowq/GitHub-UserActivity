import db_manger
import activity_display

def main():
    username = input("Enter username: ")
    db_manger.save_user_activity(username)
    activity_display.display_activity(db_manger.get_all_user_events(username))


if __name__ == "__main__":
    main()