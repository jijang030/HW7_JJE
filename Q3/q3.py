def main():
    import numpy as np
    import pandas as pd
    arr=np.array([[100,25],[280,120],[900,30]])
    df=pd.DataFrame(arr,index=['store1','store2','store3'],columns=['unit price','number'])
    print(df)
    df['total price']=df['unit price']*df['number']
    print(df)
    df3=df.sort_values(by='total price',ascending=False)
    print(df3)

if __name__ == '__main__':
    main()
