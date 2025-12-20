import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="منصة توجيه برو 2026", page_icon="🎓", layout="centered")

# 2. تنسيق CSS لضمان مظهر احترافي ومنع تداخل النصوص
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0e1117;
        color: white;
    }
    .main-title {
        font-size: 2.2rem;
        font-weight: 900;
        color: #4facfe;
        text-align: center;
        margin-bottom: 20px;
    }
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        border-right: 6px solid #4facfe;
        margin-bottom: 25px;
    }
    img {
        border-radius: 12px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الواجهة الأمامية (الصور تظهر فوراً)
st.markdown("<div class='main-title'>🚀 منصة توجيه برو 2026</div>", unsafe_allow_html=True)

# الصورة الرئيسية الكبيرة في الواجهة
st.image("https://images.unsplash.com/photo-1523050853064-db984a9617ae?q=80&w=1000", caption="مستقبلك يبدأ من هنا", use_container_width=True)

st.markdown("""
<div class='feature-card'>
    <h3>✨ لماذا تختار منصتنا؟</h3>
    <p>نحن نوفر لك تحليلاً دقيقاً بناءً على معدلات القبول التاريخية في المغرب، لنرشدك نحو الكلية التي تناسب طموحاتك.</p>
</div>
""", unsafe_allow_html=True)

# صور استعراضية في الواجهة الأمامية (قبل التحليل)
st.write("### 🏢 استكشف المؤسسات الكبرى:")
col_front1, col_front2 = st.columns(2)
with col_front1:
    st.image("https://images.unsplash.com/photo-1576091160550-2173dad99901?q=80&w=400", caption="كليات الطب والصيدلة")
with col_front2:
    st.image("https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?q=80&w=400", caption="مدارس الهندسة والتقنيات")

st.markdown("---")

# 4. إدخال بيانات الطالب
st.subheader("📝 ابدأ رحلتك التوجيهية الآن")
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الواتساب")

col1, col2 = st.columns(2)
with col1:
    math = st.number_input("الرياضيات", 0.0, 20.0, 14.0)
    lang = st.number_input("اللغات", 0.0, 20.0, 10.0)
with col2:
    physic = st.number_input("الفيزياء", 0.0, 20.0, 14.0)
    philo = st.number_input("الفلسفة", 0.0, 20.0, 10.0)

# 5. تحليل النتائج وعرضها بالصور
if st.button("🚀 عرض تقرير القبول"):
    if not name or not phone:
        st.error("⚠️ المرجو إدخال الاسم ورقم الهاتف أولاً")
    else:
        st.balloons()
        avg = (math + physic + lang + philo) / 4
        
        st.markdown(f"## 🎯 التقرير الخاص بالطالب: {name}")
        
        # قائمة المدارس المحددة
        schools = [
            {"n": "كليات الطب والصيدلة", "th": 16.0, "img": "https://images.unsplash.com/photo-1532187875605-2fe3d39148b3?q=80&w=500"},
            {"n": "المدارس الوطنية للعلوم التطبيقية (ENSA)", "th": 14.2, "img": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?q=80&w=500"},
            {"n": "المدارس الوطنية للتجارة والتسيير (ENCG)", "th": 13.5, "img": "https://images.unsplash.com/photo-1454165833767-027ffea9e77b?q=80&w=500"}
        ]
        
        for s in schools:
            diff = avg - s['th']
            # معادلة ذكية لحساب النسبة المئوية للقبول
            prob = min(99, 80 + (diff * 8)) if diff >= 0 else max(10, 50 + (diff * 15))
            color = "#00ff88" if prob >= 70 else "#ffcc00"
            
            with st.container():
                st.markdown(f"### 📍 {s['n']}")
                st.image(s['img'], use_container_width=True)
                st.markdown(f"<p style='font-size:1.2rem;'>احتمالية القبول بناءً على نقاطك: <b style='color:{color};'>{prob:.1f}%</b></p>", unsafe_allow_html=True)
                st.write("---")

st.markdown("<p style='text-align:center; opacity:0.6;'>تم التطوير بواسطة أنس المعزوزي © 2026</p>", unsafe_allow_html=True)
