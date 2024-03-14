create table if not exists `crescent-1`.`suppliers` (
  `supplier_id` int not null auto_increment,
  `supplier_name` varchar(255) not null,
  `contact_person` varchar(255) null,
  `phone_number` varchar(15) null,
  primary key (`supplier_id`));