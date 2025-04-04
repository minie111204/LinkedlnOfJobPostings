import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URI", 
        "mssql+pyodbc://@ZRMR/DATH-KTDL?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes"
    )