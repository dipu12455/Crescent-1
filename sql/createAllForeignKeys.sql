alter table Sales
add constraint fkSales_house_id
foreign key (house_id)
references Houses(house_id);

alter table HouseMaterials
add constraint fkHouseMaterials_house_id
foreign key (house_id)
references Houses(house_id),
add constraint fkHouseMaterials_supplier_id
foreign key (supplier_id)
references Suppliers(supplier_id),
add constraint fkHouseMaterials_material_id
foreign key (material_id)
references Materials(material_id);

alter table SupplierMaterials
add constraint fkSupplierMaterials_supplier_id
foreign key (supplier_id)
references Suppliers(supplier_id),
add constraint fkSupplierMaterials_material_id
foreign key (material_id)
references Materials(material_id);

