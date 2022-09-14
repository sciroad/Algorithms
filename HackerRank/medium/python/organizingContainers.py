def organizingContainers(container):
    total_c=[]
    cap_dict={}
    for i in range(len(container)):
        t_r=0
        t_c=0
        for j in range(len(container)):
            t_c+=container[j][i]
            t_r+=container[i][j]
        if t_r not in cap_dict:
            cap_dict[t_r]=0
        cap_dict[t_r]+=1
        total_c.append(t_c)
    for t_c in total_c:
        if cap_dict[t_c]==0:
            return "Impossible"
        cap_dict[t_c]-=1
    return "Possible"

container=[[1,1],[1,1]]
print(organizingContainers(container))