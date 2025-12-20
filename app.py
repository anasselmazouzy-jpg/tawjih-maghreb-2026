import streamlit as st
import datetime
import random

# 1. إعدادات الصفحة والجماليات المتقدمة
st.set_page_config(page_title="توجيه برو 2026 | المستشار الذكي", page_icon="🤖", layout="wide")

# تصميم CSS احترافي مع تأثيرات الشات بوت
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; direction: rtl; }
    .stApp { background-color: #f4f7f9; }
    
    /* ستايل البطاقات */
    .school-card {
        background: white; padding: 20px; border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border-right: 10px solid #1e3a8a; margin-bottom: 25px;
    }
    
    /* تصميم الشات بوت */
    .chat-box {
        position: fixed; bottom: 20px; left: 20px;
        width: 300px; background: white; border-radius: 15px;
        box-shadow: 0 5px 25px rgba(0,0,0,0.2);
        z-index: 1000; border: 1px solid #1e3a8a;
    }
    .chat-header { background: #1e3a8a; color: white; padding: 10px; border-radius: 15px 15px 0 0; text-align: center; }
    
    /* أنيميشن الأزرار */
    .stButton>button {
        background: linear-gradient(90deg, #1e3a8a, #3b82f6);
        color: white; border-radius: 30px; border: none;
        padding: 15px 30px; font-weight: bold; transition: 0.5s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 10px 20px rgba(59, 130, 246, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# 2. الهيدر والصور الملهمة
st.markdown("<h1 style='text-align: center; color: #1e3a8a; font-size: 3rem;'>مستقبلك يبدأ من هنا 🎓</h1>", unsafe_allow_html=True)
st.image("https://images.unsplash.com/photo-1523050335392-9af560c12bb5?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", use_container_width=True)

# 3. إدخال بيانات الطالب
with st.container():
    col_a, col_b, col_c = st.columns([2, 2, 1])
    with col_a:
        name = st.text_input("👤 الاسم الكامل")
    with col_b:
        phone = st.text_input("📱 رقم الواتساب (للتوصل بدليل المدارس PDF)")
    with col_c:
        shouba = st.selectbox("📚 الشعبة", ["SVT", "PC", "Math", "Eco"])

st.markdown("---")

# 4. نظام تحليل المواد المتقدم
st.write("### 📊 أدخل نقاطك في المواد الأساسية")
c1, c2, c3, c4 = st.columns(4)
with c1: math = st.number_input("الرياضيات", 0.0, 20.0, 10.0)
with c2: physic = st.number_input("الفيزياء/العلوم", 0.0, 20.0, 10.0)
with c3: lang = st.number_input("اللغة الإنجليزية/الفرنسية", 0.0, 20.0, 10.0)
with c4: philo = st.number_input("الفلسفة/العربية", 0.0, 20.0, 10.0)

# 5. منطق التحليل الذكي
if st.button("تحليل المسار الدراسي 🚀"):
    if not name or not phone:
        st.warning("⚠️ نرجو إدخال بياناتك أولاً لنتمكن من تحليل ملفك.")
    else:
        st.balloons()
        avg = (math + physic + lang + philo) / 4
        
        # تحديد البروفايل
        scores = {"العلمي": (math + physic)/2, "اللغوي": lang, "الأدبي": philo}
        profile = max(scores, key=scores.get)
        
        st.markdown(f"## 🏆 النتيجة لـ {name}:")
        
        if profile == "العلمي":
            st.success("🌟 **بروفايل تقني/هندسي:** لديك مهارات تحليلية قوية.")
            img_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800"
            advice = "ننصحك بالتركيز على مدارس المهندسين (ENSA/ENSAM) أو كليات الطب."
        elif profile == "اللغوي":
            st.info("🌟 **بروفايل تواصل/عالمي:** لديك قدرة رائعة على تعلم اللغات.")
            img_url = "https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800"
            advice = "خيارك الأفضل هو الصحافة (ISIC)، التجارة (ENCG) أو العلاقات الدولية."
        else:
            st.info("🌟 **بروفايل فكري/تحليلي:** أنت بارع في التفكير النقدي.")
            img_url = "https://images.unsplash.com/photo-1505664194779-8beaceb93744?w=800"
            advice = "ننصحك بالعلوم السياسية، الحقوق، أو التدبير الإداري."

        col_res1, col_res2 = st.columns(2)
        with col_res1:
            st.image(img_url, caption="المجال الأنسب لشخصيتك", use_container_width=True)
        with col_res2:
            st.markdown(f"""
            <div class='school-card'>
                <h3>تحليل المعدل: {avg:.2f}</h3>
                <p>{advice}</p>
                <hr>
                <p>✅ <b>فرص القبول:</b> تتراوح بين 70% و 90% حسب الـ Seuil.</p>
            </div>
            """, unsafe_allow_html=True)

# 6. الشات بوت التفاعلي (Sidebar Chat)
with st.sidebar:
    st.markdown("<div class='chat-header'>🤖 مساعدك الذكي</div>", unsafe_allow_html=True)
    st.write("مرحباً بك! أنا هنا للإجابة على تساؤلاتك.")
    user_q = st.text_input("اسألني أي شيء عن المدارس:")
    if user_q:
        responses = [
            "سؤال ممتاز! أغلب المباريات تبدأ في شهر 6.",
            "التسجيل غالباً يكون عبر منصة Tawjihi.ma، سأعلمك فور بدئها.",
            "لا تقلق بشأن المعدل، هناك دائماً بدائل رائعة مثل EST و BTS.",
            "ركز الآن على الوطني، والمعدل هو من سيفتح لك الأبواب."
        ]
        st.chat_message("assistant").write(random.choice(responses))
    
    st.markdown("---")
    st.write("📢 **آخر الأخبار:**")
    st.caption("• تحديث عتبات الانتقاء (Seuils) لعام 2026 قريباً.")
    st.caption("• فتح باب الترشيح للأقسام التحضيرية في أبريل.")

# 7. التذييل
st.markdown("<br><hr><p style='text-align: center; color: #7f8c8d;'>جميع الحقوق محفوظة منصة توجيه برو © 2026</p>", unsafe_allow_html=True)
