def gen(orient):
    tbls = []
    for i in range(2 ** 9):
        tbl = []; b = "{0:09b}".format(i); cnt = 0
        for o in orient:
            if o == 'a':
                tbl.append('ah' if b[cnt] == '0' else 'av')
            elif o == 'r':
                tbl.append('rh' if b[cnt] == '0' else 'rv')
            elif o == 'b':
                tbl.append('bh')
            elif o == 'g':
                tbl.append('gv')
            cnt += 1
        tbls.append(tbl)
    return tbls

def rot(tbl, flag):
    if (flag == 0):
        return tbl
    elif (flag == 1):
        return [tbl[2], tbl[0], tbl[1], tbl[5], tbl[3], tbl[4], tbl[8], tbl[6], tbl[7]]
    elif (flag == 2):
        return [tbl[1], tbl[2], tbl[0], tbl[4], tbl[5], tbl[3], tbl[7], tbl[8], tbl[6]]
    elif (flag == 3):
        return [tbl[8], tbl[7], tbl[6], tbl[4], tbl[3], tbl[5], tbl[2], tbl[1], tbl[0]]
    elif (flag == 4):
        return [tbl[7], tbl[6], tbl[8], tbl[3], tbl[5], tbl[4], tbl[1], tbl[0], tbl[2]]
    elif (flag == 5):
        return [tbl[6], tbl[8], tbl[7], tbl[5], tbl[4], tbl[3], tbl[0], tbl[2], tbl[1]]

def equ(e, x):
    tag = False
    for i in range(6):
        if e == rot(x, i):
            tag = True
            break
    return tag

def rmv(tbls):
    for i in range(2 ** 9):
        if i < len(tbls) - 1:
            tbls = tbls[:i + 1] + [e for e in tbls[i + 1:] if not equ(e, tbls[i])]
        else:
            break
    return tbls

def fpr(out, tbls):
    for tbl in tbls:
        for tgl in tbl:
            out.write(f'{tgl} ')
        out.write('\n')
    out.write('\n')

if __name__ == '__main__':
    orients = open('orients.txt', 'rt').read().split('\n')
    out = open('links.txt', 'wt')
    for orient in orients:
        tbls = gen(orient)
        tbls = rmv(tbls)
        fpr(out, tbls)
    out.close()