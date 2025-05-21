import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Use your MySQL host
            user="root",  # Use your MySQL username
            password="",  # Use your MySQL password
            database="users"  # Use your database name
        )
        if connection.is_connected():
            return connection
    except Error as e:
        return False

def validate_user(username, password, role):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            table = "buyers" if role == "buyer" else "sellers"
            query = f"SELECT id FROM {table} WHERE username = %s AND password = %s"
            values = (username, password)
            cursor.execute(query, values)
            result = cursor.fetchone()

            cursor.close()
            connection.close()

            if result:
                return result[0]
            else:
                return None

    except Error as e:
        return None

def register_user(username, password, role):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            table = "buyers" if role == "buyer" else "sellers"

            check_query = f"SELECT * FROM {table} WHERE username = %s"
            cursor.execute(check_query, (username,))
            if cursor.fetchone():
                cursor.close()
                connection.close()
                return False

            insert_query = f"INSERT INTO {table} (username, password) VALUES (%s, %s)"
            cursor.execute(insert_query, (username, password))
            connection.commit()

            cursor.close()
            connection.close()
            return True

    except Error as e:
        return False


def add_item(seller_id, name, quantity, price, category):
    try:
        if quantity <= 0:
            return False
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            query = """
                INSERT INTO products (seller_id, name, quantity, price, category)
                VALUES (%s, %s, %s, %s, %s)
            """
            values = (seller_id, name, quantity, price, category)
            cursor.execute(query, values)
            connection.commit()

            cursor.close()
            connection.close()
            return True
    except Error as e:
        return False

def remove_item(seller_id, product_id, quantity_to_remove):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            query_select = """
                SELECT quantity FROM products WHERE id = %s AND seller_id = %s
            """
            cursor.execute(query_select, (product_id, seller_id))
            result = cursor.fetchone()

            if result:
                current_quantity = result[0]

                if quantity_to_remove >= current_quantity:
                    query_delete = """
                        DELETE FROM products WHERE id = %s AND seller_id = %s
                    """
                    cursor.execute(query_delete, (product_id, seller_id))
                else:
                    query_update = """
                        UPDATE products SET quantity = quantity - %s WHERE id = %s AND seller_id = %s
                    """
                    cursor.execute(query_update, (quantity_to_remove, product_id, seller_id))

                connection.commit()
                cursor.close()
                connection.close()
                return True
            else:
                cursor.close()
                connection.close()
                return False

    except Error as e:
        return False

def get_filtered_products(category=None, search_term=None):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            query = "SELECT id, name, description, price, category FROM products WHERE quantity > 0"
            values = []

            if category and category.lower() != "all":
                query += " AND category = %s"
                values.append(category)

            if search_term:
                query += " AND name LIKE %s"
                values.append(f"%{search_term}%")

            cursor.execute(query, tuple(values))
            results = cursor.fetchall()

            cursor.close()
            connection.close()

            return results
    except Error as e:
        return []

def add_to_cart(buyer_id, product_id, quantity):
    if quantity <= 0:
        return False  # Invalid quantity

    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # First, check the product's available quantity
            cursor.execute("SELECT quantity FROM products WHERE id = %s", (product_id,))
            result = cursor.fetchone()

            if not result:
                cursor.close()
                connection.close()
                return False  # Product not found

            available_quantity = result[0]

            if quantity > available_quantity:
                cursor.close()
                connection.close()
                return False  # Not enough stock

            # Check if the product already exists in the cart
            cursor.execute(
                "SELECT quantity FROM cart WHERE buyer_id = %s AND product_id = %s",
                (buyer_id, product_id)
            )
            existing = cursor.fetchone()

            if existing:
                # Update existing quantity
                new_quantity = existing[0] + quantity
                if new_quantity > available_quantity:
                    cursor.close()
                    connection.close()
                    return False  # Exceeds stock

                cursor.execute(
                    "UPDATE cart SET quantity = %s WHERE buyer_id = %s AND product_id = %s",
                    (new_quantity, buyer_id, product_id)
                )
            else:
                # Insert new item
                cursor.execute(
                    "INSERT INTO cart (buyer_id, product_id, quantity) VALUES (%s, %s, %s)",
                    (buyer_id, product_id, quantity)
                )

            connection.commit()
            cursor.close()
            connection.close()
            return True

    except Error as e:
        return False

def get_cart_items(buyer_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            query = """
                SELECT 
                    p.product_id, p.name, p.price, c.quantity, (p.price * c.quantity) AS total_price
                FROM 
                    cart c
                JOIN 
                    products p ON c.product_id = p.product_id
                WHERE 
                    c.buyer_id = %s
            """
            cursor.execute(query, (buyer_id,))
            results = cursor.fetchall()

            cursor.close()
            connection.close()

            return results  # Each item: (product_id, name, price, quantity, total_price)

    except Error as e:
        return []

def checkout_cart(buyer_id):
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()

            # 1. Get all cart items for the buyer
            fetch_cart = """
                SELECT product_id, quantity 
                FROM cart 
                WHERE buyer_id = %s
            """
            cursor.execute(fetch_cart, (buyer_id,))
            cart_items = cursor.fetchall()  # [(product_id, quantity), ...]

            for product_id, cart_quantity in cart_items:
                cursor.execute("SELECT quantity FROM products WHERE product_id = %s", (product_id,))
                product = cursor.fetchone()
                if product is None:
                    continue

                current_quantity = product[0]
                new_quantity = current_quantity - cart_quantity

                if new_quantity <= 0:
                    cursor.execute("DELETE FROM products WHERE product_id = %s", (product_id,))
                else:
                    cursor.execute("UPDATE products SET quantity = %s WHERE product_id = %s", (new_quantity, product_id))


            cursor.execute("DELETE FROM cart WHERE buyer_id = %s", (buyer_id,))

            connection.commit()
            cursor.close()
            connection.close()
            return True

    except Error as e:
        print(f"Checkout Error: {e}")
        return False
