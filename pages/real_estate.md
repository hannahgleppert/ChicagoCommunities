
---
title: Real Estate
---
```sql num_elem
select Zip, count(Is_Elementary_School) as elem
from school_information
group by Zip
order by elem desc;
```
<BarChart
    data={num_elem}
    x=Zip
    y=elem
    title="Elementary School Counts"
    labels
    yGridlines=false
    yAxisLabels=false
    yAxisTitle=false
    y2AxisLabels=false
    y2Gridlines=false
    y2SeriesType=line
    y2AxisTitle=false
    legend
/>