from asammdf import MDF
import pandas as pd
import matplotlib.pyplot as plt

dbc_filename = "11-bit-OBD2-v4.0.dbc"
mf4_filename = r"00000001.MF4"
mdf = MDF(mf4_filename)
# dalla documentazione
# The valid bus (il secondo elem della tupla) is an integer specifying for
# which bus channel the database can be applied; 0 means any bus channel.
db_files = {"CAN": [(dbc_filename, 0)]}
# interpreta i dati usando il file dbc
mdf_scaled = mdf.extract_bus_logging(db_files)
df = mdf_scaled.to_dataframe()
print(df.columns)
# estrai la velocità
column_name = "S01PID0C_EngineRPM"
if column_name in df.columns:
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df[column_name], label=column_name)
    plt.xlabel("Time (s)")
    plt.ylabel("Value")
    plt.title(f"Plot of {column_name}")
    plt.legend()
    plt.grid()
    plt.show()
else:
    print(f"Column '{column_name}' not found in the DataFrame.")


