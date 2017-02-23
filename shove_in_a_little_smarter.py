from read_in import *
import sys

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests, caches = read()
    skip = set()
    vids_cached = [set() for e in endpoints]
    changed = True
    while changed:
        print("Iterating", file=sys.stderr)
        changed = False
        for cache in caches:
            if cache in skip:
                print("skipping cache", file=sys.stderr)
                continue
            # the number of endpoints that currently can't access
            # a given video by a cache
            endpoints_changed = {}

            for endpoint_id in cache.connected:
                endpoint = endpoints[endpoint_id]
                for request in endpoint.requests:
                    vid = request.video
                    if vid in vids_cached[endpoint_id]:
                        continue
                    if vid.meg > cache.remaining:
                        continue
                    if endpoint.get_shortest_route_to(vid) == endpoint.dc_lat:
                        if vid in endpoints_changed:
                            endpoints_changed[vid] += 1
                        else:
                            endpoints_changed[vid] = 1
            if len(endpoints_changed) == 0:
                skip.add(cache)
                continue
            changed = True
            best = max(endpoints_changed, key=lambda x: endpoints_changed[x])
            for endpoint_id in cache.connected:
                vids_cached[endpoint_id].add(best)
                
            cache.add_video(best)
    print(len([c for c in caches if len(c.vids) > 0]))
    for cache in caches:
        print(cache.i, ' '.join([str(v.i) for v in cache.vids]))
