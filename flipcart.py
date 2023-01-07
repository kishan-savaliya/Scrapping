from requests_html import HTMLSession

s = HTMLSession()

url = 'https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.screen_size%255B%255D%3D60%2Binch%2B%2BAbove&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhcmdlIFNjcmVlbiBUVnMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=25.productCard.PMU_V2_2'
r = s.get(url)

products = []
def get_product(url):

    title = r.html.find('div._1YokD2._3Mn1Gg div._4rR01T',first=True).text
    price = r.html.find('div._1YokD2._3Mn1Gg div._30jeq3._1_WHN1',first=True).text
    rating = r.html.find('div._1YokD2._3Mn1Gg span._1lRcqv',first=True).text
    warranty = r.html.find('div._1YokD2._3Mn1Gg li.rgWa7D',first=True).text
    # print(title,price,rating,warranty)

    product = {
        "title" : title,
        "price" : price,
        "rating" : rating,
        "warranty" : warranty
    }
    return product





