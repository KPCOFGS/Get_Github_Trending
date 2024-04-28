import requests
from bs4 import BeautifulSoup

def get_trending_repositories():
    url = "https://github.com/trending"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the repository links using the given pattern
    repo_links = soup.select("a[data-hydro-click*='TRENDING_REPOSITORIES_PAGE'][data-hydro-click*='REPOSITORY']")
    for link in repo_links:
        repo_url = "https://github.com" + link["href"]
        print(repo_url)

if __name__ == "__main__":
    get_trending_repositories()
