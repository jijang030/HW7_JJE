def main():
    import numpy as np
    import pandas as pd
    df=pd.read_csv('gender2.csv',encoding='ANSI')
    #print(df)
    df2=pd.concat([df['2022년_계_총인구수'],df['2022년_남_총인구수'],df['2022년_여_총인구수']],axis=1)
    a=df2.to_numpy()
    df3=pd.DataFrame(a,index=df['행정구역'],columns=['Total','Male','Female'])
    #print(df2)
    print("\n\nNew DataFrame:")
    print(df3)


if __name__ == '__main__':
    main()
