---
title: Community Scores
---

```sql zipscores_overall
SELECT 
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "NeighborhoodScore",
  "Rank"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```
```sql zipscores_education
select 
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "MedEnrollment", 
  "MedGraduation",
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```
```sql zipscores_crime
select
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "DrugCrimes",
  "PropertyCrimes",
  "ViolentCrimes",
  "Other"
FROM zip_scores
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
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

```sql zipscores_housing
select
  LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 
  "Forclosure2023",
  "Foreclosure_rate",
FROM zip_scores
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
            {id: 'NeighborhoodScore', title: 'Neighborhood Scores', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
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
          value=DrugCrimes
          title="Crime Scores"
          tooltip={[
            {id: 'DrugCrimes', title: 'Drug Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'PropertyCrimes', title: 'Property Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'PropertyCrimes', title: 'Property Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'ViolentCrimes', title: 'Violent Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Other', title: 'Other Crimes since 2001', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
          ]}
        />

    ###### Colors represent Drug Crimes values.
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
          value=Forclosure2023
          title="Housing Scores"
          tooltip={[
            {id: 'Forclosure2023', title:'Foreclosures 2023', fmt: 'id', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
            {id: 'Foreclosure_rate', title:'Foreclosure Rate per 10,000 People', fmt: 'id', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
          ]}
        />

    ###### Colors represent Foreclosures 2023 values.

    </Group>
</Grid>