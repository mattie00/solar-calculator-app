# 🌞 Solar Calculator

**Solar Calculator** is an early-stage desktop application designed for photovoltaic companies, used for calculating installation costs and forecasting annual electricity expenses. This version is no longer actively used but remains fully functional, allowing precise cost calculations for photovoltaic installations and generating PDF reports.

---

## 📌 Key Features

✅ Photovoltaic installation cost calculator, including modules, inverters, optimizers, and other components.  
✅ Support for different investor types (private individuals, companies) with appropriate VAT rates.  
✅ Annual electricity cost forecasting based on input parameters.  
✅ Calculation history with preview and export to PDF files.  
✅ User-friendly interface built with **CustomTkinter**.  
✅ Export of calculation results to **JSON** and **PDF** files.  
✅ Database configuration and parameter adjustment options.  

---

## 🛠️ Technologies Used

This project utilizes the following technologies and libraries:

- **Python** – Core programming language.
- **CustomTkinter** – For creating a modern and dynamic graphical user interface.
- **SQLite** – Embedded database for storing calculation history.
- **ReportLab** – Used for generating PDF reports from calculation data.
- **PyInstaller** – For packaging the application into an executable (.exe) file for Windows.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```sh
https://github.com/mattie00/solar-calculator-app.git
```

### 2️⃣ Install dependencies

Make sure you have **Python 3.10+** installed.

```sh
pip install -r requirements.txt
```

### 3️⃣ Run the application

```sh
python main.py
```

---

## 🛆 Building an .exe File (Windows)

If you want to create an **.exe** file, run:

```sh
python -m PyInstaller --onefile --windowed --name "SolarCalculator" --add-data "database\calculator.db;database" main.py
```

The executable file will be available in the `dist/` folder.

---

## 🗂️ Project Structure

```
solar-calculator/
│── app/
│   ├── calculator/            # Main photovoltaic installation calculator
│   ├── additional_calculator/ # Electricity cost forecast calculator
│   ├── history/               # Calculation history module
│   ├── settings/              # Application settings module
│── database/                  # SQLite database and JSON files
│── utils/                     # Helper functions
│── main.py                    # Main application launcher
│── requirements.txt           # Dependencies list
│── README.md                  # Project documentation
```

---


## 💜 License

This project is licensed under the [MIT License](LICENSE).

---

**🔗 Repository Link:** [https://github.com/mattie00/solar-calculator-app.git](https://github.com/mattie00/solar-calculator-app.git)

