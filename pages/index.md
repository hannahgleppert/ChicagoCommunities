---
title: Chicago Insights Dashboard
---
This dashboard allows you to interact with the City of Chicago's data. The database visualized by this app includes Zillow's, crime statistics, and education data. 


```sql housing
SELECT  
  LPAD(CAST("ZIP" AS TEXT), 5, '0') AS ZIP,
  AVG("TOTAL_HOUSEHOLDS") AS TOTAL_HOUSEHOLDS
FROM 
  community.housing_stats
GROUP BY 
  ZIP;
```


```sql population_and_income
select
  "ZipCode" as ZIP,
  "Population" as Population,
  "Growth" as Growth,
  "Age" as Average_Age,
  "Income per household" as Income,
from
  community.population_income
group by all;
```


<AreaMap
  data={population_and_income}
  geoJsonUrl="/Cook_County_Zip_Code.geojson"
  geoId=zip
  areaCol=ZIP
  value=Population
  title = "Population and Income Data of Chicago"
  tooltip={[
    {id: 'ZIP', fmt: 'id', showColumnName: false, valueClass: 'text-xl font-semibold'},
    {id: 'Population', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    {id: 'Growth', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    {id: 'Average_Age', fmt: 'num0', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    {id: 'Income', fmt: 'usd', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    
]}
/>


<Details title='About this data'>

    <Details title='Zillow'>
     Information about Zillow's data.
    </Details>
    <Details title='Crime'>
    Information about crime data.
    </Details>
     <Details title='Education'>
     Information about education data.
    </Details>

 </Details>
