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


```sql community_housing
select
  "CommunityNo" as CommunityNo,
  "Geography" as Community,
  "Total_Population" as Population,
from
  community_housing_stats
group by all;
order by CommunityNo
```


<AreaMap
  data={community_housing}
  geoJsonUrl="/chicago-community-areas.geojson"
  geoId=area_numbe
  areaCol=CommunityNo
  value=Population
  title = "Community Populations"
  tooltip={[
    {id: 'Community', fmt: 'id', showColumnName: false, valueClass: 'text-xl font-semibold'},
    {id: 'Population', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    ]}
/>


```sql foreclosures_by_year
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2010 as year,
  "Foreclosures_2010" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2011 as year,
  "Foreclosures_2011" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2012 as year,
  "Foreclosures_2012" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2013 as year,
  "Foreclosures_2013" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2014 as year,
  "Foreclosures_2014" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2015 as year,
  "Foreclosures_2015" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2016 as year,
  "Foreclosures_2016" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2017 as year,
  "Foreclosures_2017" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2018 as year,
  "Foreclosures_2018" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2019 as year,
  "Foreclosures_2019" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2020 as year,
  "Foreclosures_2020" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2021 as year,
  "Foreclosures_2021" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2022 as year,
  "Foreclosures_2022" as foreclosures
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2023 as year,
  "Foreclosures_2023" as foreclosures
from community_housing_stats
```

<Value 
data={foreclosures_by_year} 
column=year
fmt='yyyy' 
/>

<LineChart
  data={foreclosures_by_year}
  x=year
  y=foreclosures
  series=community
/>