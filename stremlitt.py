import streamlit as st
import pandas as pd
import numpy as np


import streamlit as st

# Initialize connection.
conn = st.connection("postgresql", type="sql")

# Perform query.
df = conn.query('SELECT * FROM actualizacion_cityland.floridablanca.lc_terreno lt ', ttl="10m")

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")
