create table if not exists `crescent-1`.`houses` (
  `house_id` int not null auto_increment,
  `address` varchar(255) not null,
  `city` varchar(45) null,
  `state` varchar(45) null,
  `zipcode` varchar(45) null,
  `construction_date` varchar(255) null,
  primary key (`house_id`));