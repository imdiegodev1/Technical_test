import pandas as pd
import numpy as np

def main():
    df = the_function('astronauts_wrangling.csv')

    return df


def the_function(file_name = str):

    ##Read csv file
    df = pd.read_csv(f'./{file_name}')
    
    #Work just with the neccesary columns
    df_f = df[['country', 'missions', 'days in space', 'spacewalks']]

    ##grouping by country and use aggregaton functions to get average number of missions, days in space
    ##and total spacewalks (I asume that spacewalks = astronauts in space)
    df_g = df_f.groupby(['country']).agg({'missions': np.mean,
                                            'days in space': np.mean,
                                            'spacewalks': np.sum})

    total_spacewalks = df_g['spacewalks'].sum()
    df_g['percentage_astronauts'] = (df_g['spacewalks']/total_spacewalks)*100

    ##get company that has sent the most missions by country
    df_fixed2 = df[['country', 'missions', 'company space agency']]
    df_g2 = df_fixed2.groupby(['country', 'company space agency']).agg({'missions': np.sum}).reset_index()
    df_gf=df_g2.sort_values('missions', ascending=False).drop_duplicates('country').sort_index()

    ##get main achievement by country (i'll work just with 'achievement 1')
    df_fixed3 = df[['country', 'acheivement 1']]
    df_fixed3['count1'] = 1
    df_gf2 = df_fixed3.groupby(['country', 'acheivement 1'])['count1'].sum().reset_index()

    ##Merging all the data in a single df
    df_f1 = df_g.merge(df_gf, left_on='country', right_on='country')
    df_f2 = df_f1.merge(df_gf2, left_on='country', right_on='country')

    ##Remove unnecesary columns
    df_final = df_f2.drop(['missions_y', 'count1', 'spacewalks'], axis=1)

    return df_final


if __name__ == '__main__':
    df = main()

    print(df.head())