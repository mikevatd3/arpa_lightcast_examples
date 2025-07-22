# Using the Lightcast API

## Services that we can access

### Core LMI (labor market information)

Their Docs: https://docs.lightcast.dev/apis/core-lmi

The Core LMI service combines several datasets about jobs, skills, occupations, and industries. It provides estimates for how many jobs are available in a given location, occupation, and year. It provides salary estimates (historical medians, and averages, and current distribution information). It also provides skills associated with the occupation.

The Core LMI also offers data on industries in a given area, and which occupations are hired to work within those industries.


### Career Pathways

The Career Pathways API offers a 'first-person' view of career advancement. You can query by choosing a starting occupation and explore which next steps are available to someone in that occupation, what skills are required for advancement and what salary gains could be expected by switching.


### Occupation Benchmark

The Occupation Benchmark API offers much more detail about occupations than what is available from the Core LMI API. You can find which education level is typically required, Lightcast estimates for risk of automation, salary information and which skills might boost the salary.


### D3 Additions

#### Gathering all active SOC codes available on the API.

There wasn't a convenient way to get Standard Occupational Classification (SOC) codes used throughout the API from the API. Lightcast uses a subset of SOC codes, combining some occupations under a single, Lightcast-specific code.

All of those codes and their descriptions can be found in the `detroit_tech_employment.occupation` table in the ARPA database.


### Standard codes referenced by Lightcast APIs

- [Standard Occupation Codes (SOC)](https://www.bls.gov/soc/)
- [O\*Net](https://www.dol.gov/agencies/eta/onet)
- [North American Industry Classification System (NAICS)](https://www.census.gov/naics/)
- [Lightcast Occupation Taxonomy](https://lightcast.io/lot/occupations/categories)


### Geographic availability

Not all Lightcast data is available at every geography -- some data is available only nation-wide, some doesn't go more granular than MSA. This is shown for Core LMI anyway in the 'Area' dimension in the 'levelsStored' field of the metadata. 

```
...
    {
        "name": "Area",
        "levelsStored": [
            "1", # Nation
            "2", # State
            "3", # MSA
            "4", # County
            ---------------------- Only available on a few datasets
            "5", # Zip code
            "6", # Census Tract
        ]
    }
...
```
