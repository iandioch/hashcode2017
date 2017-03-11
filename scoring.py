import sys
from math import floor

class Cache:
    def __init__(self):
        self.vids = set()

    def has_vid(self, vid):
        return vid in self.vids

    def add_vids(self, vids):
        self.vids.update(vids)

class Endpoint:
    def __init__(self, Ld):
        # List of request objs
        self.requests = []
        # Caches
        self.caches = []
        # Cache obj to latency
        self.cache_lat = {}
        # Latency to DC
        self.dc_lat = Ld

    def add_request(self, r):
        self.requests.append(r)

    def add_cache(self, c, lc):
        self.caches.append(c)
        self.cache_lat[c] = lc

    def find_lat_saved(self):
        lat_saved = 0
        for r in self.requests:
            lat_saved += (self.dc_lat - self.min_request_route(r)) * r.num
        return lat_saved

    def min_request_route(self, r):
        c_with_vid = [self.cache_lat[c] for c in self.caches if c.has_vid(r.vid)]
        return min(c_with_vid) if c_with_vid else self.dc_lat


class Request:
    def __init__(self, vid, num):
        self.vid = vid
        self.num = num

if __name__ == '__main__':

    in_file = sys.argv[1]
    out_file = sys.argv[2]

    with open(in_file, 'r') as f:
        V, E, R, C, X = map(int, f.readline().split())
        total_reqs = 0
        caches = [Cache() for _ in range(C)]
        f.readline()  # Video sizes
        endpoints = []
        for _ in range(E):
            Ld, K = map(int, f.readline().split())
            endp = Endpoint(Ld)
            for _ in range(K):
                c, Lc = map(int, f.readline().split())
                endp.add_cache(caches[c], Lc)
            endpoints.append(endp)
        for _ in range(R):
            v_id, e_id, num = map(int, f.readline().split())
            total_reqs += num
            endpoints[e_id].add_request(Request(v_id, num))


    with open(out_file, 'r') as f:
        ls = f.readlines()
        for l in ls[1:]:
            c, *vids = map(int, l.split())
            caches[c].add_vids(vids)

    total_lat_saved = 0
    for e in endpoints:
        total_lat_saved += e.find_lat_saved()

    print(floor(total_lat_saved * 1000 / total_reqs))
