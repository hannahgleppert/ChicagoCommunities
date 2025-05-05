
---
title: Chicago Community Insights
---
This is an app that allows you to interact with the City of Chicago's data. The database visualized by this app includes Zillow's, crime statistics, and education data. 


```sql communities
SELECT CommunityArea, CommunityNo, FamilyUnits
FROM community.housing_data
```


<AreaMap
  data={communities}
  geoJsonUrl="/static/chicago.geojson"
  geoId=area_num_1
  areaCol=CommunityNo
  value=FamilyUnits
/>


```sql description
select count(*) as count 
from community.housing_data
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
