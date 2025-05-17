---
title: Chicago Community Insights Dashboard
---
This dashboard allows you to interact with the City of Chicago's data. The database visualized by this app includes housing, crime, and education data. It is the visualization piece for the project submitted in partial fulfillment of the requirements for the Master of Science in Data Science degree in the College of Aviation, Science, and Technology of Lewis University.

Full code can be found at the [ChicagoCommunities GitHub](https://github.com/hannahgleppert/ChicagoCommunities).

<Details title='About this data'>
  <Details title='Housing, Income, and Population'>
    Housing data was collected from the Institute of Housing Studies at DePaul University: 

	  [Property Sales Activity](https://www.housingstudies.org/data-portal/browse/?indicator=total-sales-activity&area=chicago-community-areas&property_type=0&view_as=view-table)

    [Mortgage Activity](https://www.housingstudies.org/data-portal/browse/?indicator=total-mortgage-activity&area=chicago-community-areas&property_type=0&view_as=view-table)

	  [Foreclosure Filing Activity](https://www.housingstudies.org/data-portal/browse/?indicator=total-foreclosure-activity&area=chicago-community-areas&property_type=0&view_as=view-table)

	  [Housing Stock Composition](ttps://www.housingstudies.org/data-portal/browse/?indicator=housing-units-composition&area=chicago-community-areas&view_as=view-table)

	  [Poverty Rate](https://www.housingstudies.org/data-portal/browse/?indicator=poverty-rate&area=chicago-community-areas&view_as=view-table)

	  [Resident Tenure](https://www.housingstudies.org/data-portal/browse/?indicator=resident-tenure&area=chicago-community-areas&view_as=view-table)

	  [Cost Burdened Households](https://www.housingstudies.org/data-portal/browse/?indicator=cost-burdened-households&area=chicago-community-areas&view_as=view-table)

	  [Population](https://www.housingstudies.org/data-portal/browse/?indicator=population-and-age&area=chicago-community-areas&view_as=view-table)

  </Details>
    

    <Details title='Crime'>
    Crime data was downloaded from the Chicago Data Portal:

    [Crimes - 2001 to Present](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data)

    </Details>
     <Details title='Education'>
     Education data was downloaded from the Chicago Data Portal:

     [Chicago Public Schools - School Profile Information SY2324](https://data.cityofchicago.org/Education/Chicago-Public-Schools-School-Profile-Information-/cu4u-b4d9/about_data)

     [Chicago Public Schools - School Progress Reports SY2324](https://data.cityofchicago.org/Education/Chicago-Public-Schools-School-Progress-Reports-SY2/2dn2-x66j/about_data)

    </Details>

 </Details>


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


