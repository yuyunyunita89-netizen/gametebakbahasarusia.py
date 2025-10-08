import streamlit as st
import random

# Judul aplikasi
st.title("🎯 Game Tebak Bahasa Rusia 🇷🇺")
st.write("Tebak arti kata atau frasa dalam Bahasa Rusia. Selamat bermain!")

# Data kosakata Rusia - Indonesia
questions = {
    "Здравствуйте": "Halo",
    "Спасибо": "Terima kasih",
    "Пожалуйста": "Sama-sama / Silakan",
    "До свидания": "Sampai jumpa",
    "Да": "Ya",
    "Нет": "Tidak",
    "Как дела?": "Apa kabar?",
    "Хорошо": "Baik",
    "Плохо": "Buruk",
    "Как вас зовут?": "Siapa nama Anda?",
    "Меня зовут": "Nama saya adalah",
    "Сколько вам лет?": "Berapa umur Anda?",
    "Извините": "Maaf",
    "Где вы живёте?": "Di mana Anda tinggal?",
    "Я говорю по-русски": "Saya berbicara bahasa Rusia",
    "Я не понимаю": "Saya tidak mengerti",
    "Кот": "Kucing",
    "Собака": "Anjing",
    "Книга": "Buku",
    "Музыка": "Musik"
}

# Inisialisasi sesi permainan
if "score" not in st.session_state:
    st.session_state.score = 0
if "current" not in st.session_state:
    st.session_state.current = 0
if "questions" not in st.session_state:
    items = list(questions.items())
    random.shuffle(items)
    st.session_state.questions = items
if "total" not in st.session_state:
    st.session_state.total = len(questions)

# Ambil soal saat ini
if st.session_state.current < st.session_state.total:
    russian_word, correct_answer = st.session_state.questions[st.session_state.current]

    st.subheader(f"Soal ke-{st.session_state.current + 1} dari {st.session_state.total}")
    st.markdown(f"### 🇷🇺 {russian_word}")

    player_answer = st.text_input("Masukkan arti kata dalam Bahasa Indonesia:")

    if st.button("Periksa Jawaban"):
        if player_answer.strip().lower() == correct_answer.lower():
            st.success("✅ Jawaban Anda benar!")
            st.session_state.score += 1
        else:
            st.error(f"❌ Salah. Jawaban yang benar adalah: **{correct_answer}**")

        st.session_state.current += 1
        st.experimental_rerun()
else:
    st.success("🎉 Game Selesai!")
    st.write(f"Skor akhir Anda: **{st.session_state.score} dari {st.session_state.total}**")

    if st.button("Main Lagi 🔁"):
        st.session_state.score = 0
        st.session_state.current = 0
        items = list(questions.items())
        random.shuffle(items)
        st.session_state.questions = items
        st.experimental_rerun()
