import streamlit as st
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Tawjih Pro 2026", page_icon="🎓", layout="wide")

# 2. ستايل CSS محسن لضمان ظهور الصور وتناسق الألوان
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stImage > img { border-radius: 20px; box-shadow: 0 4px 15px rgba(0,0,0,0.2); }
    .school-card {
        background: white; padding: 20px; border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        border-right: 8px solid #1e3a8a; margin-bottom: 20px;
        color: #1e3a8a;
    }
    .stButton>button {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        color: white; border-radius: 25px; border: none;
        width: 100%; height: 3.5rem; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. العنوان الرئيسي وصورة الهيدر
st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🎓 منصة توجيه برو 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>مستشارك الذكي لاختيار أفضل الكليات والمعاهد في المغرب</p>", unsafe_allow_html=True)

# صورة تعبيرية (رابط موثوق)
st.image("https://images.pexels.com/photos/267885/pexels-photo-267885.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1", use_container_width=True)

# 4. إدخال البيانات
with st.expander("📝 سجل بياناتك للبدء في التحليل", expanded=True):
    col_name, col_phone = st.columns(2)
    with col_name:
        name = st.text_input("الاسم الكامل")
    with col_phone:
        phone = st.text_input("رقم الواتساب")
    shouba = st.selectbox("شعبة البكالوريا", ["SVT", "PC", "Math", "Eco", "Lettres"])

# 5. تحليل نقط المواد
st.write("### 📊 أدخل نقطك في المواد الرئيسية:")
c1, c2, c3, c4 = st.columns(4)
with c1: math = st.number_input("الرياضيات", 0.0, 20.0, 10.0)
with c2: physic = st.number_input("الفيزياء/العلوم", 0.0, 20.0, 10.0)
with c3: lang = st.number_input("اللغات", 0.0, 20.0, 10.0)
with c4: philo = st.number_input("الفلسفة", 0.0, 20.0, 10.0)

# 6. زر التحليل والنتائج
if st.button("🚀 ابدأ تحليل مستقبلي"):
    if not name or not phone:
        st.error("⚠️ يرجى إدخال اسمك ورقم هاتفك أولاً!")
    else:
        st.balloons()
        avg = (math + physic + lang + philo) / 4
        
        st.markdown(f"## 🎯 النتيجة الخاصة بك: {name}")
        
        # تحليل المسار بناءً على أعلى نقطة
        scores = {"علمي": (math + physic)/2, "تواصل": lang, "أدبي": philo}
        profile = max(scores, key=scores.get)
        
        if profile == "علمي":
            st.success("✅ بروفايلك هندسي/علمي بامتياز!")
            st.image("https://images.pexels.com/photos/3825573/pexels-photo-3825573.jpeg?auto=compress&cs=tinysrgb&w=600", width=500)
            rec = "ننصحك بمدارس المهندسين (ENSA) أو كليات العلوم والتقنيات (FST)."
        elif profile == "تواصل":
            st.info("✅ بروفايلك تواصل وتدبير!")
            st.image("https://images.pexels.com/photos/3184328/pexels-photo-3184328.jpeg?auto=compress&cs=tinysrgb&w=600", width=500)
            rec = "ننصحك بالمدارس الوطنية للتجارة والتسيير (ENCG) أو الصحافة (ISIC)."
        else:
            st.info("✅ بروفايلك فكري وأدبي!")
            st.image("https://images.pexels.com/photos/159711/books-bookstore-book-reading-159711.jpeg?auto=compress&cs=tinysrgb&w=600", width=500)
            rec = "ننصحك بكليات الآداب، الحقوق، أو المعاهد العليا للفنون."

        st.markdown(f"<div class='school-card'><h3>معدلك العام التقريبي: {avg:.2f}</h3><p>{rec}</p></div>", unsafe_allow_html=True)

# 7. الشات بوت البسيط (Side)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🤖 المساعد الذكي</h2>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712035.png", width=100)
    user_msg = st.text_input("لديك سؤال؟ اسألني هنا:")
    if user_msg:
        replies = ["أغلب المباريات تفتح في شهر يونيو.", "نعم، نقطتك تؤهلك لعدة خيارات، استمر في العمل!", "التسجيل عبر منصة Tawjihi.ma غالباً."]
        st.write(f"💬: {random.choice(replies)}")
    st.markdown("---")
    st.write("📞 **للمساعدة الخاصة:**")
    st.write("تواصل معنا عبر الواتساب مباشرة.")

st.markdown("<hr><p style='text-align: center;'>تم التطوير بواسطة Anas Selmazouzy © 2025</p>", unsafe_allow_html=True)
