"""หน้าจอ Study Time Tracker"""

import streamlit as st

from data_store import load_records, save_record
from logic import classify_duration, validate_session

st.set_page_config(
    page_title="Study Time Tracker",
    page_icon=":material/menu_book:",
    layout="centered",
)

st.title("Study Time Tracker", icon=":material/menu_book:")
st.caption("ระบบบันทึกเวลาเรียนรู้")

with st.container(border=True):
    st.subheader("บันทึกเวลาเรียน")
    with st.form("study_session_form"):
        subject = st.text_input("ชื่อวิชา (Subject)", placeholder="เช่น วิทยาศาสตร์")
        minutes = st.text_input(
            "เวลาเรียน (Duration: นาที)",
            placeholder="กรอกจำนวนเต็ม 1–240",
        )
        submitted = st.form_submit_button(
            "Save",
            type="primary",
            icon=":material/save:",
            width="stretch",
        )

if submitted:
    is_valid, message = validate_session(subject, minutes)

    if not is_valid:
        st.error(message)
    else:
        duration = int(minutes.strip())
        record = {
            "subject": subject.strip(),
            "minutes": duration,
            "category": classify_duration(duration),
        }
        try:
            save_record(record)
        except (OSError, ValueError) as error:
            st.error(f"บันทึกข้อมูลไม่สำเร็จ: {error}")
        else:
            st.success("บันทึกข้อมูลเรียบร้อยแล้ว")

st.subheader("ประวัติการเรียน")
try:
    records = load_records()
except (OSError, ValueError) as error:
    st.error(f"อ่านประวัติการเรียนไม่สำเร็จ: {error}")
else:
    if records:
        st.table(list(reversed(records)))
    else:
        st.info("ยังไม่มีประวัติการเรียน เริ่มบันทึกวิชาแรกของคุณได้เลย")
