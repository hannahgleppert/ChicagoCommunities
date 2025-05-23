---
title: Education
---


##### School Explorer

{#if inputs.map_input.ZIP === true}
    # Chicago
{:else}
    # {inputs.map_input.ZIP}
    [See ZIP code deep dive &rarr;](./{inputs.map_input.ZIP})

{/if}

```sql schools
SELECT LPAD(CAST("Zip" AS TEXT), 5, '0') AS ZIP, COUNT(*) AS schools
FROM school_information
WHERE ZIP IS NOT NULL
GROUP BY ZIP
order by schools DESC
```
```sql schools_cat
SELECT 1 AS order_col, 'Pre-School' AS School_Type, COUNT(*) FILTER (WHERE Is_Pre_School = true) AS count FROM school_information WHERE (LPAD(CAST("Zip" AS TEXT), 5, '0') = '${inputs.map_input.ZIP}' OR '${inputs.map_input.ZIP}' = 'true') 
UNION ALL
SELECT 2, 'Elementary School', COUNT(*) FILTER (WHERE Is_Elementary_School = true) FROM school_information WHERE (LPAD(CAST("Zip" AS TEXT), 5, '0') = '${inputs.map_input.ZIP}' OR '${inputs.map_input.ZIP}' = 'true')
UNION ALL
SELECT 3, 'Middle School', COUNT(*) FILTER (WHERE Is_Middle_School = true) FROM school_information WHERE (LPAD(CAST("Zip" AS TEXT), 5, '0') = '${inputs.map_input.ZIP}' OR '${inputs.map_input.ZIP}' = 'true')
UNION ALL
SELECT 4, 'High School', COUNT(*) FILTER (WHERE Is_High_School = true) FROM school_information WHERE (LPAD(CAST("Zip" AS TEXT), 5, '0') = '${inputs.map_input.ZIP}' OR '${inputs.map_input.ZIP}' = 'true')
order by order_col
```

<Grid cols=2>
    <Group>


        <AreaMap
            data={schools}
            geoJsonUrl="/Cook_County_Zip_Code.geojson"
            geoId=zip
            areaCol=ZIP
            value=schools
            name=map_input
        />

    </Group>
    <Group>

    <BarChart
    data={schools_cat}
    x=order_col
    y=count
    labels=true
    series=School_Type
    seriesLabels=true
    yAxisTitle=true
    legend=true
    xAxisLabels=false
    xAxisLabelRotation=0
    chartAreaHeight=260
    seriesOrder = {['Pre-School', 'Elementary School', 'Middle School', 'High School']}
    />

    </Group>
</Grid>

```sql schools_zip
select LPAD(CAST("Zip" AS TEXT), 5, '0') AS ZIP, 'Pre-School' as School_Type, COUNT(*) FILTER (WHERE Is_Pre_School = true) AS count from school_information group by ZIP
union all
select LPAD(CAST("Zip" AS TEXT), 5, '0') AS ZIP, 'Elementary School', COUNT(*) FILTER (WHERE Is_Elementary_School = true) from school_information group by ZIP
union all
select LPAD(CAST("Zip" AS TEXT), 5, '0') AS ZIP, 'Middle School', COUNT(*) FILTER (WHERE Is_Middle_School = true) from school_information group by ZIP
union all
select LPAD(CAST("Zip" AS TEXT), 5, '0') AS ZIP, 'High School', COUNT(*) FILTER (WHERE Is_High_School = true) from school_information group by ZIP
order by ZIP
```


<BarChart
    data={schools_zip}
    x=ZIP
    y=count
    title="Chicago Schools"
    yGridlines=false
    yAxisLabels=false
    yAxisTitle=true
    swapXY=true
    legend
    seriesOrder = {['Pre-School', 'Elementary School', 'Middle School', 'High School']}
    series=School_Type
/>

## ZIP Code List

<DataTable data={schools} link=ZIP>
    <Column id=ZIP/>
    <Column id=schools contentType=colorscale/>
</DataTable>

