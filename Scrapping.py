from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.screen_size%255B%255D%3D60%2Binch%2B%2BAbove&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhcmdlIFNjcmVlbiBUVnMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=25.productCard.PMU_V2_2")
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,'html.parser')

titles = []
prices = []
images = []

for d in soup.find_all('div', class_="_13oc-S"):
    title = d.find('div',class_="_4rR01T")
    price = d.find('div',class_="_25b18c")
    image = d.find('img',class_="_396cs4")
    # print(titles.string)
    # print(prices.text)
    # print(images)

    titles.append(title.string)
    prices.append(price.text)
    images.append(image.get('src'))

print(titles)
print(prices)
print(images)
  

# contents = soup.find('li',class_="ebb6d69bfc").find_all('div')
# print(contents)

# # for content in contents:
# #     name = content.find('',class_='a1b3f50dcd b2fe1a41c3 ef8295f3e6 db7f07f643')
# #     print(name)
