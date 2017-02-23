from read_in import *

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests, caches = read()
    changed = True
    while changed:
        changed = False
        for cache in caches:
            # find the vid that would make the biggest diff if saved here
            vid_diffs = {}
            for video in videos:
                if (video.meg > cache.remaining):
                    continue
                diff = 0
                # find the diff this vid would make if put here
                for endpoint_id in cache.connected:
                    curr = endpoints[endpoint_id].get_shortest_route_to(video)
                    better = cache.connected[endpoint_id]
                    if (curr - better) > 0:
                        diff += (curr-better)
                vid_diffs[video] = diff
            if vid_diffs:
                vid = max(vid_diffs, key=lambda x: vid_diffs[x])
                cache.add_video(vid)
                changed = True
    print(len([c for c in caches if len(c.vids) > 0]))
    for cache in caches:
        print(cache.i, ' '.join([str(v.i) for v in cache.vids]))
