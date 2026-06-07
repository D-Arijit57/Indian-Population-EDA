import pandas as pd 
import requests
import matplotlib.pyplot as plt

url = "https://api.worldbank.org/v2/country/ind/indicator/SP.POP.TOTL?format=json"

response = requests.get(url)
# Check if we got the data (should be a 200 OK)
print(response.status_code)

data = response.json()
print(type(data))
print(len(data))
# data[0] -> metadata 
# data[1] -> actual data



# understanding the format of the data 
print("First entry : ",data[1][0], end="\n")
print("First entry of meta data : ", data[0])

records = data[1]
df = pd.DataFrame(records)
# Check the columns which are avaibable
print(df.head())

# Manually creating rows for the data frame 
rows = []

for record in records : 
    rows.append({
            "country" : record["country"]["value"]  ,
            "year" : record["date"],
            "population" : record["value"]
    })

pop_data = pd.DataFrame(rows)
print("Population Data : \n", pop_data.head())


def data_preprocessing(pop_data) :
    # Information about the data 
    print("Information:")
    pop_data.info()
    
    # Statistical Summary of the data : 
    print("Statistical Summary : \n", pop_data.describe())
    
    #Finding out the missing values : 
    print("Total missing values : \n",pop_data.isnull().sum())
    
    # Changing it visually ( not using the scientific notation)
    pd.set_option('display.float_format', '{:,.0f}'.format)

    # Converting the year to numeric : 
    pop_data['year'] = pd.to_numeric(pop_data['year'])
    # Dropping the missing values
    pop_data = pop_data.dropna()
    
    # Average yearly change in the population 
    pop_data = pop_data.sort_values('year')
    pop_data['population_change'] = pop_data['population'].diff()
    print("Comparison : \n ")
    print(pop_data[['year', 'population', 'population_change']])

    print("Average yearly change in population: ", pop_data['population_change'].mean())
    
    # Growth rate increasing or decreasing 
    population_1980 = pop_data.loc[

        pop_data['year'] == 1980,

        'population'

        ].iloc[0]

    print("Population in 1980:", population_1980)

    population_2023 = pop_data.loc[
        pop_data['year'] == 2023,
        'population'
    ].iloc[0]
    
    print("Population in 2023 : ", population_2023)
    growth =((population_2023 - population_1980) / population_1980 ) * 100
    print(f"Population Growth 1980 - 2023 : " f"{growth:.2f}%")
    
    
    # Year with the highest increase : 
    max_growth = pop_data.loc[
        pop_data['population_change'].idxmax()]
    print(" Year with the highest increase : \n", max_growth)
    
    # Which decade grew the fastest : 
    # create a decade column 
    pop_data['decade'] = (
        pop_data['year'] // 10
        ) * 10
    # find out the growth decade wise : 
    decade_growth = (
        pop_data.groupby('decade')['population_change'].sum()
    )
    print("Decade wise growth : \n", decade_growth)
    
    # Decade with the fastest growth :
    print("Fastest growing decade : ",decade_growth.idxmax())
    
    # How many years to add 100 million people
    # Assumption : Considering the growth rate is constant 
    avg_growth_rate_per_year = pop_data['population_change'].mean()
    print("Growth Rate Per Year : ", avg_growth_rate_per_year)
    
    print(f"To add 100 million people we would need :  {100000000/avg_growth_rate_per_year:.2f} years")
    
    # How many years did it take India to add the next 100 million people at different points in history    
    # Create milestones :  when did India crossed a certain number of population 
    milestones = [
    700_000_000,
    800_000_000,
    900_000_000,
    1_000_000_000,
    1_100_000_000,
    1_200_000_000,
    1_300_000_000,
    1_400_000_000
]
    # find out the years crossing the milestones
    milestone_years = {}
    for  milestone in milestones : 
        year = pop_data.loc[
            pop_data['population'] >= milestone,
            'year'
        ].iloc[0]
        milestone_years[milestone] = year
        
    for milestone, year in milestone_years.items():

        print(

        f"India crossed "

        f"{milestone/1_000_000:.0f} million "

        f"people in {year}"

        )
    print(f"Years to have a change of 100 million :{5} to {6} years")
    
    return pop_data, decade_growth
    
def visualization(pop_data, decade_growth):

    growth_data = pop_data[
        (pop_data['year'] >= 1980)
        &
        (pop_data['year'] <= 2020)
    ]

    # Growth Trend
    plt.figure(figsize=(12, 6))

    plt.plot(
        growth_data['year'],
        growth_data['population_change'],
        marker='o'
    )

    plt.title(
        'India Population Growth Trend (1980-2020)'
    )

    plt.xlabel('Year')
    plt.ylabel('Population Change')

    plt.grid(True)

    plt.tight_layout()

    plt.show()


    # Decade Growth
    plt.figure(figsize=(8, 5))

    decade_growth.plot(
        kind='bar'
    )

    plt.title(
        'Population Growth by Decade'
    )

    plt.xlabel('Decade')
    plt.ylabel('Total Population Growth')

    plt.tight_layout()

    plt.show()
    

processed_data, decade_growth = data_preprocessing(pop_data)

visualization(
    processed_data,
    decade_growth
)