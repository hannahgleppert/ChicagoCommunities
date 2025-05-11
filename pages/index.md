---
title: Chicago Community Insights
---
This is an app that allows you to interact with the City of Chicago's data. The database visualized by this app includes Zillow's, crime statistics, and education data. 


```sql map_info
SELECT 
  ZIPCodes AS ZIP, TOTAL_HOUSEHOLDS
FROM 
  community.housing_stats
GROUP BY 
  ZIP;
```


<AreaMap
  data={map_info}
  geoJsonUrl="/chicago_zipcodes.geojson"
  geoId=ZIP
  areaCol=ZIP
  value=TOTAL_HOUSEHOLDS
/>


```sql description
select count(*) as count 
from community.housing_stats
```

<Details title='About this data'>
This dataset includes information about <Value data={description} column=count/> communities in Chicago.

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
