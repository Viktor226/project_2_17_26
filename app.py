import streamlit as st
books = [
  "The Hobbit"
  "1984"
  "Harry Potter"
  "Sherlok Holms"
  "Top gear"
  
]
st.title("Book Checker App")
st.write("Enter a book title to check if it exist in the database.")
user_input =st.text_input("Book Title")
if st.button("Check Book"):
  if user_input.strip() == "":
    st.warning("Please enter a book title")
  elif user_input in books:
    st.success("The book exist in database!")
  else :
    st.error("The book is NOT in the database")
    st.write("you can add this book in database")
    if st.button("add book"):
      books.append(user_input)
      st.write("book",user_input,"has been added to database") 
      
    
