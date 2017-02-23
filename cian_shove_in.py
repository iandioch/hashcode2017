from read_in import *

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests, caches = read()
    caches_full = False
    while not caches_full:
        caches_full = True
        for endp in endpoints:
            endp.sort_requests_by_most_pop_to_least()
            # Find best vid not cached already
            for req in endp.requests:
                if endp.vid_has_cached_route(req.video):
                    continue
                # Find a cache to fit this vid
                for cache in endp.get_caches_sorted_by_lowest_lat():
                    if cache.vid_fits(req.video):
                        cache.add_video(req.video)
                        caches_full = False
                        break
                break
    print(len([c for c in caches if len(c.vids)]))
    for cache in caches:
        if len(cache.vids) == 0:
            continue
        print(cache.i, ' '.join([str(vid.i) for vid in cache.vids]))
