out = open('links.tex', 'wt')
with open('links.txt', 'rt') as file:
    n = 0
    for line in file:
        link = line.split(' ')[:-1]
        if link:
            n +=1
            out.write(f'$L_{{{n}}}$ $')
            for tgl in link:
                if tgl == 'ah':
                    out.write('\\alpha_{2n}^h ')
                elif tgl == 'av':
                    out.write('\\alpha_{2n}^v ')
                elif tgl == 'rh':
                    out.write('\\bar{\\alpha}_{2n}^h ')
                elif tgl == 'rv':
                    out.write('\\bar{\\alpha}_{2n}^v ')
                elif tgl == 'bh':
                    out.write('\\beta_{2n-1}^h ')
                elif tgl == 'gv':
                    out.write('\\gamma_{2n-1}^v ')
            out.write('$ ')
            if n % 2 == 0:
                out.write('\n')
out.close()