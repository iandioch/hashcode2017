from read_in import *

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests, caches = read()
    
    for cache in caches:
        vids_wanted = {}
        for endp in cache.endpoints:
            lat_to_endp = cache.connected[endp.i]
            for vid, num_req in endp.get_wanted_vids(lat_to_endp).items():
                if vid in vids_wanted:
                    vids_wanted[vid] += num_req
                else:
                    vids_wanted[vid] = num_req
        vids_best_to_worst = sorted(
            vids_wanted,
            key=lambda v: vids_wanted[v],
            reverse=True)
        for vid in vids_best_to_worst:
            if cache.vid_fits(vid):
                cache.add_video(vid)

    print(len([c for c in caches if len(c.vids)]))
    for cache in caches:
        if len(cache.vids) == 0:
            continue
        print(cache.i, ' '.join([str(vid.i) for vid in cache.vids]))