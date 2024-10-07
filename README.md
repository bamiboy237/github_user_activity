# GitHub Activity Tracker
This Python script retrieves and displays recent activity for a specified GitHub user using the GitHub API. It provides insights into various actions performed by the user, such as pushes, forks, pull requests, and more.

## Features
Fetches recent events of a GitHub user.
Displays different types of activities, including:
Pushes to repositories
Forking repositories
Submitting pull request reviews
Commenting on issues and pull requests
Starring repositories
Opening and closing issues and pull requests

### Requirements
Python 3.x
urllib and json modules (included in the standard library)

#### Usage
1. Clone the repository:
     git clone https://github.com/yourusername/repository-name.git
     cd repository-name
2. Run the script:
     python github_activity_tracker.py <username>
     
##### Example
python github_activity_tracker.py octocat
Output:
octocat has performed the following actions on GitHub recently:
- Pushed 3 commit(s) to octocat/Hello-World
- Forked octocat/Spoon-Knife
- Submitted a review for a pull request in octocat/Hello-World

###### Code Explanation
Argument Parsing: The script uses argparse to collect the GitHub username from the command line.
API Request: It constructs a URL to fetch the user's events from the GitHub API.
Error Handling: The script handles HTTP and URL errors gracefully, providing informative messages.
Event Handling: The handle_event function processes different types of activities and appends them to the actions list.
Output: Finally, it prints the recent actions performed by the specified user.

####### Contributing
Feel free to submit issues or pull requests if you would like to contribute to this project.

Project Link: https://roadmap.sh/projects/github-user-activity
