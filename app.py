import streamlit as st
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Tawjih Pro 2026", page_icon="🎓", layout="centered")

# 2. حل مشكلة الكتابة في الوسط (CSS Fixed)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    /* منع تداخل النصوص وتصحيح الاتجاه */
    html, body, [class*="css"] {
        font-family: 'Cairo', sans-serif;
        direction: rtl;
        text-align: right;
    }
    
    /* منع ظهور النصوص فوق بعضها في المنتصف */
    .stMarkdown div {
        line-height: 1.6;
    }

    /* تحسين عرض الصور لتناسب الهاتف */
    .stImage img {
        max-width: 100%;
        border-radius: 15px;
    }

    /* ستايل البطاقات */
    .school-card {
        background: white; 
        padding: 15px; 
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-right: 5px solid #1e3a8a;
        margin-top: 10px;
        color: #1e3a8a;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. المحتوى الرئيسي (بدون شريط جانبي لتفادي المشاكل على الهاتف)
st.markdown("<h1 style='text-align: center; color: #1e3a8a;'>🎓 منصة توجيه برو 2026</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>مستشارك الذكي لاختيار أفضل الكليات في المغرب</p>", unsafe_allow_html=True)

# الصورة الرئيسية
st.image("https://images.pexels.com/photos/267885/pexels-photo-267885.jpeg?auto=compress&cs=tinysrgb&w=800", use_container_width=True)

st.markdown("---")

# 4. إدخال البيانات بتنسيق بسيط
st.subheader("📝 سجل بياناتك للتحليل")
name = st.text_input("الاسم الكامل")
phone = st.text_input("رقم الواتساب")
shouba = st.selectbox("شعبة البكالوريا", ["SVT", "PC", "Math", "Eco", "Lettres"])

st.write("### 📊 أدخل نقطك الرئيسية:")
col1, col2 = st.columns(2) # تقسيم المواد لعمودين فقط لتناسب الهاتف
with col1:
    math = st.number_input("الرياضيات", 0.0, 20.0, 10.0)
    lang = st.number_input("اللغات", 0.0, 20.0, 10.0)
with col2:
    physic = st.number_input("الفيزياء/العلوم", 0.0, 20.0, 10.0)
    philo = st.number_input("الفلسفة", 0.0, 20.0, 10.0)

# 5. زر التحليل والنتائج
if st.button("🚀 ابدأ تحليل مستقبلي"):
    if not name or not phone:
        st.error("⚠️ يرجى إدخال البيانات المطلوبة!")
    else:
        st.balloons()
        avg = (math + physic + lang + philo) / 4
        
        # تحليل البروفايل
        scores = {"علمي": (math + physic)/2, "تواصل": lang, "أدبي": philo}
        profile = max(scores, key=scores.get)
        
        st.markdown(f"### 🎯 النتيجة الخاصة بك: {name}")
        
        if profile == "علمي":
            st.success("✅ بروفايلك هندسي/علمي بامتياز!")
            st.image("https://images.pexels.com/photos/3825573/pexels-photo-3825573.jpeg?auto=compress&cs=tinysrgb&w=600")
        elif profile == "تواصل":
            st.info("✅ بروفايلك تواصل وتدبير!")
            st.image("https://images.pexels.com/photos/3184328/pexels-photo-3184328.jpeg?auto=compress&cs=tinysrgb&w=600")
        else:
            st.info("✅ بروفايلك فكري وأدبي!")
            st.image("https://images.pexels.com/photos/159711/books-bookstore-book-reading-159711.jpeg?auto=compress&cs=tinysrgb&w=600")

        st.markdown(f"""
        <div class='school-card'>
            <h4>معدلك العام التقريبي: {avg:.2f}</h4>
            <p>بناءً على هذا المعدل، لديك فرص جيدة في المدارس الوطنية.</p>
        </div>
        """, unsafe_allow_html=True)

# 6. قسم المساعد الذكي (تم وضعه في الأسفل بدلاً من الجانب لتفادي الخلل)
st.markdown("---")
st.subheader("🤖 المساعد الذكي")
user_msg = st.text_input("اسألني أي شيء (مثلاً: متى يبدأ التسجيل؟)")
if user_msg:
    replies = ["أغلب المباريات تبدأ في يونيو.", "نعم، نقطتك تؤهلك لعدة خيارات!", "التسجيل عبر Tawjihi.ma."]
    st.info(f"💬 رد المساعد: {random.choice(replies)}")

st.markdown("<br><p style='text-align: center; color: gray;'>تم التطوير بواسطة Anas Selmazouzy © 2025</p>", unsafe_allow_html=True)
