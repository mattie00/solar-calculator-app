import os
import sys
import shutil
from pathlib import Path

from utils.db import Database


def setup_calculator_db():
    user_data_dir = Path(os.getenv("LOCALAPPDATA", ".")) / "SolarCalculator"
    user_data_dir.mkdir(parents=True, exist_ok=True)

    db_final_path = user_data_dir / "calculator.db"

    if getattr(sys, '_MEIPASS', False):
        resource_db_path = os.path.join(sys._MEIPASS, 'database', 'calculator.db')

        if not db_final_path.exists():
            shutil.copy2(resource_db_path, db_final_path)

    else:
        resource_db_path = os.path.join(os.path.dirname(__file__), 'database', 'calculator.db')

        if not db_final_path.exists():
            shutil.copy2(resource_db_path, db_final_path)

    calc_db = Database(str(db_final_path))
    calc_db.connect()

    calc_tables = [
        """
        CREATE TABLE IF NOT EXISTS modules (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            product_warranty TEXT,
            performance_warranty TEXT,
            power REAL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS inverters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            warranty TEXT,
            type TEXT,
            phases TEXT,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS warehouses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            warranty TEXT,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS security (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS support (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS installation_direction (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            direction TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS installation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS cable_ac (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS cable_dc (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS optimizers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS rafter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            type TEXT NOT NULL,
            price REAL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS promotions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            amount REAL
        );
        """,

        """
        CREATE TABLE IF NOT EXISTS calculations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            record_name TEXT,
            data TEXT,
            created_at TEXT
        );
        """

    ]
    calc_db.create_tables(calc_tables)
    return calc_db
