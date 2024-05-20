import pandas
from IPython.display import display

df = pandas.read_csv('TaxiDatset.csv')
display(df)
print('\n\n\n')
average_distance = df['trip_distance'].mean()
print(f'Average distance of Taxi trips: {average_distance} miles')
max_total_amount = df['total_amount'].max()
print(f"Max value of paid cash: {max_total_amount:.2f}$")
print('\nInformation about first row in dataset:')
print(df.loc[0])
