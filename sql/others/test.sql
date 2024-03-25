DECLARE @year INT
DECLARE @currentHouse_id INT
DECLARE @supplier_id INT
DECLARE @material_id INT
DECLARE @amount INT
DECLARE @unit_price DECIMAL(10, 2)
DECLARE @construction_cost DECIMAL(10, 2)

DECLARE @sales TABLE (
    sale_date DATE,
    house_id INT
)

DECLARE @houseMaterials TABLE (
    house_id INT,
    supplier_id INT,
    material_id INT,
    amount INT
)

DECLARE @supplierMaterials TABLE (
    material_id INT,
    supplier_id INT,
    unit_price DECIMAL(10, 2)
)

-- Populate @sales table with sales data
INSERT INTO @sales (sale_date, house_id)
SELECT sale_date, house_id
FROM Sales

-- Iterate over years
SET @year = 2014
WHILE @year <= 2024
BEGIN
    -- Iterate over sales for the current year
    INSERT INTO @houseMaterials (house_id, supplier_id, material_id, amount)
    SELECT house_id, supplier_id, material_id, amount
    FROM HouseMaterials
    WHERE house_id IN (
        SELECT house_id
        FROM @sales
        WHERE YEAR(sale_date) = @year
    )

    -- Calculate construction cost for each house in the current year
    DECLARE houseMaterials_cursor CURSOR FOR
    SELECT house_id, supplier_id, material_id, amount
    FROM @houseMaterials

    OPEN houseMaterials_cursor
    FETCH NEXT FROM houseMaterials_cursor INTO @currentHouse_id, @supplier_id, @material_id, @amount

    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Find unit price of the material from SupplierMaterials table
        SELECT @unit_price = unit_price
        FROM SupplierMaterials
        WHERE material_id = @material_id AND supplier_id = @supplier_id

        -- Calculate construction cost
        SET @construction_cost = @unit_price * @amount

        -- Print construction cost
        PRINT 'Construction cost for house ' + CAST(@currentHouse_id AS VARCHAR) + ' in year ' + CAST(@year AS VARCHAR) + ' is ' + CAST(@construction_cost AS VARCHAR)

        FETCH NEXT FROM houseMaterials_cursor INTO @currentHouse_id, @supplier_id, @material_id, @amount
    END

    CLOSE houseMaterials_cursor
    DEALLOCATE houseMaterials_cursor

    SET @year = @year + 1
END
