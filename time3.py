import streamlit as st
from datetime import datetime
from zhdate import ZhDate

# 六個結果
results = ["大安", "流連", "速喜", "赤口", "小吉", "空亡"]

# 農曆時辰表（子=1 丑=2 ... 亥=12）
chinese_hours = [
    ("子時", 1), ("丑時", 2), ("寅時", 3), ("卯時", 4),
    ("辰時", 5), ("巳時", 6), ("午時", 7), ("未時", 8),
    ("申時", 9), ("酉時", 10), ("戌時", 11), ("亥時", 12)
]

def get_chinese_hour(hour: int) -> str:
    if 23 <= hour or hour < 1: return "子時"
    elif 1 <= hour < 3: return "丑時"
    elif 3 <= hour < 5: return "寅時"
    elif 5 <= hour < 7: return "卯時"
    elif 7 <= hour < 9: return "辰時"
    elif 9 <= hour < 11: return "巳時"
    elif 11 <= hour < 13: return "午時"
    elif 13 <= hour < 15: return "未時"
    elif 15 <= hour < 17: return "申時"
    elif 17 <= hour < 19: return "酉時"
    elif 19 <= hour < 21: return "戌時"
    elif 21 <= hour < 23: return "亥時"

def hour_to_number(hour_name: str) -> int:
    for name, num in chinese_hours:
        if name == hour_name:
            return num
    return 1

def calculate_result(lunar_month, lunar_day, chinese_hour):
    index = (lunar_month - 1) % 6
    index = (index + (lunar_day - 1) % 6) % 6
    hour_num = hour_to_number(chinese_hour)
    index = (index + (hour_num - 1) % 6) % 6
    return results[index]

# Streamlit 網頁 UI
st.title("掐指一算 🧧")

if st.button("開始算卦"):
    now = datetime.now()
    lunar = ZhDate.from_datetime(now)
    chinese_hour = get_chinese_hour(now.hour)
    result = calculate_result(lunar.lunar_month, lunar.lunar_day, chinese_hour)

    st.write(f"**國曆**：{now.strftime('%Y-%m-%d %H:%M:%S')}")
    st.write(f"**農曆**：{lunar.lunar_year}年{lunar.lunar_month}月{lunar.lunar_day}日 {chinese_hour}")
    st.write(f"**今日卦象**：{result}")
