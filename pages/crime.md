---
title: Crime
---
 
 


```sql crimes
SELECT LPAD(CAST("zip_code" AS TEXT), 5, '0') AS ZIP, COUNT(*) AS crimes
FROM crime_data
WHERE ZIP IS NOT NULL
GROUP BY ZIP
order by crimes DESC
```

<AreaMap
   data={crimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value=crimes
   name=map_input
        />

```sql crime_locations
SELECT LPAD(CAST("zip_code" AS TEXT), 5, '0') AS ZIP, *,
FROM crime_data
WHERE ZIP = '${inputs.map_input.ZIP}'
```
```sql crime_type_counts
SELECT 
  "Primary Type",
  COUNT(*) AS count
FROM crime_data
WHERE LPAD(CAST(zip_code AS TEXT), 5, '0') = '${inputs.map_input.ZIP}'
GROUP BY "Primary Type"
```

{#if inputs.map_input.ZIP === true}
    # Chicago
{:else}
    # {inputs.map_input.ZIP}

{/if}

<Grid cols=2>
    <Group>


        <PointMap
        title="Crime Locations"
        data={crime_locations}
        lat='Latitude'
        long='Longitude'
        startingZoom=12
        name=my_point_map
        value='Arrest'        
        tooltipType=hover
        tooltip={[
            {id: 'Primary Type', showColumnName: false, valueClass: 'font-bold text-lg'},
            {id: 'Date', fmt: 'longdate'},
            {id: 'Description', showColumnName: true, valueClass: 'text-gray-500'},
        ]}
    />

    </Group>
    <Group>

    <BarChart
    data={crime_type_counts}
    title = "Count of Primary Types"
    x='Primary Type'
    y='count'
    labels=true
    seriesLabels=true
    yAxisTitle=true
    legend=true
    series= 'Primary Type'
    xAxisLabels=false
    xAxisLabelRotation=0
    chartAreaHeight=260
/>

    </Group>
</Grid>