use crescent1;

-- drop foreign key constraints before dropping the tables

alter table Sales
drop constraint fkSales_house_id;

alter table HouseMaterials
drop constraint fkHouseMaterials_house_id,
drop constraint fkHouseMaterials_supplier_id,
drop constraint fkHouseMaterials_material_id;

alter table SupplierMaterials
drop constraint fkSupplierMaterials_supplier_id,
drop constraint fkSupplierMaterials_material_id;

-- drop the tables if they exist
drop table if exists HouseMaterials;
drop table if exists Houses;
drop table if exists Materials;
drop table if exists Sales;
drop table if exists SupplierMaterials;
drop table if exists Suppliers;