# caching-proxy
a CLI tool that starts a caching proxy server, it will forward requests to the actual server and cache the responses.

caching-proxy/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── proxy/
│   │   ├── __init__.py
│   │   ├── server.py
│   │   ├── cache.py
│   │   └── utils.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   ├── test_server.py
│   ├── test_cache.py
│   └── test_utils.py
├── requirements.txt
├── setup.py
└── README.md