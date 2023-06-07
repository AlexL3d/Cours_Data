import mysql.connector

# Paramètres de connexion à la base de données
config = {
    'user': 'root',
    'port': '3308',
    'password': 'SINAY',
    'host': 'localhost',
    'raise_on_warnings': True
}

try:
    # Établir la connexion à la base de données
    conn = mysql.connector.connect(**config)

    if conn.is_connected():
        print('Connecté à la base de données MariaDB')

        # Exécuter une requête
        cursor = conn.cursor()
        cursor.execute('SELECT VERSION()')
        version = cursor.fetchone()[0]
        print(f'Version de MariaDB : {version}')

        # Fermer le curseur et la connexion
        cursor.close()
        conn.close()

except mysql.connector.Error as e:
    print(f'Erreur de connexion à la base de données : {e}')