from django.db import models
from django.db.models.signals import post_save 


class Appearance(models.Model): 
  listing = models.ForeignKey('Listing') 
  word = models.ForeignKey('Word')
  location = models.IntegerField()
  section = models.CharField(max_length=255)

class Word(models.Model): 
  content = models.CharField(max_length=255)

class Listing(models.Model): 
  summary = models.TextField()
  title = models.CharField(max_length=255)
  published = models.DateTimeField()
  url = models.CharField(max_length=255)

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
  title_words = instance.title.lower().split() 
  summary_words = instance.summary.lower().split() 

  # must be in same order 
  sets_of_words = [title_words, summary_words]
  sections_for_sets = ['title', 'summary']

  for set_of_words in sets_of_words:  
    for section_for_set in sections_for_sets: 
      index_section(instance, set_of_words, section_for_set)

post_save.connect(index_listing, sender=Listing)