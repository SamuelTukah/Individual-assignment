"""Question 4: Functional programming on world population data."""

import csv
import requests
from functools import reduce
from operator import add
from io import StringIO

DATA_URL = "https://raw.githubusercontent.com/datasets/population/master/data/population.csv"

def fetch_csv(url):
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    return r.text

def read_population_csv(text):
    reader = csv.DictReader(StringIO(text))
    rows = list(reader)
    return rows

def filter_year(rows, year="2020"):
    return list(filter(lambda r: r['Year'] == year, rows))

def map_to_country_population(rows):
    # returns tuples (Country Name, Population as int)
    def conv(r):
        name = r['Country Name']
        pop = int(float(r['Value']))  # some CSVs have float formatted numbers
        return (name, pop)
    return list(map(conv, rows))

def top_n_by_population(country_pop_list, n=5):
    return sorted(country_pop_list, key=lambda x: x[1], reverse=True)[:n]

def total_population(country_pop_list):
    return reduce(lambda a,b: a + b, (p for _, p in country_pop_list), 0)

def average_population_of_continent(rows, continent_countries_set):
    # rows are (country, pop) for 2020
    africa = list(filter(lambda cp: cp[0] in continent_countries_set, rows))
    if not africa:
        return 0
    total = reduce(lambda a,b: a + b, (p for _, p in africa), 0)
    return total / len(africa)

def apply_and_log(func, iterable):
    """Higher-order function: applies func to iterable, prints a log and returns result."""
    print(f"[LOG] Applying {func.__name__} to iterable of length {len(iterable)}")
    return func(iterable)

if __name__ == "__main__":
    print("Fetching CSV...")
    text = fetch_csv(DATA_URL)
    print("Parsing CSV...")
    rows = read_population_csv(text)

    # Show immutability: store original length and sample entry
    print("Original number of rows:", len(rows))
    sample_before = rows[0]
    print("Sample row before transform:", sample_before)

    # Filter for 2020
    rows_2020 = filter_year(rows, "2020")
    country_pop = map_to_country_population(rows_2020)

    print("\nTop 5 most populated countries (2020):")
    top5 = top_n_by_population(country_pop, 5)
    for name, pop in top5:
        print(f"{name}: {pop:,}")

    total_world_pop = total_population(country_pop)
    print(f"\nTotal world population (sum of country entries in dataset for 2020): {total_world_pop:,}")

    # For average of African countries: we need a list of African country names.
    # For demonstration: a small sample set of African countries (you may expand).
    african_sample = {
        "Nigeria", "Ethiopia", "Egypt", "DR Congo", "Tanzania",
        "South Africa", "Kenya", "Uganda", "Algeria", "Sudan"
    }
    avg_africa = average_population_of_continent(country_pop, african_sample)
    print(f"\nAverage population (sample African countries): {avg_africa:,.0f}")

    # Immutability demonstration: original sample unchanged
    print("\nSample row after transform (should be unchanged):", sample_before)

    # Higher-order function usage
    apply_and_log(lambda lst: lst[:3], country_pop)

    # Composed functional pipeline: filter -> map -> sort -> take top
    def composed_top_n(rows, year="2020", n=5):
        # pipeline implemented with functions
        filtered = list(filter(lambda r: r[1] > 50_000_000, country_pop))
        return sorted(filtered, key=lambda x: x[1], reverse=True)[:n]

    pipeline_top5 = composed_top_n(country_pop, n=5)
    print("\nPipeline top5 (>50M):")
    for name, pop in pipeline_top5:
        print(name, pop)
