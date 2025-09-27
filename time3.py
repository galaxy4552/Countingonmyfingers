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

其歷史可追溯至古代六壬術，屬傳統三式（奇門、太乙、六壬）之一。小六壬因簡單掌訣演算得名，宋代已有文獻記載，魯迅曾提及此法，印證其在民間術數的延續。六壬體系中，小六壬與大六壬分別對應不同推演邏輯，共同構成傳統預測分支。

---
### 傳統占語
            
大安：身不動時，五行屬木，顏色青色，方位東方，臨青龍，凡謀事主一、五、七。有靜止、心安、吉祥之意義。
            
留連：卒未歸時，五行屬水，顏色黑色，方位北方，臨玄武，凡謀事主二、八、十。有暗昧不明、延遲、糾纏、拖延、漫長之意義。
            
速喜：人即至時，五行屬火，顏色紅色，方位南方，臨朱雀，凡謀事主三、六、九。有快速、喜慶、吉利之意義。指時機已到。
            
赤口：官事兇時，五行屬金，顏色白色，方位西方，臨白虎，凡謀事主四、七、十。有不吉、驚恐、兇險、口舌是非之意義。
            
小吉：人來喜時，五行屬水，臨六合，凡謀事主一、五、七。有和合、吉利之意義。
            
空亡：音信稀時，五行屬土，顏色黃色，方位中央，臨勾陳，凡謀事主三、六、九。有不吉、無結果、憂慮之意義。

---           
### 解說
            
大安大安事事昌，求財在坤方，失物去不遠，宅舍保安康
行人身未動，病者主無妨，將軍回田野，仔細更推詳
            
留連留連事難成，求謀日未明，官事凡宜緩，去者未回程
失物南方見，急討方心稱，更須防口舌，人口且平平
            
速喜速喜喜來臨，求財向南行，失物申未午，逢人路上尋
官事有福德，病者無禍侵，田宅六畜吉，行人有信音
            
赤口赤口主口舌，官非切宜防，失物速討，行人有驚慌
六畜多作怪，病者出西方，更須防咀咒，誠恐染瘟皇
            
小吉小吉最吉昌，路上好商量，陰人來報喜，失物在坤方
行人即便至，交關甚是強，凡事皆和合，病者叩窮蒼
            
空亡空亡事不祥，陰人多乖張，求財無利益，行人有災殃
失物尋不見，官事有刑傷，病人逢暗鬼，解禳保安康

---            
### 注意事項

1、遇事即刻卦，無事勿佔，凡事只佔一次，再佔不驗。
            
2、同樣一件事，也可以以臨時起卦，如上個事件，也可以按在接到朋友之約時的具體時間起卦。但同一個事件，只能算一次，例如按約會時算了，就不能再按約會的時間算了。
            
3.任何占卜都不是絕對準的，大的方向對就算準了。一般來說，平時生活中能算對個總事件的8成。如被偷了，算出了能否找到罪犯、人數、方向、破案時間，但沒算對追回來的金額，這也算是成功了。
            
4.冥冥中藏有玄機，所以對於六壬等掐指一算不能心中大不敬，否則不妙。                       

""")