import yaml
import psycopg2

def parseConnYAML(file = 'conn.yaml'):
    with open(file, "r") as stream:
        try:
            d = yaml.safe_load(stream)
            connInfo = d['postgres']
        except yaml.YAMLError as e:
            print(e)
    return connInfo

def createConnection(host,dbname,user,password):
    conn = psycopg2.connect("host={0} dbname={1} user={2} password={3}".format(host,dbname,user,password))
    return conn

def createCursor(conn):
    # Cursor object to create
    cur = conn.cursor()
    return cur

def execQuery(cur, query):
    """Executes SQL query on a cursor object

    Args:
        cur (cursor): cursor object for a database connection
        query (string): SQL query to execute

    Returns:
        out: Return value from query. None if no return expected.
    """
    out = None
    out = cur.execute(query)
    # Conditions to check out
    return out

def closeConnection(conn):
    conn.Close()
    return
