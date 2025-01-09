import streamlit as st

st.title("halaman menabung")

with st.form("menabung"):
    nama = st.text_input("nama")
    jumlah = st.number_input("jumlah (RP.)", min_value=0)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("waktu")
    button = st.form_submit_button(label="menabung")

    if button and jumlah >= 50000:
        st.session_state['total_semua'].append({
            "type" : "menabung",
            "jumlah" : jumlah
        })
        st.success("Anda berhasil menabung")
    else:
        st.error("kamu gagal menabung, nominal kurang dari 50000")