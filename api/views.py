from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict  

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

def search_listings(request):
  
  query_string = request.GET.get('q')
  words = query_string.lower().split() 

  # important intial callback for map 

  def get_word_model(word): 
    word_exists = Word.objects.filter(content=word).exists()

    if (word_exists):
      return Word.objects.get(content=word)
    else:
      return None 

  word_models = list(map(get_word_model, words))  

  # various callbacks for map 

  def get_listings_sets(word_model):
    return set(word_model.listings.all()) 

  def get_listings_lists(word_model):
    return list(word_model.listings.all())

  def get_listing_values(listing_model):
    return model_to_dict(listing_model) 

    # if no record of that word 
  if (None in word_models):

    listings = []
    # otherwise process one word and more
    # differently   
  elif (len(word_models) < 2):

    all_listings = sum(list(map(get_listings_lists, word_models)), [])  

    listings = list(map(get_listing_values, list(set(all_listings)))) 

  else: 
  
    words_listings = list(map(get_listings_sets, word_models)) 
 
    listings_with_all_words = \
    words_listings[0].intersection(*words_listings[1:]) 

    listings = \
    list(map(get_listing_values, listings_with_all_words))
   

  return JsonResponse(listings, safe=False)