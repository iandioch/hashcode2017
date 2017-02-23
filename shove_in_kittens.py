from read_in import *

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests, caches= read()

    for cache in caches:
        cache.asked = {i:0 for i in range(V)}

    for e in endpoints:
        for cache in e.caches:
            for r in e.requests:
                cache.asked[r.video.i] += r.num_req/len(e.caches)

    for c in caches:
        asked = sorted(c.asked, key=lambda x: -c.asked[x])
        for i in asked:
            if videos[i].meg <= c.remaining:
                c.add_video(videos[i])
 
    print(len([c for c in caches if len(c.vids) > 0]))
    for cache in caches:
        if len(cache.vids) > 0:
            print(cache.i, ' '.join([str(v.i) for v in cache.vids]))
