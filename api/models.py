from django.db import models
from django.db.models.signals import post_save 

import re 

class Appearance(models.Model): 
  listing = models.ForeignKey('Listing') 
  word = models.ForeignKey('Word', related_name='appearances')
  location = models.IntegerField()
  section = models.CharField(max_length=255)

class Word(models.Model): 
  content = models.CharField(max_length=255)
  listings = models.ManyToManyField('Listing', through='Appearance')


class Listing(models.Model): 
  summary = models.TextField()
  title = models.CharField(max_length=255)
  published = models.DateTimeField()
  url = models.CharField(max_length=255)

# These are routines are here to, 
# upon creation of a listing,   
# split it up into various Appearances and, 
# as necessary, Words.    

def tokenize_text(text):
  print(text) 
  text = text.lower()
  text = re.sub(r'<a.*?>|</a>', '', text) # strip a tags 
  text = re.sub(r'[\-/]', ' ', text) 
  text = re.sub(r'[.():,!?\[\]\+]+', '', text)
  text = re.sub(r'&#x\d{4};\d{1,3}', '', text) # &#0032;123
  words = text.split() 
  print(words)  
  return words 


def index_section(instance, words, section_name): 
  word_location = 0 
  for word in words:

    word_exists = Word.objects.filter(content=word).exists() 

    word_model = False 

    if (word_exists):
      word_model = Word.objects.get(content=word)
    else: 
      word_model = Word(content=word)
      word_model.save() 

    Appearance(word=word_model, listing=instance, section=section_name, location=word_location).save()

    word_location += 1  

def index_listing(sender, instance, **kwargs):
  title_words = tokenize_text(instance.title)
  summary_words = tokenize_text(instance.summary)

  # must be in same order 
  sets_of_words = [title_words, summary_words]
  sections_for_sets = ['title', 'summary']

  for set_of_words in sets_of_words:  
    for section_for_set in sections_for_sets: 
      index_section(instance, set_of_words, section_for_set)

post_save.connect(index_listing, sender=Listing)