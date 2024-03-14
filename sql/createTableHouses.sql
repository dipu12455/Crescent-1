CREATE TABLE IF NOT EXISTS `crescent-1`.`Houses` (
  `house_id` INT NOT NULL AUTO_INCREMENT,
  `address` VARCHAR(255) NOT NULL,
  `city` VARCHAR(45) NULL,
  `state` VARCHAR(45) NULL,
  `zipcode` VARCHAR(45) NULL,
  `construction_date` VARCHAR(255) NULL,
  PRIMARY KEY (`house_id`));