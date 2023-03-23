from typing import List, Set, Tuple, Dict

def get_suf(s: str):
    return s[1:]

def get_pref(s: str):
    return s[:-1]

def main():
    input_s: List[str] = list(map(str, input().split()))

    n: int = 0
    for el in input_s:
        n = max(n, len(el))

    vertexes: List[Set[str]] = [set() for el in range(n + 1)]
    vertexes[0].add("")
    prev_vertex: Dict[str, List[str]] = dict()
    next_vertex: Dict[str, List[str]] = dict()

    last_lvl: Set[str] = set()
    cur_lvl: Set[str] = set()
    for el in input_s:
        last_lvl.add(el)
    while True:
        cur_lvl.clear()
        for el in last_lvl:
            vertexes[len(el)].add(el)
            if get_pref(el) not in next_vertex.keys():
                next_vertex[get_pref(el)] = [el]
            else:
                next_vertex[get_pref(el)].append(el)

            if get_suf(el) not in prev_vertex.keys():
                prev_vertex[get_suf(el)] = [el]
            else:
                prev_vertex[get_suf(el)].append(el)

            if el not in next_vertex.keys():
                next_vertex[el] = [get_suf(el)]
            else:
                next_vertex[el].append(get_suf(el))
            
            if el not in prev_vertex.keys():
                prev_vertex[el] = [get_pref(el)]
            else:
                prev_vertex[el].append(get_pref(el))
            cur_lvl.add(get_pref(el))
            cur_lvl.add(get_suf(el))

        last_lvl.clear()
        for el in cur_lvl:
            last_lvl.add(el)
        res: List[str] = []
        for el in last_lvl:
            res.append(el)
        if len(res) == 1 and res[0] == '':
            break
    
    d: Dict[str, List[int]] = dict()
    for lvl in vertexes:
        for el in lvl:
            d[el] = [0, 0]
    #d[el][0] - входящие, d[el][1] - исходящие

    for lvl in range(n, -1, -1):
        for el in vertexes[lvl]:
            if el in input_s:
                d[el] = [len(prev_vertex[el]), len(next_vertex[el])]
                for prev in prev_vertex[el]:
                    d[prev][1] += 1
                for next in next_vertex[el]:
                    d[next][0] += 1
            else:
                if d[el][0] < d[el][1]:
                    possible: str = ""
                    for x in prev_vertex[el]:
                        if len(x) < len(el):
                            possible = x
                            break
                    d[possible][1] += d[el][1] - d[el][0]
                    d[el][0] = d[el][1]
                elif d[el][0] > d[el][1]:
                    possible: str = ""
                    for x in next_vertex[el]:
                        if len(x) < len(el):
                            possible = x
                            break
                    d[possible][0] += d[el][0] - d[el][1]
                    d[el][1] = d[el][0]
    cnt: int = 0
    for el in d.values():
        cnt += el[1]
    print(cnt // 2)

if __name__ == '__main__':
    main()
