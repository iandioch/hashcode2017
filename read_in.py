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
        self.requests = []
        # maps connected cache object to latency
        self.caches = {}

    def sort_requests_by_most_pop_to_least(self, _already_called=False):
        if not _already_called:
            self.requests = sorted(self.requests,
                                   key=lambda r: r.num_req,
                                   reverse=True)
            _already_called = True

    def get_caches_sorted_by_lowest_lat(self):
        return sorted(self.caches, key=lambda c: self.caches[c])

    def get_shortest_route_to(self, video_obj):
        best = self.dc_lat
        for cache in self.caches:
            if video_obj.i in cache.vid_ids:
                best = min(best, self.caches[cache])
        return best

    def vid_has_cached_route(self, video_obj):
        for cache in self.caches:
            if video_obj.i in cache.vid_ids:
                return True
        return False

class Request:
    def __init__(self, i, endp, r, video_obj):
        self.i = i
        self.endp_id = endp
        self.num_req = r
        self.video = video_obj

class Cache:
    def __init__(self, i, meg, endpoints):
        self.i = i
        self.remaining = meg
        self.vids = []
        self.vid_ids = set()

        # maps endpoint id to latency
        self.connected = {}
        for e in endpoints:
            for k, v in e.cache_lats:
                if k == self.i:
                    self.connected[e.i] = v

    def vid_fits(self, vid):
        return vid.meg <= self.remaining

    def add_video(self, video_obj):
        self.vids.append(video_obj)
        self.vid_ids.add(video_obj.i)
        self.remaining -= video_obj.meg

def read():
    V, E, R, C, X = map(int, input().split())
    videos = []
    for i, s in enumerate(map(int, input().split())):
        videos.append(Video(i, s))
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
        r = Request(Rv, Re, Rn, videos[Rv])
        requests.append(r)
        endpoints[Re].requests.append(r)

    # create cache objects
    caches = []
    for i in range(C):
        caches.append(Cache(i, X, endpoints))
    # build up (cache object: latency) dicts for each endpoint
    for e in endpoints:
        for c in e.cache_lats:
            e.caches[caches[c[0]]] = c[1]
    return V, E, R, C, X, videos, endpoints, requests, caches
