import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)


#CREATING
def category_creator():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE category(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name TINYTEXT NOT NULL
        )
        """
    )
    conn.commit()

def item_creator():
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE item(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TINYTEXT NOT NULL,
        item_count INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        FOREIGN KEY (category_id) REFERENCES category_name(id)
        )
        """
    )
    conn.commit()

# category_creator()
# item_creator()

# "DROP TABLE category"
# "DROP TABLE item"


# ADD
def add_category(category_name):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO category(category_name) VALUES("{category_name}")
        """
    )
    conn.commit()

def add_item(item_name, item_count, category_id):
    cur = conn.cursor()
    cur.execute(
        f"""
        INSERT INTO item(item_name, item_count, category_id) VALUES("{item_name}", "{item_count}", "{category_id}")
        """
    )
    conn.commit()


#GET
def get_category():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id, category_name FROM category
        ORDER BY category_name ASC
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data

def get_item():
    cur = conn.cursor()
    cur.execute(
        f"""
        SELECT id, item_name, item_count, category_id FROM item
        ORDER BY item_name ASC
        """
    )
    conn.commit()
    data = cur.fetchall()
    return data


#REMOVE
def remove_category(id):
    for i in range(len(id)):
        cur = conn.cursor()
        cur.execute(
            f"""
            DELETE FROM category
            WHERE id = "{id[i]}"
            """
        )
        conn.commit()

def remove_item(id):
    for i in range(len(id)):
        cur = conn.cursor()
        cur.execute(
            f"""
            DELETE FROM item
            WHERE id = "{id[i]}"
            """
        )
        conn.commit()


#UPDATE
def update_category(id, category_name):
    cur = conn.cursor()
    cur.execute(
        f"""
        UPDATE category
        SET category_name = "{category_name}"
        WHERE id = {id};
        """
    )
    conn.commit()

def update_item(id, item_name, item_count, category_id):
    cur = conn.cursor()
    cur.execute(
        f"""
        UPDATE item
        SET item_name = "{item_name}", item_count = "{item_count}" category_id = "{category_id}"
        WHERE id = {id};
        """
    )
    conn.commit()