import requests

# Download the data-set from Github
url = "https://raw.githubusercontent.com/bursteinalan/Data-Sets/master/Fake%20News/news.csv"
r = requests.get(url, allow_redirects=True)
with open("data_set.csv", "wb") as f:
    f.write(r.content)
