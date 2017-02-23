from read_in import *

if __name__ == '__main__':
    V, E, R, C, X, videos, endpoints, requests = read()
    in_cache = []
    cache_left = X
    i = 0
    while True:
        if i >= len(videos):
            break
        if videos[i].meg <= cache_left: 
            in_cache.append(videos[i])
            cache_left -= videos[i].meg
        i += 1
    print(C)
    for i in range(C):
        print(i, ' '.join([str(v.i) for v in in_cache]))
