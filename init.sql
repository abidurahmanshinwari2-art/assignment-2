CREATE TABLE IF NOT EXISTS registry (
    id INT PRIMARY KEY,
    registration VARCHAR(32) NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    title VARCHAR(120) NOT NULL
);

INSERT INTO registry (id, registration, full_name, title)
VALUES (1, 'SP22-BCS-108', 'Abidurahman shinwari', 'SP22-BCS-108 Registry')
ON DUPLICATE KEY UPDATE
    registration = VALUES(registration),
    full_name = VALUES(full_name),
    title = VALUES(title);

CREATE USER IF NOT EXISTS 'readonly108'@'%' IDENTIFIED BY 'ReadOnly108';
GRANT SELECT ON sp22bcs108.* TO 'readonly108'@'%';
FLUSH PRIVILEGES;
