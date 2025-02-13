-- Create customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    user_id INT,
    customer_age INT,
    location VARCHAR(100),
    account_age_days INT
);

-- Create orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    transaction_id INT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Create products table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_category VARCHAR(100)
);

-- Create order_items table
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create indexes for performance optimization (optional)
CREATE INDEX idx_customer_id ON orders (customer_id);
CREATE INDEX idx_order_id ON order_items (order_id);
CREATE INDEX idx_product_id ON order_items (product_id);
