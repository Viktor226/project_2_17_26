
import streamlit as st

# Инициализация списка книг в session_state для сохранения между перезапусками
if 'books' not in st.session_state:
    st.session_state.books = [
        "The Hobbit",
        "1984",
        "Harry Potter",
        "Sherlok Holms",
        "Top gear"
    ]

st.title("📚 Book Checker App")
st.write("Enter a book title to check if it exists in the database.")

# Поле ввода
user_input = st.text_input("Book Title")

# Создаем две колонки для кнопок
col1, col2 = st.columns(2)

with col1:
    # Кнопка для проверки книги
    if st.button("🔍 Check Book"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a book title")
        elif user_input in st.session_state.books:
            st.success(f"✅ The book '{user_input}' exists in database!")
        else:
            st.error(f"❌ The book '{user_input}' is NOT in the database")

with col2:
    # Кнопка для добавления книги
    if st.button("➕ Add Book"):
        if user_input.strip() == "":
            st.warning("⚠️ Please enter a book title to add")
        elif user_input in st.session_state.books:
            st.warning(f"⚠️ The book '{user_input}' already exists in database!")
        else:
            st.session_state.books.append(user_input)
            st.success(f"✅ Book '{user_input}' has been added to database!")

# Показываем текущий список книг (для проверки)
with st.expander("📋 Show current book list"):
    if st.session_state.books:
        for i, book in enumerate(st.session_state.books, 1):
            st.write(f"{i}. {book}")
    else:
        st.write("No books in database yet")
   
      
    
