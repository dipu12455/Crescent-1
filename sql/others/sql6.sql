select SUM(SupplierMaterials.unit_price * HouseMaterials.how_many) from HouseMaterials, SupplierMaterials
where SupplierMaterials.supplier_id = HouseMaterials.supplier_id and SupplierMaterials.material_id = HouseMaterials.material_id
and HouseMaterials.house_id = 28;