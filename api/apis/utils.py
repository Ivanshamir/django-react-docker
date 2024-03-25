from django.core.cache import cache

def add_news_to_cache(news):
    print(news)
    cache.set('news', news)

def get_news_from_cache():
    cached_news_string = cache.get('news')
    return cached_news_string

def delete_news_from_cache():
    cache.delete('news')