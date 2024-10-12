def construct_cache_key(path, query_string):
    return f"{path}?{query_string}"

def add_cache_headers(response, cache_hit):
    response.headers['X-Cache'] = 'HIT' if cache_hit else 'MISS'
    return response