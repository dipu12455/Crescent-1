CREATE TABLE IF NOT EXISTS `crescent-1`.`HouseMaterials` (
  `house_id` INT NOT NULL,
  `supplier_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `how_many` INT,
  PRIMARY KEY (`house_id`, `supplier_id`, `material_id`));