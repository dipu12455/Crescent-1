CREATE TABLE IF NOT EXISTS `crescent-1`.`SupplierMaterials` (
  `supplier_id` INT NOT NULL,
  `material_id` INT NOT NULL,
  `unit_price` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`supplier_id`, `material_id`));