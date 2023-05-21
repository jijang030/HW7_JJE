def main():
    import numpy as np
    docs=np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    query=np.array([1,1,0,0,1,0])
    n=len(docs)
    #print(docs[0])
    cos_sim=[]
    for i in range(n):
        c=np.dot(docs[i],query)/(np.linalg.norm(docs[i])*np.linalg.norm(query))
        cos_sim.append(float(c))

    print(f"Docs1={cos_sim[0]:.2f}")
    print(f"Docs2={cos_sim[1]:.2f}")
    print(f"Docs3={cos_sim[2]:.2f}")


if __name__ == '__main__':
    main()
