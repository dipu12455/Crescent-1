SELECT SupplierMaterials.unit_price 
FROM HouseMaterials 
JOIN SupplierMaterials 
ON HouseMaterials.supplier_id = SupplierMaterials.supplier_id 
AND HouseMaterials.material_id = SupplierMaterials.material_id 
WHERE HouseMaterials.house_id = 28;

-- multiply the unit price by the quantity in the `how_many` column in HouseMaterials table
-- Path: sql/others/sql6.sql
SELECT SUM(SupplierMaterials.unit_price * HouseMaterials.how_many)
FROM HouseMaterials
JOIN SupplierMaterials
ON HouseMaterials.supplier_id = SupplierMaterials.supplier_id
AND HouseMaterials.material_id = SupplierMaterials.material_id
WHERE HouseMaterials.house_id = 28;

select SupplierMaterials.unit_price * HouseMaterials.how_many from HouseMaterials;
