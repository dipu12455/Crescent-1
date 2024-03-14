create table if not exists `crescent-1`.`materials` (
  `material_id` int not null auto_increment,
  `material_name` varchar(255) not null,
  primary key (`material_id`));