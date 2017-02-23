from read_in import *

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests, caches = read()
    for e in endpoints: 
        for r in e.requests:
            if e.get_shortest_route_to(r.video) == e.dc_lat:
                d = e.get_shortest_route_to(r.video)
                if d == e.dc_lat:
                    connected_caches = sorted(e.caches.keys(), key=lambda x:e.caches[x])
                    for cache in connected_caches:
                        if cache.remaining >= r.video.meg:
                            cache.add_video(r.video)
                            break
    print(len([c for c in caches if len(c.vids) > 0]))
    for cache in caches:
        print(cache.i, ' '.join([str(v.i) for v in cache.vids]))
