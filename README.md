# accessible-wayfinding-systematic-review-data

Raw data and associated tools (Jupyter notebooks for each step of the workflow) for a systematic review of accessible wayfinding and navigation, conducted using as described in Section 3 of [Prandi et al.'s "Accesible wayfinding and navigation: a systematic mapping study"](https://link.springer.com/article/10.1007/s10209-021-00843-x) (Research question: "Which devices and software applications for accessible wayfinding and navigation have been proposed in scientific literature?"), but updated for post-2021. Search conducted May 25, 2023 using Scopus (access provided by UNC Chapel Hill Libraries).

## Contributions and Data Availability
- Feel free to clone and/or fork for your use! Contributions via pull request are welcome.
- If relevant, I ask that you cite this repository with the website link (https://github.com/christineiym/accessible-wayfinding-systematic-review-data). Thanks!
- To request final analysis results, please email [christine.mendoza@unc.edu](mailto:christine.mendoza@unc.edu)! 

## Paper Search Criteria

*Initial search string:* (accessible OR accessibility) AND (city OR indoor OR urban OR campus OR university) AND (wayfinding OR navigation OR mobility) AND (application OR system OR map)

*Scopus subjects:* "Computer Science", "Engineering"

*Publication time range:* 2021, 2022 (2023 is analyzed separately)

*Language*: English

- Note: While Prandi et al. do not consider papers not written in English, this repository briefly examines Spanish-language papers from 2010 to 2023 separately, albeit limited by the English-language focus of Scopus.

*Final search string:*
```
TITLE-ABS-KEY ( ( accessible  OR  accessibility )  AND  ( city  OR  indoor  OR  urban  OR  campus  OR  university )  AND  ( wayfinding  OR  navigation  OR  mobility )  AND  ( application  OR  system  OR  map ) )  AND  ( LIMIT-TO ( SUBJAREA ,  "ENGI" )  OR  LIMIT-TO ( SUBJAREA ,  "COMP" ) )  AND  ( LIMIT-TO ( PUBYEAR ,  2022 )  OR  LIMIT-TO ( PUBYEAR ,  2021 ) )  AND  ( LIMIT-TO ( LANGUAGE ,  "English" ) ) 
```

## Exclusion Criteria

### Stage 1

*Aspects analyzed:* Title, abstract, paper type

*Exclusion criteria:* Off-topic, duplicates, introductory papers to conference/workshop proceedings

### Stage 2

*Aspects analyzed:* Title, abstract, paper type, paper text

*Exclusion criteria:* Preliminary work, extended abstract, requirement analysis (versus actual application), systems for data collection and storage, conceptual model, user study or guidelines, survey/review

- Note: survey/reviews are analyzed separately.

## Analysis Criteria

### Overview of Dimensions (adapted from Prandi et al.)
1) Context of use
2) Target population
3) Technology type
4) Data sources type
5) User involvement in system design and evaluation

### Keywords
- How many have keywords?
- Average number of keywords per paper? Standard deviation? Median?
- Most frequent keywords? Number of occurrences?

### Device classification
- Mobile application
- Web application
- Wearable
- Smart
- Tactile/public interfaces
- Multiple

### Dimension 1: Context of Use
- Indoor
- Outdoor
- Indoor AND outdoor

### Dimension 2: Target population
- Visually impaired
- Mobility impaired
- Cognitive
- Hearing
- Other
- All

### Dimension 3: Technology type
- Environment representation and modeling
- Localization
- Wayfinding and navigation

### Dimension 4: Data sources
- Crowdsourcing
- Crowdsensing and pervasive sending
- Official and expert
- Multi-source

### Dimension 5: User involvement in system design and evaluation
- None
- Design time
- System evaluation
- Both