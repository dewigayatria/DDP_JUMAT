import streamlit as st

st.title("halaman dashboard")

def total():
    total_nabung = sum(t['jumlah'] for t in st.session_state['total_semua'] if t ['type'] == 'menabung')

    return total_nabung

total_semua = st.session_state['total_semua']
total_nabung = total()

st.metric("total menabung anda", f"Rp.{total_nabung:,}")