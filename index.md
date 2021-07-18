# Table of contents
- [Objective](#objective)
- [Dashboard chart](#dbpedia-spotlight-dashboard-flowchart)
- [Progress](#progress)

## Objective

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets ([instance-types](https://databus.dbpedia.org/dbpedia/mappings/instance-types/),  [redirects ](https://databus.dbpedia.org/dbpedia/generic/redirects) and [disambiguations](https://databus.dbpedia.org/dbpedia/generic/disambiguations/)) and [Wikipedia's statistics ](https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats/) (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts)** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, it is first necessary to **obtain the raw data**.  Subsequently, it is verified that the DBpedia entities (URLs) that Spotlight uses (URLs of the `uriCounts` file) are found  in one of the three DBpedia datasets (`instance-types`, `redirects` and `disambiguations`).  If they are found in a dataset, they are entities whose type is **known** (from DBpedia), on the contrary,  if they are not found in any dataset, they are entities whose type is **unknown**.  This process is called **entity validation**. 
Once `valid URLs` (of known type), `invalid URLs` (of unknown type)  and the `DBpedia types` that each URL present are known, a series of **statistical measures** are calculated on the data  (percentage of valid URLs over the total (**precision**), percentage of invalid URLs over the total (**impact**), mean, median, standard deviation, quartiles , percentiles, etc).   
Afterwards, **necessary figures** are generated to visualize the statistics.  Once all the figures are ready, they are placed and the final dashboard is obtained.

## DBpedia Spotlight Dashboard Flowchart

![DBpedia Spotlight Dashboard Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png)

## Progress
**[17/05/2021]**: Proposal acceptance and community bonding period started.

**[27/05/2021]**: Meeting the mentors on Google Meet to introduce ourselves and talk about the project and interesting ideas:
 - Load data from **Wikistats** (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts) and **DBpedia artifacts** (instance-types, redirects and disambiguations) in dataframes using [Pandas](https://pandas.pydata.org/) and [RDFLib](https://rdflib.readthedocs.io/en/stable/) libraries.
 - Create the desired visualizations using [Matplotlib](https://matplotlib.org/) library.
 - Use frameworks like [Dash](https://dash.plotly.com/) for building the dashboard. 
 - Compute the desired statistics over the dataframe using [NumPy](https://numpy.org/) library. 
 - Publish the statistical data generated using [Linked Open Vocabularies](https://lov.linkeddata.es/dataset/lov/) once the dashboard is built.

 **[10/06/2021]**: Second meeting with the mentors, first advances in the project and new ideas:
 - Get model raw data for Spanish and English -> Done
 - Visualize DBpedia types for Spanish and English -> Done (**problem**: some hierarchy types are missing in the instance_types file) 
 - Validation of DBpedia links (entities) -> In progress (**problem**: IP address blocked for 1 day due to excessive requests) (**new idea**: get ALL DBpedia distinct resources doing SPARQL queries and store results in local file, then look for valid URLs comparing that **generated file URLs** and **instance_types URLs** using UNIX commands)
![Blocked IP](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dbpedia_ban.png)

**[14/06/2021]**: Some progress:
 - Validation of DBpedia links (entities) -> In progress (solving problem). I found out that all entities (both valid and invalid entities) are found on SPARQL endpoints, so the idea I came up with doesn't work in this case. Regarding the first idea, even putting timeout between each request my IP address is still blocked (already 3 times in total)
 - Review of the code generated so far -> Done
 - Dashboard draft using [Dash](https://dash.plotly.com/) -> Done
 ![Dashboard draft](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_draft.png)

**[24/06/2021]**: The problem of URLs validation has been resolved:
 - URLs of the latest version of uriCounts file have been validated for Spanish language. For this, each URL of the file has been checked by means of the following SPARQL query (using a local SPARQL Endpoint to avoid DBpedia IP blocking):
 
![SPARQL validation](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/validate_query.png)

If the value returned by the query is 0, it means that this URL does not have any type, that is, it is a URL that does not exist and therefore is invalid.
- Once valid and invalid URLs for Spanish were obtained, types of valid URLs have been obtained and can be viewed according to the DBpedia hierarchy:

 ![Spanish valid types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_valid_types.png)

- Precision and impact of Spanish URLs has also been calculated.
 ![Spanish statistics](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_urls_impact.png)

- URLs validation of the latest version of uriCounts file for English language -> In progress (executing)
- Types of valid English URLs -> In progress (executing)
- Precision and impact of English URLs -> In progress (executing)

**[25/06/2021]**: DBpedia entities used by Spotlight have been validated for both Spanish and English languages. Now is time to think of other interesting statistical measures to show on the dashboard: 
- URLs validation of the latest version of uriCounts file for English language -> Done
- Types of valid English URLs -> Done

![English valid types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/en_valid_types.png)

- Precision and impact of English URLs -> Done

![English statistics](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/en_urls_impact.png)

- Think about other interesting statistical measures to show on the dashboard -> In progress

**[01/07/2021]**: Some statistical measures have been calculated from DBpedia datasets (redirects, disambiguations and instance-types) and Wikistats (uriCounts, pairCounts, tokenCounts, sfAndTotalCounts) for English and Spanish:
- **Redirects and disambiguations**:

![Redirects and disambiguations](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/redirects_disambiguations_statistics1.png)

- **Instance-types**:

![Instance-types 1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/instance_types_statistics1.png)
![Instance-types 2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/instance_types_statistics2.png)
![Instance-types 3](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/instance_types_statistics3.png)

- **uriCounts**:

![uriCounts1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/uriCounts_statistics1.png)
![uriCounts2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/uriCounts_statistics1.png)

- **pairCounts**:

![pairCounts1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/pairCounts_statistics1.png)
![pairCounts2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/pairCounts_statistics2.png)

- **tokenCounts**:

![tokenCounts1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/tokenCounts_statistics1.png)

- sfAndTotalCounts:

![sfAndTotalCounts1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/sfAndTotalCounts_statistics1.png)
![sfAndTotalCounts2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/sfAndTotalCounts_statistics2.png)
![sfAndTotalCounts3](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/sfAndTotalCounts_statistics3.png)

Next tasks:
    
       1. Review all the statistics generated (especially those of the instance-types file) -> In progress
       2. Think about other statistics that may be interesting to have on the dashboard
       3. Think about how these statistics will be displayed on the dashboard

**[02/07/2021]**: Statistics have been revised and now they seem to be all good. Next thing to do is think about how to display them in the Dashboard.

**[06/07/2021]**: I have thought about how to display the statistics on the dashboard.

These are the statistics that are currently displayed:
- Firstly, the **information of the Dbpedia Extraction Framework** is displayed:
 1. Number of non-repeating entities (instance_types.nt)
 1. Non-repeating types (instance_types.tsv)
 1. Bar chart of instance-types.nt (instance_types.tsv)

- Then, the **Spotlight information** is displayed:
 1. Number of non-repeating entities with known types from Dbpedia (valid_urls)
 1. Number of non-repeating types (valid_types.tsv)
 1. Bar chart with known types (valid_types.tsv)
 1. Statistics on known types: median, mean, percentiles, quartiles, etc (valid_types.tsv)

This is how the dashboard is at the moment, waiting for feedback from the mentors to change what is necessary:

![dashboard_stats1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats1.png)

![dashboard_stats2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats2.png)

![dashboard_stats3](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats3.png)

![dashboard_stats4](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats4.png)

![dashboard_stats5](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats5.png)

![dashboard_stats6](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats6.png)

![dashboard_stats7](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats7.png)

![dashboard_stats8](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats8.png)

![dashboard_stats9](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats9.png)

![dashboard_stats10](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats10.png)

**[08/07/2021]**: Meeting with the mentors and new ideas for the Dashboard:
- Add a flowchart at the beginning where it can be seen how DBpedia Spotlight works
- Change some of the graphs so that the dispersion of the data can be better appreciated 

**[11/07/2021]**: DBpedia Spotlight and Spotlight Dashboard flow charts have been made. Some Dashboard charts have also been changed, now the data looks better. Waiting for feedback from mentors:
- An additional tab has been added to the Dashboard called `Information` where the process of creating Spotlight models and the purpose and operation of the Spotlight Dashboard are explained, as well as flow charts to see both processes graphically.

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/information_tab.png)

- Some of the Dashboard graphics have been changed to better appreciate the dispersion of the data. In the case of Wikistats, since they are millions of data, `Slicers` have been added so that the user can select different samples of the data. The information reflected in these graphs together with the tables (`top 50`) allow you to get an idea of what the data used by Spotlight is like.

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new2.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new3.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new4.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new5.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new6.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new7.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new8.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new9.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new10.png)

![information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/es_dashboard_stats_new11.png)

**[15/07/2021]**: Meeting with the mentors in which the Dashboard has been reviewed and the following tasks to be carried out have been defined:
- Make the `Comparison` tab, where the number of entities and the types found in the DBpedia `instance-types` dataset will be compared for both Spanish and English for the following versions:
```
2016.10.01
2020.10.01
2021.05.01
2021.06.01
```
- Think about the ontology to use to represent the calculated statistics as Linked Data. Also think if it is worth creating our own ontology to represent the information instead of using any of the existing ones or reusing terms from different ontologies.

**[18/07/2021]**:

- `Instance types`,` uriCounts`, `pairCounts`,` tokenCounts` and `sfAndTotalCounts` sub-tabs have been added within the `Spanish` and `English` tabs to be able to view the information of interest in parts.

![Subtabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/subtabs.png)

- The `Comparison` tab has been made, where the different versions can be compared and the variation of entities and types between them can be appreciated.

![Comparison 1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/comp1.png)

![Comparison 2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/comp2.png)