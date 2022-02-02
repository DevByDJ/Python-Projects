from bs4 import BeautifulSoup
import requests

url = "https://www.newegg.com/p/N82E16824012015?Item=N82E16824012015&quicklink=true"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)


