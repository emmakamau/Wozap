'''
Define and initialize classes for our objects
'''

class Source:
    def __init__(self,id,name):
        self.id = id
        self.name = name
    pass

class Article:
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content) -> None:
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        pass