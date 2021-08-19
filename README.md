# DBpedia-Spotlight-Dashboard - GSoC 2021
An integrated statistical information tool from the Wikipedia dumps and the DBpedia Extraction Framework artifacts

Dashboard URL: http://134.155.95.24:8050/

## Table of Contents
- [Objective](#objective)
- [Raw data](#raw-data)
- [Dashboard chart](#dbpedia-spotlight-dashboard-flowchart)
- [Dashboard content](#dashboard-content)
- [Evaluation](#evaluation)
- [Used tools](#used-tools)
- [How to run](#how-to-run)
- [Conclusions](#conclusions)
- [Future work](#future-work)

### Objective

The purpose of this dashboard is to **facilitate the understanding and analysis of both DBpedia datasets ([instance-types](https://databus.dbpedia.org/dbpedia/mappings/instance-types/),  [redirects ](https://databus.dbpedia.org/dbpedia/generic/redirects) and [disambiguations](https://databus.dbpedia.org/dbpedia/generic/disambiguations/)) and [Wikipedia's statistics ](https://databus.dbpedia.org/dbpedia/spotlight/spotlight-wikistats/) (uriCounts, pairCounts, sfAndTotalCounts and tokenCounts)** by calculating statistical measures on these data that allow understanding the trends of **DBpedia resources**, **Wikipedia links** and **surface forms**.
 
 To make the dashboard, these steps have been followed:

 1. **Obtain raw data** from the DBpedia Databus
 2. **Entity validation process**: throughout the project, it was seen that there are Spotlight entities whose type is **unknown**. This process consists of determining the DBpedia entities with `known types` and those with `unknown types`.
DBpedia entities with **known types** will be found in one of the following datasets: `instance-types`, `redirects`, and `disambiguations`. 
Whereas entities with **unknown types** will not be found in any of them. 
 3. **Computation of statistical measures**: percentage of entities with known types over the total (precision), percentage of entities with unknown types over the total (impact), mean, median, standard deviation, quartiles, percentiles...
 4. **Plot dashboard figures**

### Raw Data
As mentioned before, the statistical measures have been calculated from the **DBpedia datasets** and the Wikipedia statistical files (**Wikistats**)

#### DBpedia Datasets
- **redirects.nt**: contains the redirect links extracted from Wikipedia redirection pages
- **disambiguations.nt**: contains the disambiguation links extracted from Wikipedia disambiguation pages
- **instance_types.nt**: classification of instances with the DBpedia Ontology. Triple containers of the form `<$ resource> rdf: type <$ dbpedia_ontology_class>` generated by the mappings extraction.

| DBpedia Dataset    | Sample                                                                                                                                       |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| redirects.nt       | `<http://es.dbpedia.org/resource/Artesanal> <http://dbpedia.org/ontology/wikiPageRedirects> <http://es.dbpedia.org/resource/Artesanía> .`      |
| disambiguations.nt | `<http://es.dbpedia.org/resource/Abate> <http://dbpedia.org/ontology/wikiPageDisambiguates> <http://es.dbpedia.org/resource/Carlo_Abate> .`    |
| instance_types.nt  | `<http://es.dbpedia.org/resource/Cristiano_Ronaldo> <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <http://dbpedia.org/ontology/Athlete> .` |

#### Wikistats
- **uriCounts**: Contains the number of times each DBpedia resource (URI) appears in the Wikipedia dump
- **pairCounts**: contains the number of times that a text (surface form) is used to link a DBpedia resource
- **sfAndTotalCounts**: Contains the number of times a text (surface form) appears linked to a DBpedia resource (second column) and also the number of times it appears unlinked (third column).
- **tokenCounts**: contains the number of times the words (tokens) appear in each Wikipedia article

|File |Sample  |
|---|---|
|uriCounts |`http://es.dbpedia.org/resource/Ciudadanía_rusa 69`|
|pairCounts  |`ciudadanos rusos http://es.dbpedia.org/resource/Ciudadanía_rusa	5`|
|sfAndTotalCounts  |`ciudadanos rusos	5	133`  |
|tokenCounts  |`http://es.wikipedia.org/wiki/14_Wall_Street	{(street,13),(wall,11),(edifici,10),(del,5),(adyacent,5),(broadway,4)...}`|

### DBpedia Spotlight Dashboard Flowchart

![DBpedia Spotlight Dashboard Flowchart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/dashboard_flowchart.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 1. DBpedia Spotlight Dashboard Flowchart*

### Dashboard Content
The dashboard consists of 4 tabs: 
 - [**Information**](#information-tab)
 - [**Instance-types comparison**](#instance-types-comparison-tab)
 - [**Details**](#details-tab)
 - [**Feedback**](#feedback-tab)

**Figure 2** shows the 4 main tabs of the dashboard

![Tabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/1_tabs.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 2. Dashboard tabs*

#### Information tab
This tab explains:
 - The **purpose** of this dashboard
 - How the **statistics** have been computed
 - The **entity validation** process
 - The **raw files** that DBpedia Spotlight uses during the generation of a language model
 
#### Instance-types comparison tab
This tab is used to compare the `instance-types` of the versions *October 2016,* *October 2020*, *May 2021* and *June 2021* for **English** and **Spanish** languages

It is divided into 3 views:
 - **Version comparison**: a table to compare the number of entities and types of the selected versions as well as their differences
 
 **Figure 3** shows a table with entities and types of **October 2016** and **May 2021** versions for the **English** language.
 
 ![Version Comparison](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/3_comparison.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 3. Version comparison*

 - **Version 1 VS Version 2**:  a chart illustrates the number of entities from the selected versions
 
 **Figure 4** shows a chart with the number of entities of **October 2016** and **May 2021** versions for the **English** language.
 
![VS](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/4_comparison.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 4. Version 1 VS Version 2*

 - **DBpedia types comparison**: the entities from each selected version are graphically compared based on the [DBpedia hierarchy of classes](http://mappings.dbpedia.org/server/ontology/classes/)
 
Figure 5** shows a chart with the number of entities by DBpedia types of **October 2016** and **May 2021** versions for the **English** language. 
 
![Types comparison](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/5_comparison.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 5. DBpedia types comparison*

#### Details tab
It contains 6 sub-tabs:
 - Summary
 - Instance-types
 - uriCounts
 - pairCounts
 - tokenCounts
 - sfAndTotalCounts

**Figure 6** shows the 6 sub-tabs of the Details tab

![Sub-tabs](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/6_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 6. Sub-tabs of Details tab*
 
 ##### Summary
 It shows the calculated statistics.
 
 In **Figure 7** can be seen **measures of central tendency** (mean and mode) that are used to know where the data is inclined or clustered the most. In this case, we can see how the DBpedia entities, surface forms and Wikipedia tokens are grouped.
 Also it can be seen the standard deviation, which is the main **measure of dispersion**, that is used to observe the degree of variability of DBpedia entities, surface forms and Wikipedia tokens.

![Summary](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/7_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 7. Table with statistical measures of **Jun 2021** version for **English** language*

##### Instance-types
Allows to view the instance-types in more detail for the selected language and version

**Figure 8** shows part of the content of the instance-types sub-tab of **May 2021** version for the **English** language .

![Instance-types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/8_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 8. Instance-types details*

It is divided in two main sections:

 - **DBpedia Extraction Framework**: to see metrics about the `raw files` of the DBpedia Databus that Spotlight uses to generate the models
 - **DBpedia Spotlight**: to see metrics about the entities and types that are actually used by DBpedia Spotlight after the `entity validation process`
 
 Both sections are formed by the following views:
 - **Measures of Central Tendency**: mean, mode
 - **Measures of Dispersion**: standard deviation

 - **Entities by DBpedia types** 
 
**Figure 9** shows the entities by DBpedia types chart of **May 2021** version for the **English** language .

![Instance-types entities and types](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/10_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 9. Entities by DBpedia types chart*

Moreover, the following views can be seen in the **DBpedia Spotlight** section:
 - **Precision and impact** calculated after `entity validation process`

These measurements are used to find out which Spotlight entities have **known DBpedia types** and which entities have **unknown types**. They are calculated as follows: 

    Precision = Nº entities with known types / Nº entities
    Impact = Nº entities with unknown types / Nº entities

In the **Figure 10** it can be seen that 63% of entities present known types and 27% present unknown types in the case of **English** language in **May 2021** version 

![Precision and impact](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/11_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 10. Precision and Impact indicators*

- **Position measures for DBpedia types** (quartiles and percentiles)

**Figure 11** shows the position measures for DBpedia types chart of **May 2021** version for the **English** language .

![Position measures](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/12_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 11. Position measures for DBpedia types*

 - **Top 50 DBpedia types with more entities**
 
**Figure 12** shows the top 50 DBpedia types with more entities table of **May 2021** version for the **English** language .

![Top](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/13_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 12. Top 50 DBpedia types with more entities*

##### uriCounts
Allows to see metrics calculated from the **uriCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 **Figure 13** shows the calculated measures of **central tendency** and **dispersion** from uriCounts file of **May 2021** version for the **English** language .
 
 ![uriCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/14_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 13. Calculated measures from uriCounts file*


##### pairCounts
Allows to see metrics calculated from the **pairCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 **Figure 14** shows the calculated measures of **central tendency** and **dispersion** from pairCounts file of **May 2021** version for the **English** language .
 
 ![pairCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/15_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 14. Calculated measures from pairCounts file*

##### tokenCounts
Allows to see metrics calculated from the **tokenCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation
 
 **Figure 15** shows the calculated measures of **central tendency** and **dispersion** from tokenCounts file of **May 2021** version for the **English** language .
 
 ![tokenCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/16_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 15. Calculated measures from tokenCounts file*

##### sfAndTotalCounts
Allows to see metrics calculated from the **sfAndTotalCounts file**

The main measures are:
 - **Measures of Central Tendency**: mean, mode, median
 - **Measures of Dispersion**: standard deviation

**Figure 16** shows the calculated measures of **central tendency** and **dispersion** from sfAndTotalCounts file of **May 2021** version for the **English** language .
 
![sfAndTotalCounts](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/17_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 16. Calculated measures from sfAndTotalCounts file*

In addition, in **Figure 17** can be seen the surface forms according to their state in the **Wikipedia dump**:
 - **Without associated link** (**-1** in second file column)
 - **Not appearing as text** (**0** in third file column)
 - **Not appearing as text without associated link** (**-1** in second file column and **0** in third file column)
 - **Rest** (surface forms with associated link and appearing as text)

![sfAndTotalCounts pie chart](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/18_details.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 17. Surface forms state*

#### Feedback tab
Any questions or suggestions for improvement can be made by filling out the following form: https://forms.gle/YKiibhasVuYQ5goe6

**Figure 18** shows the Feedback tab.

![Feedback tab](https://raw.github.com/dbpedia/DBpedia-Spotlight-Dashboard/main/images/doc/19_feedback.png)
*&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Figure 18. Feedback tab*

### Evaluation
The usability of the Dashboard has been evaluated according to the following usability principles:
- Visibility of System Status
- Match between System and the Real World
- User Control and Freedom
- Consistency and Standards
- Recognition rather than Recall
- Flexibility and Efficiency of Use
- Aesthetic and Minimalist Design / Remove the Extraneous (Ink)
- Spatial Organization
- Information Coding
- Orientation

People who carried out the evaluation are related to the area of Entity Linking or with a profile in Computer Science.

The results obtained are the following:

| Usability principle                                         | Severity rating                                              |
|-------------------------------------------------------------|--------------------------------------------------------------|
| Visibility of System Status                                 | No Usability Problem - 66,7% \| Cosmetic Problem Only - 33,3%   |
| Match between System and the Real World                     | No Usability Problem - 83,3% \| Minor Usability Problem - 16,7% |
| User Control and Freedom                                    | No Usability Problem - 100%                                  |
| Consistency and Standards                                   | No Usability Problem - 100%                                  |
| Recognition rather than Recall                              | No Usability Problem - 83,3% \| Minor Usability Problem - 16,7% |
| Flexibility and Efficiency of Use                           | No Usability Problem - 83,3% \| Cosmetic Problem Only - 16,7%   |
| Aesthetic and Minimalist Design/Remove the Extraneous (Ink) | No Usability Problem - 83,3% \\| Cosmetic Problem Only - 16,7%   |
| Spatial Organization                                        | No Usability Problem - 83,3% \| Cosmetic Problem Only - 16,7%   |
| Information Coding                                          | No Usability Problem - 100%                                  |
| Orientation                                                 | No Usability Problem - 100%                                  |

In addition, the dashboard as a whole was also evaluated:

| Nº people who gave a global rating | Mark (from 0 to 10) |
|:----------------------------------:|:-------------------:|
|                  2                 |          8          |
|                  1                 |         8.5         |
|                  3                 |          9          |

After observing the results of the evaluation, it has been determined that **visual adjustments** can be made to improve the rating of the following usability principles:
- Visibility of System Status
- Flexibility and Efficiency of Use
- Aesthetic and Minimalist Design / Remove the Extraneous (Ink)
- Spatial Organization

Also, corrections or functionalities can be added to the dashboard to solve **minor usability problems** in the following usability principles:
- Match between System and the Real World
- Recognition rather than Recall

Finally, it has been concluded that the dashboard can be improved in some aspects but **is usable in general terms**.

###  Used Tools
 - [GNU datamash](https://www.gnu.org/software/datamash/) for statistics calculation

GNU datamash is a command-line program which performs basic numeric, textual and statistical operations on input textual data files.
 
| Operation | Description         | Example                                           |
|-----------|---------------------|---------------------------------------------------|
| sum       | Sum of the values   | ` seq 10 \| datamash sum 1`    |
| mean      | Mean of the values  | ` seq 10 \| datamash mean 1`   |
| pvar      | Population variance | ` seq 10 \| datamash pvar 1`   |
| median    | Median value        | ` seq 10 \| datamash median 1` |

 - [Dash framework](https://dash.plotly.com/) for building the web app
 
Dash is a productive Python framework for building web analytic applications.

Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.
 - [Plotly Python graphing library](https://plotly.com/python/) for visualizations

Plotly's Python graphing library makes interactive, publication-quality graphs. Examples of how to make line plots, scatter plots, area charts, bar charts, error bars, box plots, histograms, heatmaps, subplots, multiple-axes, polar charts, and bubble charts.

| Function       | Chart         |
|----------------|---------------|
| `go.Scatter()` | Scatter plot  |
| `go.Treemap()` | Treemap chart |
| `go.Bar()`     | Bar chart     |
| `go.Pie()`     | Pie chart     |

 - [Spyder IDE](https://www.spyder-ide.org/) for development and integration
 
Spyder is a free and open source scientific environment written in Python, for Python, and designed by and for scientists, engineers and data analysts. It features a unique combination of the advanced editing, analysis, debugging, and profiling functionality of a comprehensive development tool with the data exploration, interactive execution, deep inspection, and beautiful visualization capabilities of a scientific package.

### How to Run
In order to run the dashboard on yout local system, it is only necessary to:
- Clone the repository
- Go to the root folder and execute `main.sh` script

The script will install all the necessary packages and modules

The dashboard web page will be running at: http://localhost:8050

### Conclusions
Throughout this work:
 1. **Raw data** used by DBpedia Spotlight for the elaboration of models has been obtained
 2. These data have been submitted to the **entity validation process**
 3. **Statistical measures** have been calculated
 4. A **dashboard** has been built showing these measures using
    **cards** and **charts**.

Measures of central tendency, measures of dispersion and position measures have been calculated. **Measures of central tendency** are used to see where the data are grouped the most. **Measures of dispersion** are used to see the degree of variability of the data. **Position measures** divide the data into intervals of the same size.

After analyzing all these measures, the **high degree of dispersion** in the data has been observed, which means that the data is very far from the mean, that is, the data presents a high imbalance ratio. In addition, since entity types are highly unbalanced, much of the information in the dataset is covered by a small group of entities. Thus, after ordering the entities from highest to lowest, it was observed that the **first quartile** was covered by 1 or 2 types of entities, while the last quartile contained a large number of types of entities.

### Future Work
These are some tasks that would be interesting to do in the future:
- Include the rest of the languages available in DBpedia-Spotlight in the `Details` and `Instance-types comparison` tabs.
- Define the statistical information as Linked Data
- Define an onotlogy for the representation of statistical information
