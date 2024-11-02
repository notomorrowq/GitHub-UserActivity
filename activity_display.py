
def display_activity(events):
    if not events:
        print("No recent activity found in database")

    for event_type, repo_name, event_date, details in events:
        print(f"Event Type: {event_type}")
        print(f"Repository: {repo_name}")
        print(f"Date: {event_date}")
        print(f" - Details: {details}")
        print("=" * 20)
        print("=" * 20)