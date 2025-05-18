---
title: Community Scores
---

<Details title='Community Score'>
  Scoring System Methodology for Community Score:
  The Community Scores for each neighborhood were calculated using a weighted combination of eight variables spanning education, housing, and crime. Each variable was assigned a specific weight based on its perceived impact on overall neighborhood quality. Positive weights were given to favorable indicators, including median college enrollment (0.20), median high school graduation rate (0.20), and the Income Score (0.20), which account for educational attainment and quality of housing. Conversely, negative weights were applied to less desirable factors such as foreclosure rate (-0.20), drug-related crimes (-0.10), other crimes (-0.03), property crimes (-0.12), and violent crime (-0.35), with violent crime receiving the highest negative weight due to its significant impact on safety and livability. By summing the weighted values for each ZIP code, we produced a single Community Score that enables neighborhood-to-neighborhood comparisons.
</Details>

<Details title='Income Score'>
  Scoring System Methodology for Income Score:
  To create the Income Score used in the Community Score calculation, we categorized homeowner income levels into four brackets: under $25,000, between $25,000 and $50,000, between $50,000 and $100,000, and over $100,000. Each bracket was assigned a weight reflecting its relative contribution to neighborhood socioeconomic advantage, with weights of 1, 3, 5, and 6 respectively. These weights were then applied to the percentage of homeowners in each ZIP code falling into each income category. By applying the weighted percentages, we generated a single Income Score for each neighborhood, with higher scores representing a greater concentration of higher-income households.
</Details>

```sql zipscores_overall
SELECT 
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "NeighborhoodScore",
  "Rank"
FROM zip_scores_full
WHERE ZipCode IS NOT NULL;
```
```sql zipscores_education
select 
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "MedEnrollment", 
  "MedGraduation",
FROM zip_scores_full
WHERE ZipCode IS NOT NULL;
```
```sql zipscores_crime
select
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "DrugCrimes",
  "PropertyCrimes",
  "ViolentCrimes",
  "Other"
FROM zip_scores_full
WHERE ZipCode IS NOT NULL;
```
```sql zipscores_population_and_income
select
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "IncomeScore",
  "Income_<25k",
  "Income_>25K_<50K",
  "Income_>50K_<100K",
  "Income_>100K",
  "Population",
FROM zip_scores_full
WHERE ZipCode IS NOT NULL;
```

```sql zipscores_housing
select
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "Forclosure2023",
  "Foreclosure_rate",
FROM zip_scores_full
WHERE ZipCode IS NOT NULL;
```


<AreaMap
  data={zipscores_overall}
  geoJsonUrl="/Cook_County_Zip_Code.geojson"
  geoId=zip
  areaCol=ZIP
  value=Rank
  legend=true
  legendType=scalar
  title="Overall Scores"
  tooltip={[
            {id: 'Rank', title: 'Rank', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'NeighborhoodScore', title: 'Community Scores', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            ]}
/>

###### Colors represent Rank values.

<Grid cols=2>
    <Group>


        <AreaMap
          data={zipscores_crime}
          geoJsonUrl="/Cook_County_Zip_Code.geojson"
          geoId=zip
          areaCol=ZIP
          value=ViolentCrimes
          title="Crime Scores"
          tooltip={[
            {id: 'DrugCrimes', title: 'Drug Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'PropertyCrimes', title: 'Property Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'PropertyCrimes', title: 'Property Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'ViolentCrimes', title: 'Violent Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Other', title: 'Other Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
          ]}
        />

    ###### Colors represent Violent Crime values.
    </Group>
    <Group>

        <AreaMap
          data={zipscores_education}
          geoJsonUrl="/Cook_County_Zip_Code.geojson"
          geoId=zip
          areaCol=ZIP
          value=MedEnrollment
          title="Education Scores"
          tooltip={[
            {id: 'MedEnrollment', title: 'Median Enrollment in Colleges', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'MedGraduation', title: 'Median Graduation Rate of High Schools', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
          ]}
        />

    ###### Colors represent Median Enrollment in Colleges values.
    </Group>
    <Group>

        <AreaMap
          data={zipscores_population_and_income}
          geoJsonUrl="/Cook_County_Zip_Code.geojson"
          geoId=zip
          areaCol=ZIP
          value=IncomeScore
          title="Income and Population Scores"
          tooltip={[
            {id: 'IncomeScore', title:'Income Score', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Income_<25k', title:'Income Less than 25K', fmt: 'pct', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Income_>25K_<50K', title:'Income between 25K and 50K', fmt: 'pct', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Income_>50K_<100K', title:'Income between 50K and 100K', fmt: 'pct', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Income_greater_than_100K', title:'Income greater than 100K', fmt: 'ct', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Population', title:'Population', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
          ]}
        />

    ###### Colors represent Income Score values.
    </Group>
    <Group>

        <AreaMap
          data={zipscores_housing}
          geoJsonUrl="/Cook_County_Zip_Code.geojson"
          geoId=zip
          areaCol=ZIP
          value=Foreclosure_rate
          title="Housing Scores"
          tooltip={[
            {id: 'Forclosure2023', title:'Foreclosures 2023', fmt: 'id', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Foreclosure_rate', title:'Foreclosure Rate per 10,000 People', fmt: 'id', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
          ]}
        />

    ###### Colors represent Foreclosures Rate using 2023 foreclosure values.

    </Group>
</Grid>

### Education

 ```sql medGraduation
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "MedGraduation" AS "Median Graduation Rate of High Schools"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={medGraduation}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Median Graduation Rate of High Schools"
   value="Median Graduation Rate of High Schools"
   name="Median Graduation Rate of High Schools"
/>

 ```sql medEnrollment
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "MedEnrollment" AS "Median Enrollment in Colleges" 
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={medEnrollment}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Median Enrollment in Colleges" 
   value="Median Enrollment in Colleges" 
   name="Median Enrollment in Colleges" 
/>

### Housing

```sql incomeScore
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "IncomeScore"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={incomeScore}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Income Score"
   value="IncomeScore"
   name=IncomeScore
/>

 ```sql foreclosureRate
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "Foreclosure_rate" AS "Foreclosure Rate per 10,000 People"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={foreclosureRate}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Foreclosure Rate per 10,000 People"
   value="Foreclosure Rate per 10,000 People"
   name=Foreclosure Rate per 10,000 People
/>

### Crime 

```sql violentCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "ViolentCrimes" AS "Violent Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={violentCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Violent Crimes since 2001"
   value="Violent Crimes since 2001"
   name=violent_crimes
/>

 ```sql drugCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "ViolentCrimes" AS "Drug Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={drugCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Drug Crimes since 2001"
   value="Drug Crimes since 2001"
   name=drug_crimes
/>

 ```sql propertyCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "PropertyCrimes" AS "Property Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={propertyCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Property Crimes since 2001"
   value="Property Crimes since 2001"
   name=property_crimes
/>

 ```sql otherCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "Other" AS "Other Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={otherCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   title="Other Crimes since 2001"
   value="Other Crimes since 2001"
   name=other_crimes
/>
