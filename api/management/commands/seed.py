from django.core.management.base import BaseCommand 
import feedparser 

from api.models import Listing 


class Command(BaseCommand): 

  def handle(self, *args, **options): 
    craigslist = 'http://newyork.craigslist.org/search/vga?format=rss'

    data = feedparser.parse(craigslist) 
    listings_data = data['entries']

    for listing_data in listings_data: 
      Listing(summary=listing_data['summary'], title=listing_data['title'], url=listing_data['link'], published=listing_data['published']).save()