---
title: Crime
---
 
 ```sql violentCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "ViolentCrimes" AS "Violent Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={violentCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value="Violent Crimes since 2001"
   name=violent_crimes
/>

 ```sql drugCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "ViolentCrimes" AS "Drug Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={drugCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value="Drug Crimes since 2001"
   name=drug_crimes
/>

 ```sql propertyCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "PropertyCrimes" AS "Property Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={propertyCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value="Property Crimes since 2001"
   name=property_crimes
/>

 ```sql otherCrimes
SELECT LPAD(CAST("ZipCode" AS TEXT), 5, '0') AS ZIP, "Other" AS "Other Crimes since 2001"
FROM zip_scores
WHERE ZipCode IS NOT NULL;
```

<AreaMap
   data={otherCrimes}
   geoJsonUrl="/Cook_County_Zip_Code.geojson"
   geoId=zip
   areaCol=ZIP
   value="Other Crimes since 2001"
   name=other_crimes
/>