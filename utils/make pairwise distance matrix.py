# Created by Medad Rufus Newman on 12/12/2019


from scipy import spatial
import pandas as pd



points_coordinate = [[0.181,14.9],
                     [9.06,9.40],
                     [9.38,29.6],
                     [10.0,9.77],
                     [14.0,0.915],
                     [14.5,10.1],
                     [14.9,11.8],
                     [16.5,10.9],
                     [19.0,22.4],
                     [19.1,15.6],
                     [20.0,6.26],
                     [21.6,10.8],
                     [24.1,17.3],
                     [24.5,18.1],
                     [26.3,9.85]]




matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')


points_coordinate_dict = {"Jones Branch Drive":[0.181,14.9],
                     'Ballston Metro': [9.06,9.40],
                     'Fishers Ln':[9.38,29.6],
                     'GMU / Fairfax Dr & Kenmore St':[10.0,9.77],
                     'Commerce St & Fayette St':[14.0,0.915],
                     'Lincoln Memorial':[14.5,10.1],
                     '20th & L St NW':[14.9,11.8],
                     '10th & E St NW':[16.5,10.9],
                     'Garland Ave & Walden Rd':[19.0,22.4],
                     'John McCormack Rd NE':[19.1,15.6],
                     'Stanton Square SE':[20.0,6.26],
                     'Kingman Island/The Fields at RFK':[21.6,10.8],
                     'Baltimore Ave & Jefferson St':[24.1,17.3],
                     'Riverdale Park Town Center':[24.5,18.1],
                     'Capitol Heights Metro':[26.3,9.85]}






df = pd.DataFrame(matrix,columns=points_coordinate_dict.keys())
df['names'] = points_coordinate_dict.keys()
print(df)
df.to_excel(excel_writer = "pairwise_matrix washington.xlsx")

