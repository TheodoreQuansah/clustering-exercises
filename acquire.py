import os
import pandas as pd

from env import get_connection



def get_properties_2017():
    
    # Define the filename for the CSV file
    filename = 'properties_2017.csv'
    
    # Check if the CSV file already exists
    if os.path.isfile(filename):
        # If the file exists, read it into a DataFrame and return it
        return pd.read_csv(filename)
    else:
        # If the file doesn't exist, define an SQL query to retrieve data
        query = '''
                SELECT *
                FROM properties_2017
                LEFT JOIN predictions_2017 ON predictions_2017.parcelid = properties_2017.parcelid
                LEFT JOIN properties_2016 ON properties_2016.parcelid = predictions_2017.parcelid
                LEFT JOIN predictions_2016 ON predictions_2016.parcelid = properties_2016.parcelid
                LEFT JOIN airconditioningtype ON airconditioningtype.airconditioningtypeid = properties_2017.airconditioningtypeid
                LEFT JOIN architecturalstyletype ON architecturalstyletype.architecturalstyletypeid = properties_2017.architecturalstyletypeid
                LEFT JOIN buildingclasstype ON buildingclasstype.buildingclasstypeid = properties_2017.buildingclasstypeid
                LEFT JOIN heatingorsystemtype ON heatingorsystemtype.heatingorsystemtypeid = properties_2017.heatingorsystemtypeid
                LEFT JOIN propertylandusetype ON propertylandusetype.propertylandusetypeid = properties_2017.propertylandusetypeid
                LEFT JOIN storytype ON storytype.storytypeid = properties_2017.storytypeid
                LEFT JOIN typeconstructiontype ON typeconstructiontype.typeconstructiontypeid = properties_2017.typeconstructiontypeid
                LEFT JOIN unique_properties ON unique_properties.parcelid = properties_2017.parcelid
                WHERE predictions_2017.transactiondate >= '2017-01-01' AND predictions_2017.transactiondate
                AND properties_2017.latitude IS NOT NULL AND properties_2017.longitude IS NOT NULL
                ORDER BY properties_2017.id
                '''
        
        # Get a connection URL (you may want to define the 'get_connection' function)
        url = get_connection('zillow')  # You'll need to define this function
        
        # Execute the SQL query and read the result into a DataFrame
        df = pd.read_sql(query, url)
        
        # Save the result to a CSV file
        df.to_csv(filename, index=False)

        # Return the DataFrame
        return df




def summary(df):
    info = pd.DataFrame(df.info())
    dtypes = pd.DataFrame(df.dtypes)
    shape = pd.DataFrame(df.shape)
    value_counts = pd.DataFrame(df.describe())
    return info, dtypes, shape, value_counts