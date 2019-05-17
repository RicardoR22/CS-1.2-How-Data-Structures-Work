from flask import Flask, render_template
from histogram_functions import get_words
from higher_order_markov_chain import markov_chain, form_sentence
import random


app = Flask(__name__)


@app.route('/')
def hello_world():
    word_list = get_words('corpus.txt')
    chain = markov_chain(word_list)
    list_from_chain = list(chain)
    random_words = random.choice(list_from_chain)
    sentence = form_sentence(chain, random_words, 15)
    # return HTML.format(sentence)
    return render_template('layout.html', sentence=sentence)
