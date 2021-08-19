# DBpedia Spotlight Dashboard
## Table of Contents
- [Objective](#objective)
- [Dashboard chart](#dbpedia-spotlight-dashboard-flowchart)
- [Dashboard content](#dashboard-content)
- [Raw data](#raw-data)
- [Used tools](#used-tools)
- [How to run](#how-to-run)
- [Future work](#future-work)
- [Progress](#progress)

## Objective

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets ([instance-types](https://databus.dbpedia.org/dbpedia/mappings/instance-types/),  [redirects ](https://databus.dbpedia.org/dbpedia/generic/redirects) and [disambiguations](https://databus.dbpedia.org/dbpedia/generic/disambiguations/)) and [Wikipedia's statistics ](https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats/) (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts)** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, it is first necessary to **obtain the raw data**.  Subsequently, it is verified that the DBpedia entities (URLs) that Spotlight uses (URLs of the `uriCounts` file) are found  in one of the three DBpedia datasets (`instance-types`, `redirects` and `disambiguations`).  If they are found in a dataset, they are entities whose type is **known** (from DBpedia), on the contrary,  if they are not found in any dataset, they are entities whose type is **unknown**.  This process is called **entity validation**. 
Once `valid URLs` (of known type), `invalid URLs` (of unknown type)  and the `DBpedia types` that each URL present are known, a series of **statistical measures** are calculated on the data  (percentage of valid URLs over the total (**precision**), percentage of invalid URLs over the total (**impact**), mean, median, standard deviation, quartiles , percentiles, etc).   
Afterwards, **necessary figures** are generated to visualize the statistics.  Once all the figures are ready, they are placed and the final dashboard is obtained.

## DBpedia Spotlight Dashboard Flowchart

![DBpedia Spotlight Dashboard Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png)

## Dashboard Content
The dashboard consists of 4 tabs: 
 - [**Information**](#information-tab)
 - [**Instance-types comparison**](#instance-types-comparison-tab)
 - [**Details**](#details-tab)
 - [**Feedback**](#feedback-tab)

![Tabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/1_tabs.png)

### Information tab
This tab explains:
 - The **purpose** of this dashboard
 - How the **statistics** have been computed
 - The **entity validation** process
 - The **raw files** that DBpedia Spotlight uses during the generation of a language model
 
![Information](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/2_information.png)
 
### Instance-types comparison tab
This tab is used to compare the `instance-types` of the versions *October 2016,* *October 2020*, *May 2021* and *June 2021* for **English** and **Spanish** languages

It is divided into 3 views:
 - **Version comparison**: a table to compare the number of entities and types of the selected versions as well as the diffs
 
 ![Version Comparison](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/3_comparison.png)

 - **Version 1 VS Version 2**: allows to see graphically the number of entities of selected versions
 
![VS](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/4_comparison.png)

 - **DBpedia types comparison**: allows to compare the entities of each selected version according to the DBpedia classes following a [hierarchy structure](http://mappings.dbpedia.org/server/ontology/classes/)
 
![Types comparison](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/5_comparison.png)

### Details tab
It contains 6 sub-tabs:
 - Summary
 - Instance-types
 - uriCounts
 - pairCounts
 - tokenCounts
 - sfAndTotalCounts

![Sub-tabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/6_details.png)
 
 #### Summary
 It is used to view the calculated statistics in table form

![Summary](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/7_details.png)


#### Instance-types
Allows to view the instance-types in more detail for the selected language and version


![Instance-types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/8_details.png)


It is divided in two main sections:

 - **DBpedia Extraction Framework**: to see metrics about the `raw files` of the DBpedia Databus that Spotlight uses to generate the models
 - **DBpedia Spotlight**: to see metrics about the entities and types that are actually used by DBpedia Spotlight after the `entity validation process`
 
 Both sections are formed by the following views:
 - **Measures of Central Tendency**: mean, mode
 - **Measures of Dispersion**: standard deviation
 
 ![Instance-types measures](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/9_details.png)

 - **Entities by DBpedia types** 
 
 ![Instance-types entities and types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/10_details.png)

Moreover, the following views can be seen in the **DBpedia Spotlight** section:
 - **Precision and impact** calculated after entity validation process

![Precision and impact](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/11_details.png)

 - **Position measures for DBpedia types** (quartiles and percentiles)

![Position measures](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/12_details.png)

 - **Top 50 DBpedia types with more entities**
 
 ![Top](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/13_details.png)

#### uriCounts
Allows to see metrics calculated from the **uriCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
![uriCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/14_details.png)

#### pairCounts
Allows to see metrics calculated from the **pairCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
![pairCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/15_details.png)

#### tokenCounts
Allows to see metrics calculated from the **tokenCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
![tokenCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/16_details.png)

#### sfAndTotalCounts
Allows to see metrics calculated from the **sfAndTotalCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 ![sfAndTotalCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/17_details.png)

In addition, it can be seen the surface forms according to their state in the **Wikipedia dump**:
 - **Without associated link** (**-1** in second file column)
 - **Not appearing as text** (**0** in third file column)
 - **Not appearing as text without associated link** (**-1** in second file column and **0** in third file column)
 - **Rest** (surface forms with associated link and appearing as text)

![sfAndTotalCounts pie chart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/18_details.png)

### Feedback tab
Any questions or suggestions for improvement can be made by filling out the following form: https://forms.gle/YKiibhasVuYQ5goe6

![Feedback tab](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/19_feedback.png)

## Raw Data
As mentioned before, the statistical measures have been calculated from the **DBpedia datasets** and the Wikipedia statistical files (**Wikistats**)

### DBpedia Datasets
- **redirets.nt**: contains the redirect links extracted from Wikipedia redirection pages
- **disambiguations.nt**: contains the disambiguation links extracted from Wikipedia disambiguation pages
- **instance_types.nt**: classification of instances with the DBpedia Ontology. Triple containers of the form `<$ resource> rdf: type <$ dbpedia_ontology_class>` generated by the mappings extraction.

![DBpedia Datasets](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/information_dbpedia_datasets.png)

### Wikistats
- **uriCounts**: Contains the number of times each DBpedia resource (URI) appears in the Wikipedia dump
- **pairCounts**: contains the number of times that a text (surface form) is used to link a DBpedia resource
- **sfAndTotalCounts**: Contains the number of times a text (surface form) appears linked to a DBpedia resource (second column) and also the number of times it appears unlinked (third column).
- **tokenCounts**: contains the number of times the words (tokens) appear in each Wikipedia article

![Wikistats](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/information_wikistats.png)

##  Used Tools
 - [GNU datamash](https://www.gnu.org/software/datamash/) for statistics calculation
 - [Dash framework](https://dash.plotly.com/) for building the web app
 - [Plotly Python graphing library](https://plotly.com/python/) for visualizations
 - [Spyder IDE](https://www.spyder-ide.org/) for development and integration

## How to Run
In order to run the dashboard on yout local system, it is only necessary to:
- Clone the repository
- Go to the root folder and execute `main.sh` script

The script will install all the necessary packages and modules

## Future Work
These are some tasks that would be interesting to do in the future:
- Include the rest of the languages available in DBpedia-Spotlight in the `Details` and `Instance-types comparison` tabs.
- Define the statistical information as Linked Data
- Define an onotlogy for the representation of statistical information

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

**[19/07/2021]**:

- DBpedia types comparison between different versions of `instance-types` dataset has been added to the `Comparison` tab.

![Comparison 3](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/comp3.png)

**Pending tasks**:
- **Ontology**: think about statistics of interest to show and think about vocabularies to use or else, create an ontology.
- **Wikistats**: think about what data is interesting to show for the user or another way to show the data.

**[20/07/2021]**: Once the final version of the Dashboard is made (there are still pending tasks), the idea is to update it in the future with suggestions for improvement from the users:
- A [form](https://forms.gle/YKiibhasVuYQ5goe6) has been made to receive feedback from the Dashboard. This form evaluates the **usability principles** contained in the paper: [The Development of Heuristics for Evaluation of Dashboard Visualizations.](Https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6041119/)

![Evaluation](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/evaluation.png)

- A `Feedback` tab has been added to the Dashboard. The direct link to the form appears in this tab, so that users can contribute their ideas for improvement after having examined the Dashboard.

![Evaluation Tab](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/evaluation_tab.png)

**[28/07/2021]**:

- My mentors and I have considered eliminating the bar graphs from the Wikistats because they did not provide relevant information for the user and implied an excess of unnecessary information
- Instead, we have thought of displaying the relevant measurements in the form of cards: 

![Cards1](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/uricounts_cards.png)

![Cards2](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/paircounts_cards.png)

![Cards3](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/tokencounts_cards.png)

![Cards4](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/sfandtotalcounts_cards.png)

- The corresponding statistical measures have also been added for the version of `October 10, 2016`
- All statistical measurements have been reviewed and appear to be correct
- Added to the `Information` tab an explanation of the files from which the Dashboard statistics are obtained:

![DBpedia datasets](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_information_dbpedia_datasets.png)

![Wikistats](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_information_wikistats.png)

- Modified the Dashboard header and added the Spotlight logo as  well as the appearance of the tabs, also added margins to the dashboard:

![Appearance](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/heading.png)

**Tasks in progress**: 
- Add statistics of `2020.10.01` and `2021.06.01` versions for Wikistats files
- Add a `Summary` tab to summarize the statistics in a table

**[29/07/2021]**: A `Summary` tab has been added to show users a summary of the statistics for English and Spanish.

![Summary](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/summary_tab.png)

**[05/08/2021]**:
Meeting with mentors. Finally, the publication of the statistics as linked data is pending as a future task due to lack of time. It only remains to make some visual improvements to the Dashboard. 

**[11/08/2021]**: Some visual changes have been made to the Dashboard:
- Changed the web page title and added the Spotlight icon
- Changed the order of the `Instance-types` tab
    - The cards of each version have been put in different columns:
![2 columns](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/2_columns.png)
    - The 2 bars of the left graph have been put separately:
![2 bars](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/2_bars.png)
- The **Position measures** graphs have been changed since the previous graphs were more confusing:
![Quartiles](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/quartiles.png)
- Also the dashboard is already available to everyone at http://134.155.95.24:8050/

**[15/08/2021]**: Most of the visual changes suggested by the mentors have been implemented:
- The `median` measure has been eliminated from the Summary tab tables
- Dashboard logo has been moved to the left
- `English` and Spanish tabs have been removed and replaced by a `Details` tab so as not to mix topics with languages

![Details](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/details.png)

- Cards have been removed from the `Comparison` tab and in their place a table with highlighted differences has been put

![Comparison table](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/comparison_table.png)

- Added space between buttons
- Horizontal lines have been added to separate views better
- The `Summary` sub-tab has been assigned as default when clicking on the `Details` tab
- The `Details` tab dropdown has been synchronized so that you only have to select version 1 time (in the `Summary` tab preferably)
- A summary of how statistics have been computed has been added to the `Information` tab
- The width of the tables has been modified so that they can be seen well in all possible screens (Not checked yet)