class Video:
    def __init__(self, i, meg):
        self.meg = meg
        self.i = i

class Endpoint:
    def __init__(self, i, Ld, K, cache_lats):
        self.i = i
        self.dc_lat = Ld
        self.num_cache = K
        # List of pairs: cache server ID, latency
        self.cache_lats = cache_lats

class Request:
    def __init__(self, i, endp, r):
        self.i = i
        self.endp_id = endp
        self.num_req = r

def read():
    V, E, R, C, X = map(int, input().split())
    videos = []
    for i in range(V):
        videos.append(Video(i, int(input())))
    endpoints = []
    for i in range(E):
        Ld, K = map(int, input().split())
        cache_lats = []
        for k in range(K):
            cache_lats.append(tuple(map(int, input().split())))
        endpoints.append(Endpoint(i, Ld, K, cache_lats))
    requests = []
    for i in range(R):
        Rv, Re, Rn = map(int, input().split())
        requests.append(Request(Rv, Re, Rn))
    return V, E, R, C, X, videos, endpoints, requests
