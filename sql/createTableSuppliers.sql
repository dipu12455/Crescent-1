CREATE TABLE IF NOT EXISTS `crescent-1`.`Suppliers` (
  `supplier_id` INT NOT NULL AUTO_INCREMENT,
  `supplier_name` VARCHAR(255) NOT NULL,
  `contact_person` VARCHAR(255) NULL,
  `phone_number` VARCHAR(15) NULL,
  PRIMARY KEY (`supplier_id`));