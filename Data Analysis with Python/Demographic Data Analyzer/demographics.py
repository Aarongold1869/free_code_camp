import pandas as pd
import unittest


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv(r'pandas\adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df.race.unique()
    race_dict = {}
    for r in races:
        race_dict[r] = len(df[df['race'] == r])

    race_count = pd.Series(race_dict)

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male'].loc[:,"age"].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df['education'] == 'Bachelors']) / len(df)) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    lower_education = df.loc[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]

    # percentage with salary >50K
    higher_education_rich = round((len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1)
    lower_education_rich = round((len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == 1]

    rich_percentage = (len(num_min_workers[num_min_workers['salary'] == '>50K']) / len(num_min_workers)) * 100 

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].unique()
    country_dict = {}
    for c in countries:
        country_dict[c] = round((len(df.loc[(df['native-country'] == c) & (df['salary'] == '>50K')])  / len(df[df['native-country'] == c])) * 100 ,1)

    country_salary = pd.Series(country_dict)

    highest_earning_country = country_salary.idxmax()
    highest_earning_country_percentage = country_salary[country_salary.idxmax()]

    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    india_rich_occupations = india_rich.occupation.unique()
    occ_pop = {}
    for o in india_rich_occupations:
        occ_pop[o] = len(india_rich[india_rich['occupation'] == o])

    popular_occupations_series = pd.Series(occ_pop)
    top_IN_occupation = popular_occupations_series.idxmax()

    # # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


# if __name__ == "__main__":
#     calculate_demographic_data()


class DemographicAnalyzerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.data = calculate_demographic_data(print_data = False)

    def test_race_count(self):
        actual = self.data['race_count'].tolist()
        expected = [27816, 3124, 1039, 311, 271]
        self.assertCountEqual(actual, expected, msg="Expected race count values to be [27816, 3124, 1039, 311, 271]")

    def test_average_age_men(self):
        actual = self.data['average_age_men']
        expected = 39.4
        self.assertAlmostEqual(actual, expected, msg="Expected different value for average age of men.")

    def test_percentage_bachelors(self):
        actual = self.data['percentage_bachelors']
        expected = 16.4 
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with Bachelors degrees.")

    def test_higher_education_rich(self):
        actual = self.data['higher_education_rich']
        expected = 46.5
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage with higher education that earn >50K.")
  
    def test_lower_education_rich(self):
        actual = self.data['lower_education_rich']
        expected = 17.4
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage without higher education that earn >50K.")

    def test_min_work_hours(self):
        actual = self.data['min_work_hours']
        expected = 1
        self.assertAlmostEqual(actual, expected, msg="Expected different value for minimum work hours.")     

    def test_rich_percentage(self):
        actual = self.data['rich_percentage']
        expected = 10
        self.assertAlmostEqual(actual, expected, msg="Expected different value for percentage of rich among those who work fewest hours.")   

    def test_highest_earning_country(self):
        actual = self.data['highest_earning_country']
        expected = 'Iran'
        self.assertEqual(actual, expected, "Expected different value for highest earning country.")   

    def test_highest_earning_country_percentage(self):
        actual = self.data['highest_earning_country_percentage']
        expected = 41.9
        self.assertAlmostEqual(actual, expected, msg="Expected different value for highest earning country percentage.")   

    def test_top_IN_occupation(self):
        actual = self.data['top_IN_occupation']
        expected = 'Prof-specialty'
        self.assertEqual(actual, expected, "Expected different value for top occupations in India.")      

if __name__ == "__main__":
    unittest.main()