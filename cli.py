import argparse
from flask import Flask, request, Response
import requests
import redis
import json

def create_app(args):
    app = Flask(__name__)
    cache = redis.StrictRedis(host='localhost', port=6379, db=0)

    @app.route("/", defaults={'path': ''})
    @app.route('/<path:path>', methods=['GET'])
    def proxy(path):
        cache_key = f"{path}?{request.query_string.decode()}"
        cached_response = cache.get(cache_key)
        if cached_response:
            cached_data = json.loads(cached_response)
            return Response(
                cached_data['content'],
                status=cached_data['status_code'],
                headers=cached_data['headers'] + [('X-Cache', 'HIT')]
            )

        origin_url = f"{args.origin}/{path}"
        response = requests.get(origin_url, params=request.args)

        cache_value = json.dumps({
            'status_code': response.status_code,
            'headers': list(response.headers.items()),
            'content': response.content.decode('utf-8', errors='replace')
        })
        cache.set(cache_key, cache_value)

        return Response(
            response.content,
            status=response.status_code,
            headers=list(response.headers.items()) + [('X-Cache', 'MISS')]
        )

    return app

def parser_arguments():
    parser = argparse.ArgumentParser(description="Caching Proxy Server")
    parser.add_argument("--port", type=int, default=3000, help="port number to run the server on")
    parser.add_argument("--origin", type=str, required=True, help="origin server url to forward requests to")
    parser.add_argument("--clear-cache", action="store_true", help="Clear the cache before starting the server")
    return parser

def main():
    parser = parser_arguments()
    args = parser.parse_args()
    
    cache = redis.StrictRedis(host='localhost', port=6379, db=0)
    if args.clear_cache:
        cache.flushdb()
    
    app = create_app(args)
    app.run(port=args.port)

if __name__ == "__main__":
    main()