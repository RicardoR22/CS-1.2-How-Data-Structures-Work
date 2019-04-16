from flask import Flask
from sampling import another_sample_by_frequency
from histogram_lists import count_words
from histogram_functions import get_words


HTML = """<html><head>
<title>My App</title></head>
<body><h2>{}</h2></body>
</html>
"""


app = Flask(__name__)





@app.route('/')
def hello_world():
    word_list = get_words('GoT_text.txt')
    counts = count_words(word_list)
    sample2 = another_sample_by_frequency(counts)
    return HTML.format(sample2)
