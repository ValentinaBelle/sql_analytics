
# weekly_report.py
import sqlite3
import pandas as pd

# Load SQL results → Excel 
conn = sqlite3.connect('payments.db')
df = pd.read_sql_query("""
    SELECT gateway, COUNT(*) fails 
    FROM transactions WHERE status='fail' 
    GROUP BY gateway ORDER BY fails DESC LIMIT 5
""", conn)

df.to_excel('gateway_fails_weekly.xlsx', index=False)
print("✅ Report generated!")
