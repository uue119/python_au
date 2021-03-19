import requests

TOKEN = '12e9ccaa50664a518c8f8439591054bea22a8333'

TASK_PREFIX = ['LEETCODE', 'GENERATOR', 'TRIANGLE', 'HEXNUMBER', 'REQUESTS', 'ITERATOR']
GROUP = ['1021', '1022']
ACTION = ['Added', 'Deleted', 'Refactored', 'Deleted', 'Moved']


def prepare_headers():
    return {
        'Authorization': TOKEN,
        'Accept': "application/vnd.github.v3+json"
    }


def get_all_user_prs(user_login, repo_name, pr_state):
    url = f'https://api.github.com/repos/{user_login}/{repo_name}/pulls?state={pr_state}'
    all_prs = requests.get(url, headers=prepare_headers())
    print(all_prs.status_code)
    return all_prs.json()


def get_all_pr_commits(pr):
    all_pr_commits = requests.get(pr['commits_url'], headers=prepare_headers())
    return all_pr_commits.json()


def check_prefixes(title):
    result = ''
    project = title.split('-')[0]
    group = title.split('-')[1].split()[0]
    action = title.split()[1]
    if project not in TASK_PREFIX:
        result += 'Your task prefix should be one of the following: {}. \n'.format(TASK_PREFIX)
    if group not in GROUP:
        result += 'Your group should be one of the following: {}. \n'.format(GROUP)
    if action not in ACTION:
        result += 'Your action should be one of the following: {}. \n'.format(ACTION)
    return result


def send_pr_comment(pr, message_error):
    data = {'body': message_error,
            'path': requests.get(pr['url'] + '/files', headers=prepare_headers()).json()[0]['filename'],
            'position': 1,
            'commit_id': pr['head']['sha']}
    requests.post(pr['url'] + '/comments', headers=prepare_headers(), json=data)


def verify_pr(pr):
    commits = get_all_pr_commits(pr)
    for commit in commits:
        result = check_prefixes(commit['commit']['message'])
        if result:
            send_pr_comment(pr, result)


if __name__ == '__main__':
    repo_name = 'python_au'
    user_login = 'uue119'
    pr_state = 'open'
    pulls = get_all_user_prs(user_login, repo_name, pr_state)
    for pull in pulls:
        verify_pr(pull)
