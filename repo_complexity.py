import requests
import openai
import radon.metrics
import re
from langchain_gpt import calculate_complexity_by_chatgpt

complexity_tag = "Simple"
def fetch_repositories(github_url):
    # Extracting the username from the GitHub URL
    username = github_url.split('/')[-1]

    # Sending a GET request to the GitHub API
    response = requests.get(f'https://api.github.com/users/{username}/repos')

    if response.status_code == 200:
        repositories = response.json()

        # Extracting repository names
        repository_names = [repo['name'] for repo in repositories]

        return repository_names
    else:
        print(f"Failed to fetch repositories for user '{username}'. Error: {response.text}")
        return []

def fetch_code_and_return_total_score(github_url, repository_name):
    # Extracting the username and repository name from the GitHub URL
    username = github_url.split('/')[-1]
    
    TOTAL_SCORE = 0.0
    
    # Sending a GET request to the GitHub API
    response = requests.get(f'https://api.github.com/repos/{username}/{repository_name}/contents')

    if response.status_code == 200:
        contents = response.json()
        
        for item in contents:
            print("**"*100)
            print(item)
            print("**"*100)
            if item['type'] == 'file':
                file_path = item['path']
                file_response = requests.get(f'https://raw.githubusercontent.com/{username}/{repository_name}/master/{file_path}')
                
                if file_response.status_code == 200:
                    file_contents = file_response.text

                    # Remove comments
                    file_contents = re.sub(r'#.*', '', file_contents)

                    # Remove import statements
                    file_contents = re.sub(r'^import.*$', '', file_contents, flags=re.MULTILINE)
                    file_contents = re.sub(r'^from.*$', '', file_contents, flags=re.MULTILINE)

                    # Remove empty lines and leading/trailing whitespaces
                    file_contents = '\n'.join(line.strip() for line in file_contents.split('\n') if line.strip())
                    

                    try:
                        if '.py' in item['name']:
                            TOTAL_SCORE += float(calculate_complexity_by_chatgpt(file_contents))
                        else :
                            TOTAL_SCORE += float(calculate_complexity(file_contents, file_path))
                    except:
                        TOTAL_SCORE += float(calculate_complexity(file_contents, file_path))
                else:
                    print(f"Failed to fetch contents of file '{file_path}'. Error: {file_response.text}")
    else:
        print(f"Failed to fetch contents of repository '{repository_name}'. Error: {response.text}")

    return TOTAL_SCORE


def calculate_complexity(code, filepath=None):
    try:
        complexity = radon.metrics.mi_visit(code, False)
        return complexity
    except Exception as e:
        print(e)
        print(f"Failed to calculate complexity for file '{filepath}'.")
        return 0

def calculate_complexity_by_range(code, complexity_tag, filepath=None):
    """ Function To Check complexity and also returns complexity Tags  Func Not yet Used"""
    try:
        complexity = radon.metrics.mi_visit(code, False)
        if complexity > 1 :
            complexity_tag = "Simple"
        elif complexity > 10 :
            complexity_tag = "Medium"
        elif complexity > 20 :
            complexity_tag = "Complex"
        elif complexity > 50 :
            complexity_tag = "Very Complex"
        return complexity
    except Exception as e:
        print(e)
        print(f"Failed to calculate complexity for file '{filepath}'.")
        return 0

def find_most_complex_repository(github_url):
    repositories = fetch_repositories(github_url)

    if not repositories:
        print("No repositories found.")
        return None

    most_complex_repo = None
    max_complexity = -1

    for repo in repositories:
        complexity = fetch_code_and_return_total_score(github_url, repo)
        print(f"\n Complexity for repository '{repo}' is : {complexity} \n")

        if complexity > max_complexity:
            most_complex_repo = repo
            max_complexity = complexity

    return most_complex_repo
