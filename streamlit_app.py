# streamlit_app.py
import streamlit as st
import sympy as sp
import pandas as pd
import math
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solusi SPNL - Metode Bisection", layout="centered")
st.title("🎈 Solusi Pesamaan Non-Linear (Metode Bisection)")
st.write("Masukkan fungsi f(x) dan interval [a,b] dimana f(a) dan f(b) Berbeda tanda.")

# Input
f_input = st.text_input("Masukkan fungsi f(x) (contoh: x**3 - 4*x + 1):", value="x**3 - 4*x + 1")
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Batas bawah a", value=0.0, format="%.6f")
with col2:
    b = st.number_input("Batas atas b", value=1.0, format="%.6f")
tol = st.number_input("Toleransi (epsilon)", value=1e-6, format="%.10f")
max_iter = st.number_input("Max iterasi", min_value=1, value=50, step=1)
