# Get each individual tag- Object is a BS4tag

articles = soup.find_all(name = 'article', class_ = 'list-card')

# Get a view on the structure of a  full article 

article = articles[0].prettify()

print(article)

