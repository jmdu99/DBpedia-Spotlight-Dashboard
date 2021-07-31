# -*- coding: utf-8 -*-
import os
import resources as R
import json

src_path = os.path.dirname(os.path.realpath(__file__))
root_path = src_path.replace("src","")
resources_directory = root_path + "resources/"
es_stats= R.es_stats
en_stats= R.en_stats
versions_stats = R.versions_stats

es= {}
# Instance types
es["Instance types"] = {}
es["Instance types"]["Oct 2016"] = {}
es["Instance types"]["Oct 2016"]["N elements"] = versions_stats[1]
es["Instance types"]["Oct 2016"]["Mean"] = versions_stats[2]
es["Instance types"]["Oct 2016"]["Median"] = 'dbo:Athlete'
es["Instance types"]["Oct 2016"]["Mode"] = 'dbo:Agent'
es["Instance types"]["Oct 2016"]["Standard deviation"] = versions_stats[4]
es["Instance types"]["Oct 2020"] = {}
es["Instance types"]["Oct 2020"]["N elements"] = versions_stats[19]
es["Instance types"]["Oct 2020"]["Mean"] = versions_stats[20]
es["Instance types"]["Oct 2020"]["Median"] = 'dbo:AdministrativeRegion'
es["Instance types"]["Oct 2020"]["Mode"] = 'dbo:Agent'
es["Instance types"]["Oct 2020"]["Standard deviation"] = versions_stats[22]
es["Instance types"]["May 2021"] = {}
es["Instance types"]["May 2021"]["N elements"] = versions_stats[37]
es["Instance types"]["May 2021"]["Mean"] = versions_stats[38]
es["Instance types"]["May 2021"]["Median"] = 'dbo:AdministrativeRegion'
es["Instance types"]["May 2021"]["Mode"] = 'dbo:Agent'
es["Instance types"]["May 2021"]["Standard deviation"] = versions_stats[40]
es["Instance types"]["Jun 2021"] = {}
es["Instance types"]["Jun 2021"]["N elements"] = versions_stats[55]
es["Instance types"]["Jun 2021"]["Mean"] = versions_stats[56]
es["Instance types"]["Jun 2021"]["Median"] = 'dbo:AdministrativeRegion'
es["Instance types"]["Jun 2021"]["Mode"] = 'dbo:Agent'
es["Instance types"]["Jun 2021"]["Standard deviation"] = versions_stats[58]
#uriCounts
es["uriCounts"] = {}
es["uriCounts"]["Oct 2016"] = {}
es["uriCounts"]["Oct 2016"]["N elements"] = es_stats[42]
es["uriCounts"]["Oct 2016"]["Mean"] = es_stats[43]
es["uriCounts"]["Oct 2016"]["Median"] = 'dbpedia-es:Hinduismo'
es["uriCounts"]["Oct 2016"]["Mode"] = 'dbpedia-es:' + R.top_2016_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["Oct 2016"]["Standard deviation"] = es_stats[45]
es["uriCounts"]["Oct 2020"] = {}
es["uriCounts"]["Oct 2020"]["N elements"] = es_stats[82]
es["uriCounts"]["Oct 2020"]["Mean"] = es_stats[83]
es["uriCounts"]["Oct 2020"]["Median"] = 'dbpedia-es:Huiracocha_Inca'
es["uriCounts"]["Oct 2020"]["Mode"] = 'dbpedia-es:' + R.top_2020_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["Oct 2020"]["Standard deviation"] = es_stats[85]
es["uriCounts"]["May 2021"] = {}
es["uriCounts"]["May 2021"]["N elements"] = es_stats[22]
es["uriCounts"]["May 2021"]["Mean"] = es_stats[23]
es["uriCounts"]["May 2021"]["Median"] = 'dbpedia-es:III_milenio_a._C.'
es["uriCounts"]["May 2021"]["Mode"] = 'dbpedia-es:' + R.top_2021_05_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["May 2021"]["Standard deviation"] = es_stats[25]
es["uriCounts"]["Jun 2021"] = {}
es["uriCounts"]["Jun 2021"]["N elements"] = es_stats[62]
es["uriCounts"]["Jun 2021"]["Mean"] = es_stats[63]
es["uriCounts"]["Jun 2021"]["Median"] = 'dbpedia-es:ITunes_Store'
es["uriCounts"]["Jun 2021"]["Mode"] = 'dbpedia-es:' + R.top_2021_06_uriCounts_es['DBpedia entity'].iloc[0]
es["uriCounts"]["Jun 2021"]["Standard deviation"] = es_stats[65]
#pairCounts
es["pairCounts"] = {}
es["pairCounts"]["Oct 2016"] = {}
es["pairCounts"]["Oct 2016"]["N elements"] = es_stats[46]
es["pairCounts"]["Oct 2016"]["Mean"] = es_stats[47]
es["pairCounts"]["Oct 2016"]["Median"] = '[hinduista - dbpedia-es:Hinduismo]'
es["pairCounts"]["Oct 2016"]["Mode"] = "[" + R.top_2016_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2016_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["Oct 2016"]["Standard deviation"] = es_stats[49]
es["pairCounts"]["Oct 2020"] = {}
es["pairCounts"]["Oct 2020"]["N elements"] = es_stats[86]
es["pairCounts"]["Oct 2020"]["Mean"] = es_stats[87]
es["pairCounts"]["Oct 2020"]["Median"] = '[Wiracocha - dbpedia-es:Huiracocha_(dios)]'
es["pairCounts"]["Oct 2020"]["Mode"] = "[" + R.top_2020_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2020_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["Oct 2020"]["Standard deviation"] = es_stats[89]
es["pairCounts"]["May 2021"] = {}
es["pairCounts"]["May 2021"]["N elements"] = es_stats[26]
es["pairCounts"]["May 2021"]["Mean"] = es_stats[27]
es["pairCounts"]["May 2021"]["Median"] = '[artículo - dbpedia-es:Película_de_culto]'
es["pairCounts"]["May 2021"]["Mode"] = "[" + R.top_2021_05_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_05_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["May 2021"]["Standard deviation"] = es_stats[29]
es["pairCounts"]["Jun 2021"] = {}
es["pairCounts"]["Jun 2021"]["N elements"] = es_stats[66]
es["pairCounts"]["Jun 2021"]["Mean"] = es_stats[67]
es["pairCounts"]["Jun 2021"]["Median"] = '[Herois (Héroes) - dbpedia-es:Héroes_(película)]'
es["pairCounts"]["Jun 2021"]["Mode"] = "[" + R.top_2021_06_pairCounts_es['Surface form'].iloc[0] + " - " + 'dbpedia-es:'+ R.top_2021_06_pairCounts_es['DBpedia entity'].iloc[0] + "]"
es["pairCounts"]["Jun 2021"]["Standard deviation"] = es_stats[69]
#tokenCounts
es["tokenCounts"] = {}
es["tokenCounts"]["Oct 2016"] = {}
es["tokenCounts"]["Oct 2016"]["N elements"] = es_stats[50]
es["tokenCounts"]["Oct 2016"]["Mean"] = es_stats[51]
es["tokenCounts"]["Oct 2016"]["Median"] = 'http://es.wikipedia.org/wiki/Imperio_almohade'
es["tokenCounts"]["Oct 2016"]["Mode"] = 'http://es.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["Oct 2016"]["Standard deviation"] = es_stats[52]
es["tokenCounts"]["Oct 2020"] = {}
es["tokenCounts"]["Oct 2020"]["N elements"] = es_stats[90]
es["tokenCounts"]["Oct 2020"]["Mean"] = es_stats[91]
es["tokenCounts"]["Oct 2020"]["Median"] = 'http://es.wikipedia.org/wiki/Idioma_ruso_en_Ucrania'
es["tokenCounts"]["Oct 2020"]["Mode"] = 'http://es.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["Oct 2020"]["Standard deviation"] = es_stats[92]
es["tokenCounts"]["May 2021"] = {}
es["tokenCounts"]["May 2021"]["N elements"] = es_stats[30]
es["tokenCounts"]["May 2021"]["Mean"] = es_stats[31]
es["tokenCounts"]["May 2021"]["Median"] = 'http://es.wikipedia.org/wiki/Impunidad'
es["tokenCounts"]["May 2021"]["Mode"] = 'http://es.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["May 2021"]["Standard deviation"] = es_stats[32]
es["tokenCounts"]["Jun 2021"] = {}
es["tokenCounts"]["Jun 2021"]["N elements"] = es_stats[70]
es["tokenCounts"]["Jun 2021"]["Mean"] = es_stats[71]
es["tokenCounts"]["Jun 2021"]["Median"] = 'http://es.wikipedia.org/wiki/Invierno'
es["tokenCounts"]["Jun 2021"]["Mode"] = 'http://es.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_es['Wikipedia article'].iloc[0]
es["tokenCounts"]["Jun 2021"]["Standard deviation"] = es_stats[72]
#sfAndTotalCounts
es["sfAndTotalCounts"] = {}
es["sfAndTotalCounts"]["Oct 2016"] = {}
es["sfAndTotalCounts"]["Oct 2016"]["N elements"] = es_stats[54]
es["sfAndTotalCounts"]["Oct 2016"]["Mean"] = es_stats[59]
es["sfAndTotalCounts"]["Oct 2016"]["Median"] ='doris miller'
es["sfAndTotalCounts"]["Oct 2016"]["Mode"] = R.top_2016_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["Oct 2016"]["Standard deviation"] = es_stats[61]
es["sfAndTotalCounts"]["Oct 2020"] = {}
es["sfAndTotalCounts"]["Oct 2020"]["N elements"] = es_stats[94]
es["sfAndTotalCounts"]["Oct 2020"]["Mean"] = es_stats[99]
es["sfAndTotalCounts"]["Oct 2020"]["Median"] = 'Ciudad del Vaticano'
es["sfAndTotalCounts"]["Oct 2020"]["Mode"] = R.top_2020_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["Oct 2020"]["Standard deviation"] = es_stats[101]
es["sfAndTotalCounts"]["May 2021"] = {}
es["sfAndTotalCounts"]["May 2021"]["N elements"] = es_stats[34]
es["sfAndTotalCounts"]["May 2021"]["Mean"] =es_stats[39]
es["sfAndTotalCounts"]["May 2021"]["Median"] = 'pulmonar'
es["sfAndTotalCounts"]["May 2021"]["Mode"] = R.top_2021_05_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["May 2021"]["Standard deviation"] = es_stats[41]
es["sfAndTotalCounts"]["Jun 2021"] = {}
es["sfAndTotalCounts"]["Jun 2021"]["N elements"] = es_stats[74]
es["sfAndTotalCounts"]["Jun 2021"]["Mean"] = es_stats[79]
es["sfAndTotalCounts"]["Jun 2021"]["Median"] = 'culebrera europea'
es["sfAndTotalCounts"]["Jun 2021"]["Mode"] = R.top_2021_06_sfAndTotalCounts_es['Surface form'].iloc[0]
es["sfAndTotalCounts"]["Jun 2021"]["Standard deviation"] = es_stats[81]

