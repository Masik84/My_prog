import sqlite3

db_path = 'modules/Bonus_db.db'


def DBTables_creation_if_new():
    conn = sqlite3.connect(db_path)

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS Customers (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                SoldTo INTEGER not null UNIQUE ON CONFLICT IGNORE,
                                SoldTo_name_en VARCHAR (200),
                                SoldTo_name_ru VARCHAR (200));
                                ''')

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS DeliveryAddress (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                ShipTo INTEGER not null UNIQUE ON CONFLICT IGNORE,
                                SoldTo_name_en VARCHAR (200),
                                SoldTo_name_ru VARCHAR (200));
                                ''')

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS Materials (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Material INTEGER not null UNIQUE ON CONFLICT IGNORE,
                                Material_Name VARCHAR (100),
                                LPC_Code VARCHAR (30),
                                UoM VARCHAR (5),
                                Net_Weight DECIMAL,
                                Volume DECIMAL ,
                                Pack_Type VARCHAR (10),
                                Status VARCHAR (2),
                                Prod_LoB VARCHAR (5),
                                Excl VARCHAR (5),
                                Sal_prod_id INTEGER ,
                                Prod_name_id INTEGER ,
                                Gr_id INTEGER );
                                ''')

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS SalableProduct (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Sal_Prod_Code INTEGER not null UNIQUE ON CONFLICT IGNORE,
                                Sal_Prod_Name VARCHAR (100));
                                ''')

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS Family (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Prod_Name_Code INTEGER not null UNIQUE ON CONFLICT IGNORE,
                                Family_Name VARCHAR (100));
                                ''')

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS MatGroup (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Group_Code INTEGER not null UNIQUE ON CONFLICT IGNORE,
                                Group_Name VARCHAR (100));
                                ''')

    conn.execute('''
                                CREATE TABLE IF NOT EXISTS MatStatus (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                Code VARCHAR (2) not null UNIQUE ON CONFLICT IGNORE,
                                Status_Name VARCHAR (30));
                                ''')

    conn.commit()

    conn.execute('''
                                INSERT INTO MatStatus (Code, Status_Name)
                                VALUES 
                                        ('01', 'underDevelop'),
                                        ('02', 'active'),
                                        ('03', 'for withdrawal'),
                                        ('04', 'inactive');
                                ''')
    
    conn.commit()
    conn.close()