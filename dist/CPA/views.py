# #
from bs4 import BeautifulSoup
import requests

# List of item names to search on eBay
name_list = ["Quran", "Programming Fundamental", "Calculator", "arduino", "gtx 1070",
             "bluetooth headphones", "coffee machine", "sweet tea", "Python textbook"]


# Returns a list of urls that search eBay for an item
def make_urls(names):
    # eBay url that can be modified to search for a specific item on eBay
    url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1312.R1.TR11.TRC2.A0.H0.XIp.TRS1&_nkw="
    # List of urls created
    urls = []

    for name in names:
        # Adds the name of item being searched to the end of the eBay url and appends it to the urls list
        # In order for it to work the spaces need to be replaced with a +
        urls.append(url + name.replace(" ", "+"))

    # Returns the list of completed urls
    return urls


# Scrapes and prints the url, name, and price of the first item result listed on eBay
def ebay_scrape(urls):
    for url in urls:
        # Downloads the eBay page for processing
        res = requests.get(url)
        # Raises an exception error if there's an error downloading the website
        res.raise_for_status()
        # Creates a BeautifulSoup object for HTML parsing
        soup = BeautifulSoup(res.text, 'html.parser')
        # Scrapes the first listed item's name
        # name = soup.find("h3", {"class": "s-item__title"}).get_text(separator=u" ")
        name = soup.find("h3", {"class": "s-item__title"}).get_text()
        # Scrapes the first listed item's price
        price = soup.find("span", {"class": "s-item__price"}).get_text()
        # review = soup.find("span", {"class": "s-item__reviews"}).get_text()
        # review= soup.find("div", class_='s-item__reviews').get_text()
        # Prints the url, listed item name, and the price of the item
        #  print(url)
        print("Item Name: " + name)
        print("Price: " + price )
        # print("Review: " + review+"\n")
        # aa=soup.find('div')['class']
        # print(soup.find("div",class_='s-item__reviews').get_text())

# Runs the code
# 1. Make the eBay url list
# 2. Use the returned url list to search eBay and scrape and print information on each item
# ebay_scrape(make_urls(name_list))







from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.shortcuts import render
# from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json
from django.views.decorators.csrf import csrf_exempt

from decimal import Decimal
from django.conf import settings
from django.urls import reverse
from django.shortcuts import  render,get_object_or_404
# from paypal.standard.forms import PayPalPaymentsForm

from  subprocess import run ,PIPE
import sys
# from PayTm import Checksum
# Create your views here.
from django.http import HttpResponse
MERCHANT_KEY = 'Your-Merchant-Key-Here'

class Passvalue:
    varValue=0





def index(request):

    return render(request, 'CPA/index.html')

def FeaturedReviews(request):
    return render(request, 'CPA/FeaturedReviews.html')
def Explore(request):
    return render(request, 'CPA/Explore.html')



def SearchProduct(request):
    # thank = False
    if request.method=="POST":

        name = request.POST.get('name','')
        Passvalue.varValue=name
        # name = request.POST.get('name', '')
        # email = request.POST.get('email', '')
        # phone = request.POST.get('phone', '')
        # desc = request.POST.get('desc', '')
        # contact = Contact(name=name, email=email, phone=phone, desc=desc)
        # contact.save()
        # thank = True
        param={'get_from_textBox_var_name':name}
        ebay_scrape(make_urls(param))
        print("My name is "+ name)
    return render(request, 'CPA/SearchProduct.html',param)

def OutSearchProduct(request):
    # thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        # email = request.POST.get('email', '')
        # phone = request.POST.get('phone', '')
        # desc = request.POST.get('desc', '')
        # contact = Contact(name=name, email=email, phone=phone, desc=desc)
        # contact.save()
        # thank = True

    return render(request, 'CAP/index.html')
    out =run(sys.executable,{"..\\...\\Consensou\\test.py",name},shell=false,stout=PIPE)
    print(out)
