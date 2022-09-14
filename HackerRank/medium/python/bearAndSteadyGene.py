def steadyGene(gene):
    # Write your code here
    count = len(gene)//4
    d = {'A': 0, 'G': 0, 'C': 0, 'T': 0}
    print(count)
    def check(d):
        for i in d.values():
            if i > count:
                return False
        return True

    for ch in gene:
        d[ch] += 1
    print(d)
    if check(d):
        return 0

    head = 0
    tail = 0
    result = len(gene)

    for head in range(len(gene)):
        d[gene[head]] -= 1
        if check(d):
            print("head: ",head)
            while tail < head:
                d[gene[tail]] += 1
                if d[gene[tail]] > count:
                    break
                tail += 1
            print("tail:",tail)
            dif = head-tail+1
            if dif < result:
                result = dif
            tail += 1
    return result


print(steadyGene("TGATGCCGTCCCCTCAACTTGAGTGCTCCTAATGCGTTGC"))
