import argparse
from src.proxy.server import create_proxy_app
from src.proxy.cache import Cache
from src.config.settings import Config

def main():
    parser = argparse.ArgumentParser(description="Caching Proxy Server")
    parser.add_argument("--port", type=int, config=Config.DEFAULT_PORT,help="port to run the server")
    parser.add_argument("--origin", type=str,default=Config.DEFAULT_ORIGIN, help="Origin server url")
    parser.add_argument("--clear-cache", action="store_true", help="clear cache")

    args = parser.parse_args()

    if args.clear_cache():
        Cache.clear()
        print("Cache deleted")
        return
    
    app=create_proxy_app(args.origin)
    print(f"Starting proxy server on port {args.port}, forwarding to {args.origin}")
    app.run(debug=True)

if __name__ == "__main__":
    main()