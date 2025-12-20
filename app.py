import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Tawjih Pro AI", page_icon="🎯", layout="centered")

# CSS لمنع التداخل وتجميل العرض
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; direction: rtl; text-align: right; background-color: #0f172a; color: white; }
    .report-card { background: rgba(255, 255, 255, 0.05); border-radius: 15px; padding: 20px; border-right: 5px solid #3b82f6; margin-bottom: 15px; }
    .probability-high { color: #10b981; font-weight: bold; }
    .probability-medium { color: #f59e0b; font-weight: bold; }
    .stButton>button { background: #2563eb; color: white; border-radius: 10px; width: 100%; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 محرك التحليل الذكي 2026")

# مدخلات الطالب
with st.container():
    name = st.text_input("الاسم الكامل")
    col1, col2 = st.columns(2)
    with col1:
        math = st.number_input("الرياضيات", 0.0, 20.0, 14.0)
        physic = st.number_input("الفيزياء", 0.0, 20.0, 14.0)
    with col2:
        lang = st.number_input("اللغات", 0.0, 20.0, 14.0)
        philo = st.number_input("الفلسفة", 0.0, 20.0, 14.0)

if st.button("تحليل فرص القبول الآن"):
    st.markdown(f"### 📋 التقرير التفصيلي للطالب: {name}")
    
    avg = (math + physic + lang + philo) / 4
    
    # مصفوفة المدارس والتحليل
    schools = [
        {"name": "كلية الطب والصيدلة (FMP)", "threshold": 16.20, "city": "الرباط/البيضاء"},
        {"name": "مدرسة المهندسين (ENSA)", "threshold": 14.30, "city": "القنيطرة/طنجة"},
        {"name": "مدرسة التجارة (ENCG)", "threshold": 13.50, "city": "سطات/أكادير"},
        {"name": "المدرسة العليا للتكنولوجيا (EST)", "threshold": 12.00, "city": "سلا/مكناس"}
    ]

    for school in schools:
        # حساب النسبة المئوية للقبول
        diff = avg - school['threshold']
        if diff >= 0:
            prob = min(98, 85 + (diff * 5))
            status = "احتمال قبول مرتفع"
            color_class = "probability-high"
        else:
            prob = max(5, 50 + (diff * 15))
            status = "تحتاج مجهود إضافي"
            color_class = "probability-medium"

        st.markdown(f"""
        <div class="report-card">
            <h4 style="margin:0;">📍 {school['name']}</h4>
            <p style="font-size:0.9rem; opacity:0.8;">المدن: {school['city']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <span>نسبة القبول المتوقعة: <span class="{color_class}">{prob:.1f}%</span></span>
                <span class="{color_class}">{status}</span>
            </div>
            <progress value="{prob}" max="100" style="width:100%;"></progress>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align:center; margin-top:50px;'>منصة توجيه برو - النسخة الاحترافية 1.5</p>", unsafe_allow_html=True)
