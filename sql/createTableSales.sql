CREATE TABLE IF NOT EXISTS `crescent-1`.`Sales` (
  `sale_id` INT NOT NULL AUTO_INCREMENT,
  `house_id` INT NOT NULL,
  `sale_date` DATETIME,
  `sale_price` DECIMAL(12,2),
  PRIMARY KEY (`sale_id`, `house_id`));