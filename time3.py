import streamlit as st
from datetime import datetime
from zhdate import ZhDate

# 嘗試匯入 zhdate，如果沒安裝就自動裝
try:
    from zhdate import ZhDate
except ImportError:
    print("偵測到尚未安裝 zhdate，正在安裝中...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "zhdate"])
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
st.title("掐指一算")

if st.button("開始科學預測"):
    now = datetime.now()
    lunar = ZhDate.from_datetime(now)
    chinese_hour = get_chinese_hour(now.hour)
    result = calculate_result(lunar.lunar_month, lunar.lunar_day, chinese_hour)

#目前隱藏不必要的資訊
    #st.write(f"**國曆**：{now.strftime('%Y-%m-%d %H:%M:%S')}")
    #st.write(f"**農曆**：{lunar.lunar_year}年{lunar.lunar_month}月{lunar.lunar_day}日 {chinese_hour}")
    st.write(f"**預測結果**：{result}")

   # 網頁下方說明文字
st.markdown("""
---

### 掐指一算說明

「掐指一算」是源自《易經》奇門遁甲體系的占卜方法，透過手指指節推算天干、地支、八卦等時空訊息，判斷吉兇。其核心為小六壬演算法，以「大安起正月，月上起日，日上起時」為推算邏輯，兼具「無事勿占，一事一卦」的原則。  

此方法將左手食指、中指、無名指分為六節，對應大安、留連、速喜、赤口、小吉、空亡六神，分別象徵五行、方位等要素。推算時從大安起正月，順時針定位月、日、時辰，結合占語得出結果[1-2]。操作分三步驟：定月份起點，推日辰落點，算時辰定位。  

其歷史可追溯至古代六壬術，屬傳統三式（奇門、太乙、六壬）之一。小六壬因簡單掌訣演算得名，宋代已有文獻記載，魯迅曾提及此法，印證其在民間術數的延續[1]。六壬體系中，小六壬與大六壬分別對應不同推演邏輯，共同構成傳統預測分支。
""")
