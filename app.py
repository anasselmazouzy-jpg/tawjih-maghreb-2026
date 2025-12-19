import streamlit as st
import datetime
import random

# 1. إعدادات الصفحة
st.set_page_config(page_title="Tawjih Pro 2026", page_icon="🚀", layout="wide")

# 2. ستايل CSS متقدم
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(90deg, #1e3a8a, #3b82f6); color: white; height: 3.5rem; font-size: 1.2rem; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); margin-bottom: 20px; border-right: 6px solid #1e3a8a; }
    .seuil-badge { background: #e0e7ff; color: #1e3a8a; padding: 5px 15px; border-radius: 50px; font-weight: bold; }
    .countdown-box { background: #1e3a8a; color: white; padding: 20px; border-radius: 15px; text-align: center; margin-bottom: 30px; }
    </style>
    """, unsafe_allow_html=True)

# 3. العداد التنازلي لبكالوريا 2026
today = datetime.date.today()
exam_date = datetime.date(2026, 6, 10) # تاريخ تقديري
days_left = (exam_date - today).days

st.markdown(f"""
    <div class='countdown-box'>
        <h2>⏳ متبقي على بكالوريا 2026</h2>
        <h1 style='font-size: 3rem;'>{days_left} يوم</h1>
        <p>استغل كل دقيقة، حلمك يستحق!</p>
    </div>
    """, unsafe_allow_html=True)

# 4. قسم "نصيحة اليوم"
tips = [
    "النوم المبكر يساعد على ترسيخ المعلومات بنسبة 30% أكثر.",
    "ابدأ بالمواد الصعبة في الصباح الباكر عندما يكون تركيزك في أعلى مستوياته.",
    "قم بتلخيص الدروس على شكل خرائط ذهنية ليسهل تذكرها.",
    "اشرب الماء بكثرة، فالدماغ يحتاج للترطيب ليعمل بكفاءة."
]
st.info(f"💡 **نصيحة اليوم:** {random.choice(tips)}")

# 5. واجهة البيانات
st.write("### 🔍 أدخل بياناتك لتحليل مستقبلك")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("الاسم الكامل")
        shouba = st.selectbox("شعبتك:", ["SVT", "PC", "Math", "Eco", "Lettres"])
    with col2:
        phone = st.text_input("رقم الواتساب")
        note = st.slider("معدلك الحالي/المتوقع:", 10.0, 20.0, 14.0)

# 6. تحليل النتائج
if st.button("إظهار خارطة الطريق الخاصة بي 🚀"):
    if not name or not phone:
        st.error("الرجاء إدخال اسمك ورقم هاتفك لحفظ ملفك التوجيهي.")
    else:
        st.balloons()
        st.subheader(f"📍 خارطة طريق الطالب: {name}")
        
        schools = [
            {"n": "كلية الطب والصيدلة", "s": 16.0, "p": "تتطلب نفساً طويلاً في الحفظ والعلوم."},
            {"n": "مدرسة المهندسين ENSA", "s": 14.5, "p": "مثالية لعشاق الرياضيات والابتكار التقني."},
            {"n": "المدرسة الوطنية للتجارة ENCG", "s": 13.5, "p": "للمهتمين بعالم المال، الأعمال والتدبير."},
            {"n": "المدرسة العليا للتكنولوجيا EST", "s": 12.0, "p": "تكوين تطبيقي سريع يؤهلك لسوق العمل في عامين."}
        ]

        for s in schools:
            chance = "عالية جداً" if note >= s['s']+1 else "متوسطة" if note >= s['s'] else "تحتاج بذل مجهود"
            color = "#10b981" if note >= s['s'] else "#f59e0b"
            
            st.markdown(f"""
                <div class='card'>
                    <div style='display: flex; justify-content: space-between;'>
                        <h3 style='color: #1e3a8a;'>{s['n']}</h3>
                        <span class='seuil-badge'>Seuil: {s['s']}</span>
                    </div>
                    <p>{s['p']}</p>
                    <p>📊 نسبة القبول المتوقعة: <b style='color: {color};'>{chance}</b></p>
                </div>
                """, unsafe_allow_html=True)

# 7. قسم الأسئلة الشائعة (FAQ)
st.markdown("---")
st.write("### ❓ أسئلة شائعة تهمك")
with st.expander("متى يبدأ التسجيل في المدارس الكبرى؟"):
    st.write("يبدأ التسجيل غالباً في أواخر شهر مايو ويمتد إلى نهاية يونيو عبر البوابات الإلكترونية.")
with st.expander("هل يمكنني تغيير الشعبة بعد البكالوريا؟"):
    st.write("نعم، بعض المدارس مثل ENCG أو EST تقبل شعباً مختلفة، لكن الأولوية دائماً للشعب التقنية والعلمية في المدارس الهندسية.")

# 8. التذييل
st.markdown(f"<p style='text-align: center; color: gray;'>تم التطوير بكل ❤️ بواسطة أنس | تحديث {today.year}</p>", unsafe_allow_html=True)
