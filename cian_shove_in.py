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
                caches_best_to_worst = sorted(
                    endp.caches.keys(),
                    key=lambda c: c.get_lat_saved_by_adding_vid(req.video),
                    reverse=True)
                for cache in caches_best_to_worst:
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
