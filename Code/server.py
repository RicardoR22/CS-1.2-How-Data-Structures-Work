from flask import Flask, render_template
from sampling import sample_by_frequency
from histogram_lists import count_words
from histogram_functions import get_words


app = Flask(__name__)


@app.route('/')
def hello_world():
    word_list = get_words('GoT_text.txt')
    counts = count_words(word_list)
    selected_words = []
    for _ in range(8):
        word = sample_by_frequency(counts)
        selected_words.append(word)
    sentence = ' '.join(selected_words)
    # return HTML.format(sentence)
    return render_template('layout.html', sentence=sentence)
