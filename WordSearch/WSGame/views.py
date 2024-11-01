from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .wordBank import WordBank

# Create your views here.
# will server http requests 

# function will represent a "view"
def home(response):
    bank=WordBank()
    bank.get_words('Sports',5,8)

    
    return render(response,'./home.html',{"matrix":bank.create_word_matrix(10)}) #create a 10 x 10 matrix

