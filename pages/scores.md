 ```sql zipScores
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, 

FROM zip_scores
WHERE ZipCode IS NOT NULL;
```
<Dropdown 
    data={zipScores} 
    name=category 
    value=category_name
    title="Select a Metric" 
    defaultValue="Rank"
/>







<AreaMap
   data={zipScores}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value={inputs.category.value}
   name=neighborhood_score_map
/>

