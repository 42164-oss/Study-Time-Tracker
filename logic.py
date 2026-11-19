"""ตรวจสอบข้อมูลการเรียนและจำแนกระยะเวลา"""


def validate_session(subject: str, minutes: str | int) -> tuple[bool, str]:
    """ตรวจสอบชื่อวิชาและเวลาเรียน แล้วคืนผลพร้อมข้อความภาษาไทย"""
    if not subject.strip():
        return False, "กรุณากรอกชื่อวิชา"

    if isinstance(minutes, bool):
        return False, "กรุณากรอกเวลาเป็นจำนวนเต็ม"

    if isinstance(minutes, int):
        duration = minutes
    elif isinstance(minutes, str) and minutes.strip().isdecimal():
        duration = int(minutes.strip())
    else:
        return False, "กรุณากรอกเวลาเป็นจำนวนเต็ม"

    if not 1 <= duration <= 240:
        return False, "เวลาเรียนต้องอยู่ระหว่าง 1–240 นาที"

    return True, "ข้อมูลถูกต้อง"


def classify_duration(minutes: int) -> str:
    """จำแนกระยะเวลาเรียนเป็น Short, Medium หรือ Long"""
    if minutes < 30:
        return "Short"
    if minutes < 60:
        return "Medium"
    return "Long"
