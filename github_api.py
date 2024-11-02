import requests as rq

GIT_HUB_API_URL = "https://api.github.com"

def fech_user_git(username):
    url = f"{GIT_HUB_API_URL}/users/{username}/events"

    try:
        response = rq.get(url) #запрос урл 
        response.raise_for_status() #проверка успешно ли сделан запрос 
    except rq.exceptions.HTTPError:
        print("Error HTTP")
        return []
    except Exception:
        print("Other Error")
        return []

    events = []
    for event in response.json():#[::10]
        event_type = event['type']
        repo_name = event['repo']['name']
        created_at = event['created_at']
        details = ""

        if event_type == "PushEvent":
            commits = event['payload']['commits']
            commit_messages = []
            for commit in commits:
                commit_messages.append(commit['message'])
            details = " || ".join(commit_messages)
        elif event_type == "IssuesEvent":
            action = event["payload"]["action"]
            issue_title = event["payload"]["issue"]["title"]
            details = f"Issue '{issue_title}' was {action}"
        elif event_type == "PullRequestEvent":
            action = event["payload"]["action"]
            pr_title = event["payload"]["pull_request"]["title"]
            details = f"Pull Request '{pr_title}' was {action}"

        events.append({
            "event_type": event_type,
            "repo_name": repo_name,
            "event_date": created_at,
            "details": details
        })

    return events