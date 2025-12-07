# streamlit_app.py
import streamlit as st
import sympy as sp
import pandas as pd
import math
import matplotlib.pyplot as plt

st.title("🎈 Solusi Pesamaan Non-Linear (Metode Bisection)")
st.write(
    "Masukkan fungsi f(x) dan interval[a,b] dimana f(a) dan f(b) Berbeda tanda.)."
)
