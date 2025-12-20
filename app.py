import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(page_title="Tawjih Pro AI 2026", page_icon="🎓", layout="centered")

# 2. ستايل CSS لضبط الصور والنصوص (منع التداخل)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700;900&display=swap');
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
        background-color: #0f172a;
        color: white;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #60a5fa;
        text-align: center;
        margin-bottom: 10px;
    }
    .image-container {
        border-radius: 20px;
        overflow: hidden;
        margin-bottom: 20px;
        border: 2px solid #3b82f6;
    }
    .feature-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 20px;
        border-right: 5px solid #3b82f6;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. الواجهة الأمامية (الصور التي تظهر فور الدخول)
st.markdown("<div class='main-title'>منصة توجيه برو 2026</div>", unsafe_allow_html=True)

# صورة رئيسية جذابة في الأعلى
st.image("https://images.unsplash.com/photo-1523050853064-db984a9617ae?w=1000&q=80", use_container_width=True)

st.markdown("""
<div class='feature-box'>
    <h3>🌟 لماذا نحن؟</h3>
    <p>نستخدم أحدث خوارزميات الذكاء الاصطناعي لتحليل نقاطك وتوجيهك نحو الكلية المناسبة لمستقبلك.</p>
</div>
""", unsafe_allow_html=True)

# صور استعراضية للمجالات (تظهر في الواجهة)
st.write("### 📚 استكشف آفاقك الدراسية:")
col_img1, col_img2 = st.columns(2)
with col_img1:
    st.image("https://images.unsplash.com/photo-1576091160550-2173dad99901?w=400&q=60", caption="الطب والصيدلة")
with col_img2:
    st.image("https://images.unsplash.com/photo-1581092580497-e0d23cbdf1dc?w=400&q=60", caption="الهندسة والابتكار")

st.markdown("---")

# 4. منطقة إدخال البيانات
st.subheader("📝 ابدأ التحليل الآن")
name = st.text_input("اسمك الكامل")
phone = st.text_input("رقم الواتساب")

col1, col2 = st.columns(2)
with col1:
    math = st.number_input("الرياضيات", 0.0, 20.0, 14.0)
    lang = st.number_input("اللغات", 0.0, 20.0, 14.0)
with col2:
    physic = st.number_input("الفيزياء", 0.0, 20.0, 14.0)
    philo = st.number_input("الفلسفة", 0.0, 20.0, 14.0)

# 5. زر النتائج
if st.button("🚀 عرض تقرير القبول التفصيلي"):
    if not name or not phone:
        st.error("⚠️ يرجى ملء البيانات أولاً")
    else:
        st.balloons()
        avg = (math + physic + lang + philo) / 4
        
        # مصفوفة المدارس مع الصور (تظهر عند النتيجة أيضاً)
        schools = [
            {"n": "كلية الطب", "th": 16.2, "img": "https://images.pexels.com/photos/263402/pexels-photo-263402.jpeg?auto=compress&cs=tinysrgb&w=400"},
            {"n": "مدرسة الهندسة", "th": 14.5, "img": "https://images.pexels.com/photos/3184418/pexels-photo-3184418.jpeg?auto=compress&cs=tinysrgb&w=400"}
        ]
        
        st.markdown(f"## 🎯 النتيجة لـ {name}")
        for s in schools:
            diff = avg - s['th']
            prob = min(99, 85 + (diff * 5)) if diff >= 0 else max(10, 50 + (diff * 15))
            
            st.markdown(f"### 📍 {s['n']}")
            st.image(s['img'], use_container_width=True)
            st.info(f"نسبة القبول المتوقعة بناءً على التحليل: {prob:.1f}%")

st.markdown("<p style='text-align:center; margin-top:30px; opacity:0.6;'>جميع الحقوق محفوظة - أنس المعزوزي 2026</p>", unsafe_allow_html=True)
