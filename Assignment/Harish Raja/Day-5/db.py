import ibm_db

hostname="764264db-9824-4b7c-82df-40d1b13897c2.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
uid="yzq20262"
pwd="Hx1pNmiwkW4C6xbY"
driver="{IBM DB2 ODBC DRIVER}"
db="bludb"
port="32536"
protocol="TCPIP"
cert="cert.crt"

dsn=(
     "DATABASE={0};"
     "HOSTNAME={1}"
     "PORT={2};"
     "UID={3};"
     "SECURITY=SSL;"
     "SSLServerCertificate={4};"
     "PWD={5};").format(db,hostname,port,uid,cert,pwd)

print(dsn)

try:
    db2=ibm_db.connect(dsn,"","")
    print("Successful")
except:
    print("Failure",ibm_db.conn_errormsg())
     