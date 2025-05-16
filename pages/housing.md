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
   value="IncomeScore"
   name=IncomeScore
   title = "Income Score"
/>

<Details title='Scoring System'>
   Scoring System Methodology
   
 </Details>

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
   value="Foreclosure Rate per 10,000 People"
   title="Foreclosure Rate per 10,000 People"
/>