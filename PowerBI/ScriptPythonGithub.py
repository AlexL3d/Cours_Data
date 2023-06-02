import requests
import pandas as pd
import matplotlib.pyplot as plt

def get_trending_repos():
    url = "https://api.github.com/search/repositories"
    params = {
        "q": "stars:>1000",
        "sort": "stars",
        "order": "desc"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        repos = data.get("items", [])
        return repos
    else:
        print("Erreur lors de la récupération des données :", response.status_code)
        return []

trending_repos = get_trending_repos()

repo_data = []
for repo in trending_repos:
    repo_data.append({
        "Nom": repo["name"],
        "URL": repo["html_url"],
        "Nombre d'étoiles": repo["stargazers_count"]
    })

df = pd.DataFrame(repo_data)
print(df)