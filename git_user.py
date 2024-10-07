import urllib.request
import json 
import argparse 

# Create Command-line argument parser to collect and parse username
parser = argparse.ArgumentParser(description='Collect a username and use it in an API URL.')
parser.add_argument('username', help='The username to be included in the API URL')
args = parser.parse_args()

def main():
    actions = []
    # Specify URL
    url = f"https://api.github.com/users/{args.username}/events" 

    # Fetch the data 
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()

        # Parse JSON data
        parsed_data = json.loads(data.decode("utf-8"))

    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")

    def handle_event(activity):
        if activity['type'] == "PushEvent":
            actions.append(f"Pushed {activity['payload']['size']} commit(s) to {activity['repo']['name']}")
        elif activity["type"] == "ForkEvent":
            actions.append(f"Forked {activity['repo']['name']}")
        elif activity["type"] == "PullRequestReviewEvent":
            actions.append(f"Submitted a review for a pull request in {activity['repo']['name']}")
        elif activity["type"] == "PullRequestReviewCommentEvent":
            actions.append(f"Commented on a pull request review in {activity['repo']['name']}")
        elif activity["type"] == "IssueCommentEvent":
            actions.append(f"Commented on an issue in {activity['repo']['name']}")
        elif activity["type"] == "Starred Event":
            actions.append(f"Starred {activity['repo']['name']}")
        elif activity["type"] == "IssuesEvent":
            if activity['payload']['action'] == "closed":
                actions.append(f"Closed an issue in {activity['repo']['name']}")
            elif activity['payload']['action'] == "opened":
                actions.append(f"Opened a new issue in {activity['repo']['name']}")
            else:
                actions.append(f"Edited an issue in {activity['repo']['name']}")
        elif activity["type"] == "PullRequestEvent":
            if activity['payload']['action'] == "closed":
                actions.append(f"Closed a pull request in {activity['repo']['name']}")
            elif activity['payload']['action'] == "opened":
                actions.append(f"Opened a new pull request in {activity['repo']['name']}")
            else:
                actions.append(f"Merged a pull request in {activity['repo']['name']}")
        return None
    
    for activity in parsed_data:
        handle_event(activity)

    return actions



actions = main()
print(f"\n{args.username} has performed the following actions on github recently:\n")
for action in actions:
    print(f"- {action}")