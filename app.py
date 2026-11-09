
import streamlit as st

st.set_page_config(
    page_title="Математический кроссворд",
    page_icon="📐",
    layout="centered"
)

st.title("📐 Математический кроссворд")
st.subheader("10 класс")
st.write("Проверь свои знания по математике!")

questions = [
    {
        "question": "1. Как называется результат возведения числа в степень?",
        "answer": "степень"
    },
    {
        "question": "2. Как называется число, которое возводят в степень?",
        "answer": "основание"
    },
    {
        "question": "3. Как называется результат извлечения корня?",
        "answer": "корень"
    },
    {
        "question": "4. Как называется отношение противолежащего катета к гипотенузе?",
        "answer": "синус"
    },
    {
        "question": "5. Как называется отношение прилежащего катета к гипотенузе?",
        "answer": "косинус"
    },
    {
        "question": "6. Как называется функция y = x²?",
        "answer": "квадратичная"
    },
    {
        "question": "7. Как называется множество допустимых значений аргумента?",
        "answer": "область"
    },
    {
        "question": "8. Как называется равенство с неизвестной?",
        "answer": "уравнение"
    },
    {
        "question": "9. Как называется отношение синуса к косинусу?",
        "answer": "тангенс"
    },
    {
        "question": "10. Как называется число под знаком корня?",
        "answer": "подкоренное"
    }
]

st.info("Ответь на все 10 вопросов. Пиши ответы маленькими буквами.")

answers = []

with st.form("crossword"):
    for i, item in enumerate(questions):
        st.write(item["question"])
        answer = st.text_input(
            "Твой ответ:",
            key=f"answer_{i}"
        )
        answers.append(answer)

    submitted = st.form_submit_button("Проверить ответы")

if submitted:
    score = 0

    st.subheader("Результаты:")

    for i, item in enumerate(questions):
        correct = item["answer"]
        user_answer = answers[i].strip().lower()

        if user_answer == correct:
            score += 1
            st.success(f"Вопрос {i+1}: правильно! ✓")
        else:
            st.error(
                f"Вопрос {i+1}: неправильно. "
                f"Правильный ответ: {correct}"
            )

    st.divider()

    st.subheader(f"Твой результат: {score} из 10")

    if score == 10:
        st.balloons()
        st.success("Отлично! Ты прекрасно знаешь математику!")
    elif score >= 7:
        st.success("Хороший результат! Так держать!")
    elif score >= 4:
        st.warning("Неплохо, но стоит повторить материал.")
    else:
        st.info("Попробуй ещё раз и повтори темы!")

    if st.button("Пройти заново"):
        st.rerun()

st.divider()
st.caption("Математический кроссворд • 10 класс")
