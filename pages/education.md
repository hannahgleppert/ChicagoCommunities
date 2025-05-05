---
title: Education
---

```sql num_elem
select CAST(Zip AS TEXT) AS Zip, 'Pre-School' as School_Type, count(Is_Pre_School) as count from school_information group by Zip
union all
select CAST(Zip AS TEXT) AS Zip, 'Elementary School', count(Is_Elementary_School) from school_information group by Zip
union all
select CAST(Zip AS TEXT) AS Zip, 'Middle School', count(Is_Middle_School) from school_information group by Zip
union all
select CAST(Zip AS TEXT) AS Zip, 'High School', count(Is_High_School) from school_information group by Zip
```
<BarChart
    data={num_elem}
    x=Zip
    y=count
    title="Counts of Schools by ZIP Code"
    labels
    yGridlines=false
    yAxisLabels=false
    yAxisTitle=true
    swapXY=true
    legend
    series=School_Type
/>