en= {}
# Instance types
en["Instance types"] = {}
en["Instance types"]["Oct 2016"] = {}
en["Instance types"]["Oct 2016"]["N elements"] = versions_stats[73]
en["Instance types"]["Oct 2016"]["Mean"] = versions_stats[74]
en["Instance types"]["Oct 2016"]["Median"] = 'dbo:Work'
en["Instance types"]["Oct 2016"]["Mode"] = 'dbo:Agent'
en["Instance types"]["Oct 2016"]["Standard deviation"] = versions_stats[76]
en["Instance types"]["Oct 2020"] = {}
en["Instance types"]["Oct 2020"]["N elements"] = versions_stats[91]
en["Instance types"]["Oct 2020"]["Mean"] = versions_stats[92]
en["Instance types"]["Oct 2020"]["Median"] = 'dbo:Work'
en["Instance types"]["Oct 2020"]["Mode"] = 'dbo:Agent'
en["Instance types"]["Oct 2020"]["Standard deviation"] = versions_stats[94]
en["Instance types"]["May 2021"] = {}
en["Instance types"]["May 2021"]["N elements"] = versions_stats[109]
en["Instance types"]["May 2021"]["Mean"] = versions_stats[110]
en["Instance types"]["May 2021"]["Median"] = 'dbo:Work'
en["Instance types"]["May 2021"]["Mode"] = 'dbo:Agent'
en["Instance types"]["May 2021"]["Standard deviation"] = versions_stats[112]
en["Instance types"]["Jun 2021"] = {}
en["Instance types"]["Jun 2021"]["N elements"] = versions_stats[127]
en["Instance types"]["Jun 2021"]["Mean"] = versions_stats[128]
en["Instance types"]["Jun 2021"]["Median"] = 'dbo:AdministrativeRegion'
en["Instance types"]["Jun 2021"]["Mode"] = 'dbo:Agent'
en["Instance types"]["Jun 2021"]["Standard deviation"] = versions_stats[130]
#uriCounts
en["uriCounts"] = {}
en["uriCounts"]["Oct 2016"] = {}
en["uriCounts"]["Oct 2016"]["N elements"] = en_stats[42]
en["uriCounts"]["Oct 2016"]["Mean"] = en_stats[43]
en["uriCounts"]["Oct 2016"]["Median"] = 'dbr:Latvian_constitutional_referendum,_2008'
en["uriCounts"]["Oct 2016"]["Mode"] = 'dbr:' + R.top_2016_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["Oct 2016"]["Standard deviation"] = en_stats[45]
en["uriCounts"]["Oct 2020"] = {}
en["uriCounts"]["Oct 2020"]["N elements"] = en_stats[82]
en["uriCounts"]["Oct 2020"]["Mean"] = en_stats[83]
en["uriCounts"]["Oct 2020"]["Median"] = 'dbr:Lamar_University'
en["uriCounts"]["Oct 2020"]["Mode"] = 'dbr:' + R.top_2020_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["Oct 2020"]["Standard deviation"] = en_stats[85]
en["uriCounts"]["May 2021"] = {}
en["uriCounts"]["May 2021"]["N elements"] = en_stats[22]
en["uriCounts"]["May 2021"]["Mean"] = en_stats[23]
en["uriCounts"]["May 2021"]["Median"] = 'dbr:Kyrgyzstan_national_football_team'
en["uriCounts"]["May 2021"]["Mode"] = 'dbr:' + R.top_2021_05_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["May 2021"]["Standard deviation"] = en_stats[25]
en["uriCounts"]["Jun 2021"] = {}
en["uriCounts"]["Jun 2021"]["N elements"] = en_stats[62]
en["uriCounts"]["Jun 2021"]["Mean"] = en_stats[63]
en["uriCounts"]["Jun 2021"]["Median"] = 'dbr:Kwame_Nkrumah_University_of_Science_and_Technology'
en["uriCounts"]["Jun 2021"]["Mode"] = 'dbr:' + R.top_2021_06_uriCounts_en['DBpedia entity'].iloc[0]
en["uriCounts"]["Jun 2021"]["Standard deviation"] = en_stats[65]
#pairCounts
en["pairCounts"] = {}
en["pairCounts"]["Oct 2016"] = {}
en["pairCounts"]["Oct 2016"]["N elements"] = en_stats[46]
en["pairCounts"]["Oct 2016"]["Mean"] = en_stats[47]
en["pairCounts"]["Oct 2016"]["Median"] = '[part of the Soviet Union - dbr:Latvian_Soviet_Socialist_Republic]'
en["pairCounts"]["Oct 2016"]["Mode"] = "[" + R.top_2016_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2016_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["Oct 2016"]["Standard deviation"] = en_stats[49]
en["pairCounts"]["Oct 2020"] = {}
en["pairCounts"]["Oct 2020"]["N elements"] = en_stats[86]
en["pairCounts"]["Oct 2020"]["Mean"] = en_stats[87]
en["pairCounts"]["Oct 2020"]["Median"] = '[Lamar Softball Complex - dbr:Lamar_Softball_Complex]'
en["pairCounts"]["Oct 2020"]["Mode"] = "[" + R.top_2020_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2020_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["Oct 2020"]["Standard deviation"] = en_stats[89]
en["pairCounts"]["May 2021"] = {}
en["pairCounts"]["May 2021"]["N elements"] = en_stats[26]
en["pairCounts"]["May 2021"]["Mean"] = en_stats[27]
en["pairCounts"]["May 2021"]["Median"] = '[Wallenpaupack - dbr:Lake_Wallenpaupack]'
en["pairCounts"]["May 2021"]["Mode"] = "[" + R.top_2021_05_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_05_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["May 2021"]["Standard deviation"] = en_stats[29]
en["pairCounts"]["Jun 2021"] = {}
en["pairCounts"]["Jun 2021"]["N elements"] = en_stats[66]
en["pairCounts"]["Jun 2021"]["Mean"] = en_stats[67]
en["pairCounts"]["Jun 2021"]["Median"] = '[Lakdi ka pul - dbr:Lakdi_ka_pul]'
en["pairCounts"]["Jun 2021"]["Mode"] = "[" + R.top_2021_06_pairCounts_en['Surface form'].iloc[0] + " - " + 'dbr:'+ R.top_2021_06_pairCounts_en['DBpedia entity'].iloc[0] + "]"
en["pairCounts"]["Jun 2021"]["Standard deviation"] = en_stats[69]
#tokenCounts
en["tokenCounts"] = {}
en["tokenCounts"]["Oct 2016"] = {}
en["tokenCounts"]["Oct 2016"]["N elements"] = en_stats[50]
en["tokenCounts"]["Oct 2016"]["Mean"] = en_stats[51]
en["tokenCounts"]["Oct 2016"]["Median"] = 'http://en.wikipedia.org/wiki/Kushti'
en["tokenCounts"]["Oct 2016"]["Mode"] = 'http://en.wikipedia.org/wiki/'+ R.top_2016_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["Oct 2016"]["Standard deviation"] = en_stats[52]
en["tokenCounts"]["Oct 2020"] = {}
en["tokenCounts"]["Oct 2020"]["N elements"] = en_stats[90]
en["tokenCounts"]["Oct 2020"]["Mean"] = en_stats[91]
en["tokenCounts"]["Oct 2020"]["Median"] = 'http://en.wikipedia.org/wiki/Klondike_Open'
en["tokenCounts"]["Oct 2020"]["Mode"] = 'http://en.wikipedia.org/wiki/'+ R.top_2020_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["Oct 2020"]["Standard deviation"] = en_stats[92]
en["tokenCounts"]["May 2021"] = {}
en["tokenCounts"]["May 2021"]["N elements"] = en_stats[30]
en["tokenCounts"]["May 2021"]["Mean"] = en_stats[31]
en["tokenCounts"]["May 2021"]["Median"] = 'http://en.wikipedia.org/wiki/Klas_Lund'
en["tokenCounts"]["May 2021"]["Mode"] = 'http://en.wikipedia.org/wiki/'+ R.top_2021_05_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["May 2021"]["Standard deviation"] = en_stats[32]
en["tokenCounts"]["Jun 2021"] = {}
en["tokenCounts"]["Jun 2021"]["N elements"] = en_stats[70]
en["tokenCounts"]["Jun 2021"]["Mean"] = en_stats[71]
en["tokenCounts"]["Jun 2021"]["Median"] = 'http://en.wikipedia.org/wiki/Kovno_Kollel'
en["tokenCounts"]["Jun 2021"]["Mode"] = 'http://en.wikipedia.org/wiki/'+ R.top_2021_06_tokenCounts_en['Wikipedia article'].iloc[0]
en["tokenCounts"]["Jun 2021"]["Standard deviation"] = en_stats[72]
#sfAndTotalCounts
en["sfAndTotalCounts"] = {}
en["sfAndTotalCounts"]["Oct 2016"] = {}
en["sfAndTotalCounts"]["Oct 2016"]["N elements"] = en_stats[54]
en["sfAndTotalCounts"]["Oct 2016"]["Mean"] = en_stats[59]
en["sfAndTotalCounts"]["Oct 2016"]["Median"] = 'Deep Cove'
en["sfAndTotalCounts"]["Oct 2016"]["Mode"] = R.top_2016_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["Oct 2016"]["Standard deviation"] = en_stats[61]
en["sfAndTotalCounts"]["Oct 2020"] = {}
en["sfAndTotalCounts"]["Oct 2020"]["N elements"] = en_stats[94]
en["sfAndTotalCounts"]["Oct 2020"]["Mean"] = en_stats[99]
en["sfAndTotalCounts"]["Oct 2020"]["Median"] = 'The Herald'
en["sfAndTotalCounts"]["Oct 2020"]["Mode"] = R.top_2020_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["Oct 2020"]["Standard deviation"] = en_stats[101]
en["sfAndTotalCounts"]["May 2021"] = {}
en["sfAndTotalCounts"]["May 2021"]["N elements"] = en_stats[34]
en["sfAndTotalCounts"]["May 2021"]["Mean"] =en_stats[39]
en["sfAndTotalCounts"]["May 2021"]["Median"] = 'DC Comics'
en["sfAndTotalCounts"]["May 2021"]["Mode"] = R.top_2021_05_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["May 2021"]["Standard deviation"] = en_stats[41]
en["sfAndTotalCounts"]["Jun 2021"] = {}
en["sfAndTotalCounts"]["Jun 2021"]["N elements"] = en_stats[74]
en["sfAndTotalCounts"]["Jun 2021"]["Mean"] = en_stats[79]
en["sfAndTotalCounts"]["Jun 2021"]["Median"] = 'Cyropaedia'
en["sfAndTotalCounts"]["Jun 2021"]["Mode"] = R.top_2021_06_sfAndTotalCounts_en['Surface form'].iloc[0]
en["sfAndTotalCounts"]["Jun 2021"]["Standard deviation"] = en_stats[81]

es_dashboard_stats = json.dumps(es,indent=4)
en_dashboard_stats = json.dumps(en,indent=4)
es_json = open(resources_directory + "es_stats.json", "w")
es_json.write(es_dashboard_stats)
es_json.close()
en_json = open(resources_directory + "en_stats.json", "w")
en_json.write(en_dashboard_stats)
en_json.close()

