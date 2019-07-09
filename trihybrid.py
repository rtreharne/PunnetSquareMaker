import punnetsquaremaker_python3 as ps

key_dict_1 = {0: 'U',
            1: 'W',
            2: 'Y',}

key_dict_2 = {0: 'V',
              1: 'X',
              2: 'Z'}

def dict_from_parents(p1, p2):
    p1 = p1.split(';')
    p2 = p2.split(';')

    d1 = {}
    d2 = {}

    P1, D1 = encode_genotype(p1, key_dict_1)
    P2, D2 = encode_genotype(p2, key_dict_2)

    filter_d2 = {k:v for k,v in D2.items() if v not in D1.values()}
    
    master_dict = {**D1, **D2}

    return P1, P2, master_dict

def print_genotypes(table, key):
    print(key)
    for line in table: 
        line = line.split(" ")[0]
        line = line.replace("\n", "")
        line = [key[x] for x in sorted(line)]
        chunks = [','.join(line[i:i+2]).replace(",", "/") for i in range(0, len(line), 2)]
        print(",".join(chunks).replace(",", ";"))
   

def encode_genotype(p, k):
    P = ''    
    tdict = {}
    for i, c in enumerate(p):
        csplit = c.split('/')
        if csplit[0] == csplit[1]:
            P += k[i]
            P += k[i]
            tdict[k[i]] = csplit[0]
           
        else:
            P += k[i]
            P += k[i].lower()
            tdict[k[i]] = csplit[0]
            tdict[k[i].lower()] = csplit[1]

        P += " "
    
    return P.strip(" ").split(" "), tdict
        

if __name__ == "__main__":
    parent_1 = "alpha/alpha;beta/omega;+/+"
    parent_2 = "+/Y;beta/omega;delta/epsilon"
    p1, p2, md  = dict_from_parents(parent_1, parent_2)
    c1 = ps.get_all_combinations(p1)
    c2 = ps.get_all_combinations(p2)
    a = ps.make_table(c1, c2)
    latextable = ps.print_table(a, c1, c2)
    freqtable = ps.print_genotype_frequencies(a)
    print_genotypes(freqtable, md)
    print(p1, p2)

    
