CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    price FLOAT,
    type VARCHAR(50)
);

INSERT INTO items (name, price, type) 
VALUES 
    ('Computer', 1998.0, 'Electronic devices'),
    ('Laptop', 999.0, 'Electronic devices'),
    ('Chicken', 6, 'Food'),
    ('Eggs', 1.99, 'Food');


