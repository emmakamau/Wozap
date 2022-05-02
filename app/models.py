'''
Define and initialize classes for our objects
'''

class Article:
    articles_list = []
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
    pass

class Source:
    sources_list = []
    def __init__(self,id,name,url):
        self.id = id
        self.name = name
        self.url = url
    pass
