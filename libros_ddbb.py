import psycopg2

def connect():
    # Conectar a PostgreSQL
    conn = psycopg2.connect(
        dbname="biblioteca",
        user="postgres",
        password="1234",
        host="192.168.44.130",
        port="5433"
    )

def insertar_biblioteca(titulo, isbn, autor, paginas ,fecha):

    conn = connect()  # Conectar a la base de datos
    try:
        cursor = conn.cursor()  # Crear un cursor para ejecutar consultas SQL

        # Consulta SQL para insertar un nuevo árbol en la tabla 'Arboles'
        query = """
        INSERT INTO Libro (titulo, isbn, autor, paginas, fecha) 
        VALUES (%s, %s, %s, %s, %s)
    
        """

        # Ejecutar la consulta pasando los valores como parámetros
        cursor.execute(query, (id, titulo, isbn, autor, paginas, fecha))

        # Confirmar la transacción
        conn.commit()
        print("Libro registrado correctamente.")

    except psycopg2.Error as e:
        print(f"Error en la base de datos: {e}")

    finally:
        if conn:
            cursor.close()  # Cerrar el cursor
            conn.close()  # Cerrar la conexión a la base de datos

# Ejemplo de uso:
# insertar_arbol("Pino", "Perenne", 30, "2005-03-15")