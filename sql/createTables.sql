/* create the Suppliers table */
create table if not exists `crescent1`.`Suppliers` (
  `supplier_id` int not null auto_increment,
  `supplier_name` varchar(255) not null,
  `contact_person` varchar(255) null,
  `phone_number` varchar(15) null,
  primary key (`supplier_id`));
  
  /* create the Materials table */
  create table if not exists `crescent1`.`Materials` (
  `material_id` int not null auto_increment,
  `material_name` varchar(255) not null,
  primary key (`material_id`));
  
  /* create the Houses table */
  create table if not exists `crescent1`.`Houses` (
  `house_id` int not null,
  `address` varchar(255) not null,
  `city` varchar(45) null,
  `state` varchar(45) null,
  `zipcode` varchar(45) null,
  `construction_date` varchar(255) null,
  primary key (`house_id`));
  
  /* create the Sales table */
  create table if not exists `crescent1`.`Sales` (
  `sale_id` int not null auto_increment,
  `house_id` int not null,
  `sale_date` datetime,
  `sale_price` decimal(12,2),
  primary key (`sale_id`, `house_id`));
  
  /* create the SupplierMaterials table */
  create table if not exists `crescent1`.`SupplierMaterials` (
  `supplier_id` int not null,
  `material_id` int not null,
  `unit_price` decimal(10,2) not null,
  primary key (`supplier_id`, `material_id`));
  
  /* create the HouseMaterials table */
  create table if not exists `crescent1`.`HouseMaterials` (
  `house_id` int not null,
  `supplier_id` int not null,
  `material_id` int not null,
  `how_many` int,
  primary key (`house_id`, `supplier_id`, `material_id`));
  