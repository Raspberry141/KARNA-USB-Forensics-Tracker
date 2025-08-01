import streamlit as st
import os

st.title("🎯 KARNA - USB Forensics Tracker")

if st.button("Show USB History"):
    result = os.popen("reg query HKLM\SYSTEM\CurrentControlSet\Enum\USBSTOR /s").read()
    st.text_area("USB History", result, height=500)