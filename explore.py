import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import pearsonr, f_oneway


def explore_bedrooms(df):

    print('Null hypothesis: The number of bedrooms has no correlation with logerror')
    print('Alternative hypothesis: The number of bedrooms has a correlation with logerror')
    print('BAR PLOT')
    # Scatter plot of bedrooms vs. logerror
    sns.barplot(data=df, x='bedroomcnt', y='logerror', errorbar = None)
    plt.title('Bedrooms vs. Logerror')
    plt.show()

    print('PEARSONR TEST')
    # Calculate correlation between bedrooms, bathrooms, and logerror
    bedrooms_corr, p = pearsonr(df['bedroomcnt'], df['logerror'])
    
    print(f'We reject the null hypothesis with a correlation of {bedrooms_corr} and a p_value of {p}')


def square_footage_vs_logerror(df):

    print('Null hypothesis: There is no relationship between the porpertys calculated square footage and logerror')
    print('Alternative hypothesis: There is a relationship between the porpertys calculated square footage and logerror')
    print('SCATTER PLOT')
    # Scatter plot of calculated square footage vs. logerror
    sns.scatterplot(data=df, x='calculatedfinishedsquarefeet', y='logerror')
    plt.title('Square Footage vs. Logerror')
    plt.show()

    print('PEARSONR TEST')
    # Calculate correlation between square footage and logerror
    correlation, p = pearsonr(df['calculatedfinishedsquarefeet'], df['logerror'])
    
    print(f'We reject the null hypothesis with a correlation of {correlation} and a p_value of {p}')


def explore_bathrooms(df):

    print('Null hypothesis: The number of bathrooms has no correlation with logerror')
    print('Alternative hypothesis: The number of bathrooms has a correlation with logerror')
    print('BAR PLOT')
    # Scatter plot of bedrooms vs. logerror
    sns.barplot(data=df, x='bathroomcnt', y='logerror', errorbar = None)
    plt.title('Bathrooms vs. Logerror')
    plt.show()

    print('PEARSONR TEST')
    # Calculate correlation between bedrooms, bathrooms, and logerror
    bathrooms_corr, p = pearsonr(df['bathroomcnt'], df['logerror'])
    
    print(f'We reject the null hypothesis with a correlation of {bathrooms_corr} and a p_value of {p}')



def heating_cooling_vs_logerror(df):
    print('Null hypothesis: Properties with specific heating or cooling systems do not exhibit different logerror patterns')
    print('Alternative hypothesis: Properties with specific heating or cooling systems exhibit different logerror patterns')
    print('BAR PLOT')
    # Bar plot of log error for each heating/cooling system
    plt.figure(figsize=(12, 6))
    plt.bar(data=df, x='heatingorsystemdesc', height='logerror')
    plt.title('Heating/Cooling System vs. Logerror')
    plt.xticks(rotation=45)
    plt.show()

    print('BOX PLOT')
    # Box plot of log error for each heating/cooling system
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='heatingorsystemdesc', y='logerror')
    plt.title('Heating/Cooling System vs. Logerror')
    plt.xticks(rotation=45)
    plt.show()

    # Perform one-way ANOVA test to compare log error across heating/cooling systems
    systems = df['heatingorsystemdesc'].unique()
    anova_results = {}
    for system in systems:
        subset = df[df['heatingorsystemdesc'] == system]['logerror']
        anova_results[system] = subset

    print('F-ONEWAY TEST')
    f_statistic, p = f_oneway(*anova_results.values())

    if p <= 0.05:
        print(f'We reject the null hypothesis with an f_statistic of {f_statistic} and a p_value of {p}')
    else:
        print(f'We do not reject the null hypothesis with an f_statistic of {f_statistic} and a p_value of {p}')




def yearbuilt_vs_logerror(df):

    print('Null hypothesis: The year of construction has no relation to logerror')
    print('Alternative hypothesis: The year of construction relates to logerror')
    print('SCATTER PLOT')
    # Scatter plot of yearbuilt vs. logerror
    sns.scatterplot(data=df, x='yearbuilt', y='logerror')
    plt.title('Year of Construction vs. Logerror')
    plt.show()

    print('PEARSONR TEST')
    # Calculate correlation between yearbuilt and logerror
    correlation, p = pearsonr(df['yearbuilt'], df['logerror'])
    
    print(f'We reject the null hypothesis with a correlation of {correlation} and a p_value of {p}')
