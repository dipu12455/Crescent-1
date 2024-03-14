alter table Sales
add constraint fk_house_id
foreign key (house_id)
references Houses(house_id);

alter table HouseMaterials
add constraint fk_house_id
foreign key (house_id)
references Houses(house_id),
add constraint fk_supplier_id
foreign key (supplier_id)
references Suppliers(supplier_id),
add constraint fk_material_id
foreign key (material_id)
references Materials(material_id);

alter table SupplierMaterials
add constraint fk_supplier_id
foreign key (supplier_id)
references Suppliers(supplier_id),
add constraint fk_material_id
foreign key (material_id)
references Materials(material_id);

