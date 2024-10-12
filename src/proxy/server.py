from flask import Flask, request, Response
import requests
from .cache import Cache
from .utils import construct_cache_key, add_cache_headers

app=Flask(__name__)
cache=Cache()

def create_proxy_app(origin_url):
    @app.route('/', defaults={'path':''})
    @app.route('/<path:path>')
    def proxy(path):
        cache_key=construct_cache_key(path,request.query_string.decode())
        cached_response=cache.get(cache_key)
        if cached_response:
            response=Response(cached_response)
            return add_cache_headers(response,True)
        
        url = f"{origin_url}/{path}"
        response = requests.get(url, params=request.args)
        
        cache.set(cache_key, response.content)
        return (response.content, response.status_code, response.headers.items())
    return app

        