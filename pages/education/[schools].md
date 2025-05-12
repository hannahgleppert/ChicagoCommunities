# {params.schools}

```sql school_locations
SELECT *,
  CASE Primary_Category
    WHEN 'Early Childhood' THEN 1
    WHEN 'ES' THEN 2
    WHEN 'MS' THEN 3
    WHEN 'HS' THEN 4
    ELSE 0
  END AS Primary_Category_Value
FROM school_information
WHERE ZIP = '${params.schools}'
```

<PointMap
        title="School Locations"
        data={school_locations}
        lat='School_Latitude'
        long='School_Longitude'
        startingZoom=12
        name=my_point_map
        value=Primary_Category_Value        
        tooltipType=click
        tooltip={[
            {id: 'Long_Name', showColumnName: false, valueClass: 'font-bold text-lg'},
            {id: 'Primary_Category'},
            {id: 'Grades_Offered_All', showColumnName: true},
        ]}
    />

<Dropdown 
    data={school_locations} 
    name=school_name
    value=Long_Name
    title="Select a School" 
    defaultValue=""
/>

```sql schools_demographics
SELECT 'African American' AS Ethnicity, Student_Count_Black AS count FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Hispanic', Student_Count_Hispanic FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'White', Student_Count_White FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Asian', Student_Count_Asian FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Native American', Student_Count_Native_American FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Other Ethnicity', Student_Count_Other_Ethnicity FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Asian Pacific Islander', Student_Count_Asian_Pacific_Islander FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Multi-Ethnicity', Student_Count_Multi FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Hawaiian Pacific Islander', Student_Count_Hawaiian_Pacific_Islander FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
UNION ALL
SELECT 'Ethnicity Not Available', Student_Count_Ethnicity_Not_Available FROM school_information WHERE Long_Name = '${inputs.school_name.value}'
```

    <BarChart
    data={schools_demographics}
    title = '{inputs.school_name.value}'
    x=Ethnicity
    y=count
    labels=true
    series = Ethnicity
    yAxisTitle=true
    legend=true
    xAxisLabels=false
    xAxisLabelRotation=0
    chartAreaHeight=280
    />