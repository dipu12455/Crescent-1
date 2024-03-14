create table if not exists `crescent-1`.`suppliermaterials` (
  `supplier_id` int not null,
  `material_id` int not null,
  `unit_price` decimal(10,2) not null,
  primary key (`supplier_id`, `material_id`));