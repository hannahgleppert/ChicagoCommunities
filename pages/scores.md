 ```sql zipScores
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "Rank"
FROM neighborhood_scores
WHERE ZipCode IS NOT NULL;
```


<AreaMap
   data={zipScores}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value=Rank
   name=neighborhood_score_map
/>