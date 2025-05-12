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
        tooltipType=hover
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

### School Demographics

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
order by Ethnicity
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

### School Performance

```sql school_perform
SELECT *
FROM school_performance
WHERE Long_Name = '${inputs.school_name.value}'
```
<DataTable data={school_perform}>
    <Column id=Long_Name title="Name"/>
    <Column id=Primary_Category title="School Category"/>
    <Column id=School_Type title="School Type"/>
    <Column id=Culture_Climate_Rating title="Culture Climate Rating"/>
    <Column id=Creative_School_Certification title="Creative School Certification"/>
    <Column id=School_Survey_Student_Response_Rate_Pct title="Student Response Rate (%)" fmt=id/>
    <Column id=School_Survey_Teacher_Response_Rate_Pct title="Teacher Response Rate (%)" fmt=id/>
    <Column id=School_Survey_Involved_Families title="Involved Families"/>
    <Column id=School_Survey_Supportive_Environment title="Supportive Environment"/>
    <Column id=School_Survey_Ambitious_Instruction title="Ambitious Instruction"/>
    <Column id=School_Survey_Effective_Leaders title="Effective Leaders"/>
    <Column id=School_Survey_Collaborative_Teachers title="Collaborative Teachers"/>
    <Column id=School_Survey_Safety title="Safety"/>
    <Column id=Student_Attendance_Year_1_Pct title="Student Attendance 2021 (%)" fmt=id/>
    <Column id=Student_Attendance_Year_2_Pct title="Student Attendance 2022 (%)" fmt=id/>
    <Column id=Teacher_Attendance_Year_1_Pct title="Teacher Attendance 2021 (%)" fmt=id/>
    <Column id=Teacher_Attendance_Year_2_Pct title="Teacher Attendance 2022 (%)" fmt=id/>
    <Column id=Mobility_Rate_Pct title="Mobility Rate (%)" fmt=id/>
    <Column id=Chronic_Truancy_Pct title="Chronic Truancy (%)" fmt=id/>
    <Column id=One_Year_Dropout_Rate_Year_1_Pct title="One Year Dropout Rate 2021 (%)" fmt=id/>
    <Column id=One_Year_Dropout_Rate_Year_2_Pct title="One Year Dropout Rate 2022 (%)" fmt=id/>
    <Column id=Freshmen_On_Track_School_Pct_Year_1 title="Freshmen On Track School 2021 (%)" fmt=id/>
    <Column id=Freshmen_On_Track_School_Pct_Year_ title="Freshmen On Track School 2022 (%)" fmt=id/>
    <Column id=Graduation_4_Year_School_Pct_Year_1 title="Graduation 4 Year School 2021 (%)" fmt=id/>
    <Column id=Graduation_4_Year_School_Pct_Year_2 title="Graduation 4 Year School 2022 (%)" fmt=id/>
    <Column id=Graduation_5_Year_School_Pct_Year_1 title="Graduation 5 Year School 2021 (%)" fmt=id/>
    <Column id=Graduation_5_Year_School_Pct_Year_2 title="Graduation 5 Year School 2022 (%)" fmt=id/>
    <Column id=College_Enrollment_School_Pct_Year_1 title="College Enrollment School 2021 (%)" fmt=id/>
    <Column id=College_Enrollment_School_Pct_Year_2 title="College Enrollment School 2022 (%)" fmt=id/>
    <Column id=College_Persistence_School_Pct_Year_1 title="College Persistence School 2021 (%)" fmt=id/>
    <Column id=College_Persistence_School_Pct_Year_2 title="College Persistence School 2022 (%)" fmt=id/>
    <Column id=SAT_Grade_11_Score_School_Avg title="SAT Grade 11 Score School Average" fmt=id/>
    <Column id=Attainment_PSAT_Grade_9_School_Pct title="Attainment PSAT Grade 9 School (%)" fmt=id/>
    <Column id=Attainment_PSAT_Grade_10_School_Pct title="Attainment PSAT Grade 10 School (%)" fmt=id/>
    <Column id=Attainment_SAT_Grade_11_School_Pct title="Attainment SAT Grade 11 School (%)" fmt=id/>
    <Column id=Attainment_All_Grades_School_Pct title="Attainment All Grades School (%)" fmt=id/>
</DataTable>
