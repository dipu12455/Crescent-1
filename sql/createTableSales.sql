create table if not exists `crescent-1`.`sales` (
  `sale_id` int not null auto_increment,
  `house_id` int not null,
  `sale_date` datetime,
  `sale_price` decimal(12,2),
  primary key (`sale_id`, `house_id`));