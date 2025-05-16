 ```sql incomeScore
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "IncomeScore"
FROM zip_scores_full
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
FROM zip_scores_full
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
  name=map_input
  title = "Community Populations"
  tooltip={[
    {id: 'Community', fmt: 'id', showColumnName: false, valueClass: 'text-xl font-semibold'},
    {id: 'Population', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    ]}
/>

```sql housing_by_year
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2010 as year,
  "Foreclosures_2010" as foreclosures,
  "Sales_2010" as sales,
  "Mortgage_2010" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2011 as year,
  "Foreclosures_2011" as foreclosures,
   "Sales_2011" as sales,
  "Mortgage_2011" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2012 as year,
  "Foreclosures_2012" as foreclosures,
  "Sales_2012" as sales,
  "Mortgage_2012" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2013 as year,
  "Foreclosures_2013" as foreclosures,
  "Sales_2013" as sales,
  "Mortgage_2013" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2014 as year,
  "Foreclosures_2014" as foreclosures,
  "Sales_2014" as sales,
  "Mortgage_2014" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2015 as year,
  "Foreclosures_2015" as foreclosures,
  "Sales_2015" as sales,
  "Mortgage_2015" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2016 as year,
  "Foreclosures_2016" as foreclosures,
  "Sales_2016" as sales,
  "Mortgage_2016" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2017 as year,
  "Foreclosures_2017" as foreclosures,
  "Sales_2017" as sales,
  "Mortgage_2017" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2018 as year,
  "Foreclosures_2018" as foreclosures,
  "Sales_2018" as sales,
  "Mortgage_2018" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2019 as year,
  "Foreclosures_2019" as foreclosures,
  "Sales_2019" as sales,
  "Mortgage_2019" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2020 as year,
  "Foreclosures_2020" as foreclosures,
  "Sales_2020" as sales,
  "Mortgage_2020" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2021 as year,
  "Foreclosures_2021" as foreclosures,
  "Sales_2021" as sales,
  "Mortgage_2021" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2022 as year,
  "Foreclosures_2022" as foreclosures,
  "Sales_2022" as sales,
  "Mortgage_2022" as mortgages
from community_housing_stats
union all
select
  "Geography" as community,
  "CommunityNo" as CommunityNo,
  2023 as year,
  "Foreclosures_2023" as foreclosures,
  "Sales_2023" as sales,
  "Mortgage_2023" as mortgages
from community_housing_stats
```

## Community Housing Metrics over Time
<Dropdown name=Housing_Metric
title="Select a Category">
  <DropdownOption valueLabel= "Foreclosures" value= "foreclosures" />
  <DropdownOption valueLabel= "Sales" value= "sales" />
  <DropdownOption valueLabel= "Mortgages" value= "mortgages" />
</Dropdown>

<LineChart
  data={housing_by_year}
  x=year
  y={inputs.Housing_Metric.value}
  series=community
/>