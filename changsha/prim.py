 def Prim(i, j,d,n, w, c):
    while i < n:
        m=0
        s=0
        t=0
        for j in range(n):
            if c[i][j]!=1 and w[i][j]!=0:
                    t=w[i][j]
                    m=i
                    s=j
                    h=j+1
                    for h in range(n):
                        if  w[i][h] <= t and c[i][h]!=1 and w[i][j]!=0:
                            t=w[i][j]
                            m=i
                            s=j
        d+=t

        if c[m][s]==1:
            break
        else:
            c[m][s]=1
            c[s][m]=1
            i=s
    return d