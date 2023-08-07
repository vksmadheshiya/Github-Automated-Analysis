import os
import requests
import zipfile

def download_github_repo(repo_owner, repo_name, download_path):
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/zipball"

    # Send a GET request to the GitHub API
    response = requests.get(api_url)

    if response.status_code == 200:
        # Create the download directory if it doesn't exist
        os.makedirs(download_path, exist_ok=True)

        # Save the repository zip file to the download path
        zip_file_path = os.path.join(download_path, f"{repo_name}.zip")
        with open(zip_file_path, "wb") as f:
            f.write(response.content)

        print(f"Repository downloaded and saved to: {zip_file_path}")

        # Unzip the downloaded repository
        with zipfile.ZipFile(zip_file_path, "r") as zip_ref:
            zip_ref.extractall(download_path)

        # Remove the zip file after extraction (optional)
        os.remove(zip_file_path)

        print("Repository extracted and saved to the original files.")
    else:
        print(f"Failed to download repository. Status code: {response.status_code}")

# Replace these values with the owner and name of the repository you want to download
repo_owner = "vksmadheshiya"
repo_name = "Github-Automated-Analysis"
download_path = "GithubRepo/" + repo_owner

download_github_repo(repo_owner, repo_name, download_path)


# Not yet Used 