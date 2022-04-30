import unittest
from app.models import Article

class ArticlesTest(unittest.TestCase):
    def setUp(self):
        self.new_article = Article("John Doe","The great exodus","Lorem Ipsum Lorem Ipsum","https://chinadigitaltimes.net/chinese/680567.html","https://www.appbank.net/wp-content/uploads/2022/04/20220421-iosandoroidsamune-1.jpeg","2022-04-30T02:48:50Z","» Apple\r\niPhoneAndroid10\r\nOSiOSAndroidAppleYouTubeApple Explained\r\n*Category\r\n Technology*SourceApple Explained ,wikipedia(1),(2)\r\nAndroidiOSApple\r\niOSiPhoneiPad\r\nAndroidAndroidAndroid\r\nAndroidiPhone… [+114 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()