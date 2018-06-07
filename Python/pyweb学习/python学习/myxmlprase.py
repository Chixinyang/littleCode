from xml.parsers.expat import ParserCreate
from urllib import request
class parseXmlSaxHandle(object): #该类的作用是 把相同功能的函数放在一起，相当于归类
    forecast = []
    def start_element(self, name, attrs):
        if 'city' in attrs:
            self.city = attrs['city']
        if 'yweather:forecast' in name:
            self.forecast.append(dict(date=attrs['date'], high=attrs['high'], low=attrs['low']))
    def char_data(self, text):
        pass
    def end_element(self, name):
        pass

def parseXml(xml_str):
    handler = parseXmlSaxHandle()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.CharacterDataHandler = handler.char_data
    parser.EndElementHandler = handler.end_element
    parser.Parse(xml_str)

    return {
        'city': handler.city,
        'forecast': handler.forecast
    }

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
	data = f.read()
	print(data.decode('utf-8'))
result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
print(result)
print('ok')