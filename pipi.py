import streamlit as st
import random

st.set_page_config(
    page_title="เกมคำศัพท์อาหารเกาหลี",
    page_icon="🇰🇷",
    layout="centered"
)

vocabulary = [
    {
        "korean": "비빔밥",
        "thai": "พีบิมบับ",
        "meaning": "ข้าวยำเกาหลี"
    },
    {
        "korean": "불고기",
        "thai": "พุลโกกิ",
        "meaning": "เนื้อวัวผัดหรือย่างซีอิ๊วเกาหลี"
    },
    {
        "korean": "삼겹살",
        "thai": "ซัมกย็อบซัล",
        "meaning": "หมูสามชั้นย่าง"
    },
    {
        "korean": "볶음밥",
        "thai": "บกอึมบับ",
        "meaning": "ข้าวผัด"
    },
    {
        "korean": "짜장면",
        "thai": "จาจังมยอน",
        "meaning": "บะหมี่ซอสถั่วดำ"
    },
    {
        "korean": "냉면",
        "thai": "แนงมยอน",
        "meaning": "บะหมี่เย็น"
    },
    {
        "korean": "김치찌개",
        "thai": "คิมชิชีเก",
        "meaning": "แกงกิมจิ"
    },
    {
        "korean": "삼계탕",
        "thai": "ซัมกเยทัง",
        "meaning": "ไก่ตุ๋นโสม"
    },
    {
        "korean": "떡볶이",
        "thai": "ต็อกโปกกี",
        "meaning": "แป้งต็อกผัดซอสเผ็ด"
    },
    {
        "korean": "고기",
        "thai": "โคกี",
        "meaning": "เนื้อสัตว์"
    },
    {
        "korean": "치킨",
        "thai": "ชิชิน",
        "meaning": "ไก่ทอดสไตล์เกาหลี"
    },
    {
        "korean": "녹차",
        "thai": "นกชา",
        "meaning": "ชาเขียว"
    }
]

# -----------------------------
# ตั้งค่าเกม
# -----------------------------

if "questions" not in st.session_state:
    st.session_state.questions = random.sample(
        vocabulary,
        len(vocabulary)
    )

if "current" not in st.session_state:
    st.session_state.current = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "message" not in st.session_state:
    st.session_state.message = ""


# -----------------------------
# เริ่มเกมใหม่
# -----------------------------

def restart_game():
    st.session_state.questions = random.sample(
        vocabulary,
        len(vocabulary)
    )
    st.session_state.current = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.message = ""
    st.rerun()


# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.main {
    background: linear-gradient(
        135deg,
        #fff1f2,
        #ffe4e6,
        #fef3c7
    );
}

.game-title {
    text-align: center;
    color: #dc2626;
    font-size: 38px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 25px;
}

.korean {
    text-align: center;
    font-size: 65px;
    font-weight: bold;
    margin: 20px;
}

.meaning {
    text-align: center;
    font-size: 22px;
    color: #555;
    margin-bottom: 30px;
}

.result {
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}

.correct {
    background: #dcfce7;
    color: #15803d;
}

.wrong {
    background: #fee2e2;
    color: #b91c1c;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="game-title">🇰🇷 เกมเติมคำศัพท์อาหารเกาหลี 🍜</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">ดูคำศัพท์เกาหลี แล้วเติมคำอ่านภาษาไทย</div>',
    unsafe_allow_html=True
)


# -----------------------------
# ตรวจว่าจบเกมหรือยัง
# -----------------------------

if st.session_state.current >= len(st.session_state.questions):

    st.success("🎉 จบเกมแล้ว!")

    score = st.session_state.score
    total = len(st.session_state.questions)

    percentage = int(score / total * 100)

    st.markdown(
        f"""
        <h2 style="text-align:center;">
        🏆 คะแนนของคุณ
        </h2>

        <h1 style="text-align:center;color:#dc2626;">
        {score} / {total}
        </h1>

        <h3 style="text-align:center;">
        ได้ {percentage}%
        </h3>
        """,
        unsafe_allow_html=True
    )

    if percentage == 100:
        st.balloons()
        st.success("🌟 สุดยอด! จำคำศัพท์ได้ครบทุกคำ!")

    elif percentage >= 80:
        st.success("👏 เก่งมาก!")

    elif percentage >= 50:
        st.info("👍 ทำได้ดี ลองเล่นอีกครั้งเพื่อจำให้แม่นขึ้น")

    else:
        st.warning("💪 ลองเล่นอีกครั้งนะ!")

    st.button(
        "🔄 เล่นใหม่",
        on_click=restart_game,
        use_container_width=True
    )

    st.stop()


# -----------------------------
# คำถามปัจจุบัน
# -----------------------------

question = st.session_state.questions[
    st.session_state.current
]

current_number = st.session_state.current + 1
total_questions = len(st.session_state.questions)


# -----------------------------
# คะแนน
# -----------------------------

col1, col2 = st.columns(2)

with col1:
    st.metric(
        "🏆 คะแนน",
        st.session_state.score
    )

with col2:
    st.metric(
        "📚 ข้อ",
        f"{current_number} / {total_questions}"
    )


# -----------------------------
# Progress
# -----------------------------

progress = (
    st.session_state.current /
    total_questions
)

st.progress(progress)


# -----------------------------
# คำศัพท์
# -----------------------------

st.markdown(
    f'<div class="korean">{question["korean"]}</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="meaning">🍽️ {question["meaning"]}</div>',
    unsafe_allow_html=True
)


# -----------------------------
# ช่องคำตอบ
# -----------------------------

answer = st.text_input(
    "✏️ คำอ่านภาษาไทย",
    placeholder="เช่น พีบิมบับ",
    disabled=st.session_state.answered
)


# -----------------------------
# ตรวจคำตอบ
# -----------------------------

if not st.session_state.answered:

    if st.button(
        "ตรวจคำตอบ ✓",
        type="primary",
        use_container_width=True
    ):

        user_answer = answer.strip()
        correct_answer = question["thai"]

        if user_answer == "":
            st.warning("⚠️ กรุณาพิมพ์คำตอบก่อน")

        elif user_answer == correct_answer:

            st.session_state.score += 1
            st.session_state.answered = True
            st.session_state.message = "correct"
            st.rerun()

        else:

            st.session_state.answered = True
            st.session_state.message = "wrong"
            st.rerun()


# -----------------------------
# แสดงผล
# -----------------------------

if st.session_state.answered:

    if st.session_state.message == "correct":

        st.markdown(
            f"""
            <div class="result correct">
            🎉 ถูกต้อง!<br>
            {question["korean"]} =
            {question["thai"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="result wrong">
            ❌ ยังไม่ถูก<br>
            คำตอบที่ถูกคือ<br>
            <strong>{question["thai"]}</strong>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.write("")

    if st.button(
        "➡️ ข้อถัดไป",
        use_container_width=True
    ):

        st.session_state.current += 1
        st.session_state.answered = False
        st.session_state.message = ""

        st.rerun()


# -----------------------------
# เล่นใหม่
# -----------------------------

st.write("")

if st.button(
    "🔄 เริ่มเกมใหม่",
    use_container_width=True
):
    restart_game()
