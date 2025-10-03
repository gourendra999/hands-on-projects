import requests

query=input("What news you want to know about?\n")

api="d2ddc1e53e0949ada1fdbb06d56382f3"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-08-01&sortBy=publishedAt&apikey={api}"

print(url)

r=requests.get(url)
data=r.json()
articles=data["articles"]
for index, article in enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n**********************\n")