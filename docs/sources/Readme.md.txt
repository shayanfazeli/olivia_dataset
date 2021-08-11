# OLIVIA Dataset

## Introduction
This repository includes data sources used in OLIVIA project for region representations.
Olivia dataset is a collection of numerous data sources providing information regarding different regional attribtues,
studying which can be of significant help to pandemic understanding and response analyses.

## Installation
This package can be installed via pip:
```bash
pip3 install --upgrade olivia_dataset;
```

or via the source:
```bash
pip3 install -e .;
```

## Getting Started
The first step is to configure the package, please run the following command and insert the required information:

```bash
olivia_dataset_config
```

Afterwards, whenever you want to refresh the live repository, it is  sufficient to run the following command:

```bash
olivia_dataset_refresh
```

## Live Repository
The most recent version of the data files are available in the [live dataset gdrive repository](https://drive.google.com/drive/folders/1CfhgbPaWAvy_1FN8UqpMI6lGdL-6bJep?usp=sharing).

## Documentation
The package documentation is available at [this link](https://shayanfazeli.github.io/olivia_dataset/).

## Citation

Please use the following citation:
```
[To be published in IEEE ICHI 2021]
```

## Data Sources

* Laboratory confirmed COVID-19 Associated Hospitalizations [[link](https://gis.cdc.gov/grasp/covidnet/COVID19_5.html)]
* A Weekly Influenza Surveillance Report Prepared by the Influenza Division [[link](https://gis.cdc.gov/grasp/covidnet/COVID19_1.html)]
    * CAUTION: there are slight issues (e.g., a "434" value for New York has been recorded as "4334" in the data), that we need to be aware of.
* COVID-19 Cases, Deaths, and Recoveries across the United States [[link](https://coronavirus.1point3acres.com/)]
* US Census Data [[link](https://www.kaggle.com/muonneutrino/us-census-demographic-data)]
    * We have been utilizing this variant (and the file for Census 2017) shared by the Kaggle community, however,
      if one is interested, more recent data might be available in the [official repository](https://data.census.gov/).

* US Mortality Rates by County 1980-2014
    * The data sources: [[link](http://ghdx.healthdata.org/record/ihme-data/united-states-mortality-rates-county-1980-2014)], [[link](https://www.kaggle.com/IHME/us-countylevel-mortality/)]
    * The way we use this dataset is deriving *static* county features using these age-standardized values.

* Diversity Index of US counties [[link](https://www.kaggle.com/mikejohnsonjr/us-counties-diversity-index)]
    * Using the census data, we should be able to compute a more recent and more accurate values for county diversity indices, and
      end up not using this data.

* US Drought Monitor [[link](https://droughtmonitor.unl.edu/)], [[link](https://www.kaggle.com/us-drought-monitor/united-states-droughts-by-county)]

* US ICU beds (evaluated by Kaiser Health News) [[link](https://www.kaggle.com/jaimeblasco/icu-beds-by-county-in-the-us)]

* Election results [[link](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/VOQCHQ)]
    * To extract county-based features, we focused on 2016 which was the most recent US Presidential Election at the time,
      more information is currently available in Harvard Dataverse.

* US Household Income Statistics [[link](https://www.kaggle.com/goldenoakresearch/us-household-income-stats-geo-locations)]

* Food Business Features - From National Restaurants Association - State level [[link](https://restaurant.org/research/state)]

* Life expectancy, obesity, and physical activity [[link](http://www.healthdata.org/us-health/data-download)]

* Alcohol [[link](http://www.healthdata.org/us-health/data-download)]

* Diabetes [[link](http://www.healthdata.org/us-health/data-download)]

## Additional Data Repositories Available Online
* COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University [[link](https://github.com/CSSEGISandData/COVID-19)]]
    * Links to the official state/county dashboards can be found there.
    
* County-level Socioeconomic Data for Predictive Modeling of Epidemiological Effects - [[link](https://github.com/JieYingWu/COVID-19_US_County-level_Summaries)]
    * This is very similar to our effort in gathering regional features and attributes
    * This dataset collection is different from ours. While sharing some key features such as covid-19 outcomes, these two datasets mainly complement each other. 
        * There are information on some additional features such as crime and education in this repository.
    
* KFF Data Repository
    * This data includes vaccincation related information, as well as policy-related information - [[link](https://github.com/KFFData/COVID-19-Data)]