import requests,openpyxl
from bs4 import BeautifulSoup

excel = openpyxl.Workbook()
print(excel.sheetnames)
sheet = excel.active
sheet.title = 'Top Rated Movies'
sheet.append(['Movie Rank','Movie Name','Year of relase','Movie Rating'])

try:
    r = requests.get('https://www.imdb.com/chart/top/')
    r.raise_for_status()

    soup = BeautifulSoup(r.text,'html.parser')
    movies = soup.find('tbody', class_="lister-list").find_all('tr')

    for movie in movies:
        name = movie.find('td',class_="titleColumn").a.text
        rank = movie.find('td',class_="titleColumn").get_text(strip=True).split('.')[0]
        year = movie.find('td',class_="titleColumn").span.text.strip('()')
        rating = movie.find('td',class_="ratingColumn imdbRating").strong.text

        # print(rank,name,year,rating)
        sheet.append([rank,name,year,rating])

except Exception as e:
    print(e)

excel.save('IMDB.xlsx')


