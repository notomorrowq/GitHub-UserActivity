import db_manger
import activity_display


def main():
    username = input("Enter username: ")
    db_manger.save_user_activity(username)
    activity_display.display_activity(db_manger.get_all_user_events(username))
    #db_manger.drop_db("events_table") #drop db

def all_info_by_username(username):
    all_user_events = db_manger.get_all_user_events(username)
    for event in all_user_events:
        print(event)


if __name__ == "__main__":
    main()
    #username = input("Search by username: ")
    #all_info_by_username(username)