create table if not exists `crescent-1`.`housematerials` (
  `house_id` int not null,
  `supplier_id` int not null,
  `material_id` int not null,
  `how_many` int,
  primary key (`house_id`, `supplier_id`, `material_id`));