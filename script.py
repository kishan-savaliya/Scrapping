from bs4 import BeautifulSoup
import requests
import json

response = requests.get("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.screen_size%255B%255D%3D60%2Binch%2B%2BAbove&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhcmdlIFNjcmVlbiBUVnMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=25.productCard.PMU_V2_2")
htmlcontent = response.content

soup = BeautifulSoup(htmlcontent,'html.parser')
script = soup.find_all('script')[4].text.strip()
data = json.loads(script)
print(data['itemListElement'][0])