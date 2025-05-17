---
title: Housing
---


```sql community_housing
select
  "CommunityNo" as CommunityNo,
  "Geography" as Community,
  "Total_Population" as Population,
  "population_below_poverty_level" as population_below_poverty_level,
  "Total_Households" as Total_Households
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
  title = "Communities of Chicago"
  tooltip={[
    {id: 'Community', fmt: 'id', showColumnName: false, valueClass: 'text-xl font-semibold'},
    {id: 'Population', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    {id: 'Total_Households', title: 'Total Households', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    {id: 'population_below_poverty_level', title: 'Population Below the Poverty Line', fmt: 'pct', fieldClass: 'text-[grey]', valueClass: 'text-gray-500'},
    ]}
/>

```sql cost_burden
select "CommunityNo" as CommunityNo, "Geography" as community, 'Owner-Occupied' as label, OWNER_OCCUPIED_COST_BURDENED as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
union all
select "CommunityNo" as CommunityNo, "Geography" as community, 'Renter-Occupied' as label, RENTER_OCCUPIED_COST_BURDENED as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
union all
select "CommunityNo" as CommunityNo, "Geography" as community, 'All' as label, ALL_COST_BURDENED as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
order by label
```

```sql tenure
select "CommunityNo" as CommunityNo, "Geography" as community,'Owner-Occupied' as label, OWNER_OCCUPIED as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
union all
select "CommunityNo" as CommunityNo, "Geography" as community, 'Renter-Occupied' as label, RENTER_OCCUPIED as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
order by label
```
```sql property_type
select "CommunityNo" as CommunityNo, "Geography" as community, 'Single Family' as label, SINGLE_FAMILY as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
union all
select "CommunityNo" as CommunityNo, "Geography" as community, 'Condominium' as label, CONDOMINIUM as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
union all
select  "CommunityNo" as CommunityNo, "Geography" as community,'Building with 2-4 Units' as label, BUILDING_2TO4 as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
union all
select "CommunityNo" as CommunityNo, "Geography" as community, 'Building with 5+ Units' as label, BUILDING_5PLUS as value from community_housing_stats where CommunityNo = '${inputs.map_input.CommunityNo}'
order by label
```

{#if inputs.map_input.CommunityNo === true}
  ### Select community above to see more details
{:else}
  ### {cost_burden[0].community}
  
{/if}

<Grid cols=3>
    <Group>

      <BarChart
      data={cost_burden}
      title='Cost Burdened'
      subtitle='Share of Households'
      x=label
      y=value
      labels=true
      xAxisLabels=false
      yGridlines=false
      yAxisLabels=false
      yMin=0
      yFmt=pct
      series=label
      />
    </Group>
    <Group>
      <BarChart
      data={tenure}
      title='Resident Tenure'
      subtitle='Share of Households'
      x=label
      y=value
      labels=true
      xAxisLabels=false
      yGridlines=false
      yAxisLabels=false
      yMin=0
      yFmt=pct
      series=label
      />
    </Group>
    <Group>
      <BarChart
      data={property_type}
      title='Household by Property Type'
      subtitle='Housing Units'
      x=label
      xAxisLabels=false
      y=value
      labels=true
      yGridlines=false
      yAxisLabels=false
      yMin=0
      yFmt=pct
      series=label
      />
    </Group>
</Grid>

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
<Dropdown name=Housing_Metric
title="Select a Category">
  <DropdownOption valueLabel= "Foreclosures" value= "foreclosures" />
  <DropdownOption valueLabel= "Sales" value= "sales" />
  <DropdownOption valueLabel= "Mortgages" value= "mortgages" />
</Dropdown>

<LineChart
  data={housing_by_year}
  title="Community Housing Metrics over Time"
  x=year
  y={inputs.Housing_Metric.value}
  series=community
/>