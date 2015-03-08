from django.shortcuts import render
from django.http import JsonResponse 

from api.models import Word, Listing, Appearance

def index_words(request): 
  words = list(Word.objects.values())
  return JsonResponse(words, safe=False)

def index_listings(request):
  listings = list(Listing.objects.values())
  return JsonResponse(listings, safe=False)

def index_appearances(request): 
  appearances = list(Appearance.objects.values()) 
  return JsonResponse(appearances, safe=False)
