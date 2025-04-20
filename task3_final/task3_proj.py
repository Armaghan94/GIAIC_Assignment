import streamlit as st
import pickle
import os

# ---------------------------
# Helper Functions
# ---------------------------
def save_library(library, filename='library.pkl'):
    with open(filename, 'wb') as f:
        pickle.dump(library, f)

def load_library(filename='library.pkl'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return []

def add_book(library, book):
    library.append(book)
    save_library(library)

def remove_book(library, title):
    new_library = [book for book in library if book['title'].lower() != title.lower()]
    save_library(new_library)
    return new_library

def search_books(library, query):
    return [book for book in library if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]

def get_statistics(library):
    total = len(library)
    read = len([b for b in library if b['read']])
    unread = total - read
    genres = list(set([b['genre'] for b in library]))
    return total, read, unread, genres

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("📚 Personal Library Manager")

library = load_library()

menu = st.sidebar.selectbox("Menu", ["Add Book", "Remove Book", "Search Books", "View Library", "Statistics"])

if menu == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=0, max_value=2100, step=1)
    genre = st.text_input("Genre")
    read = st.checkbox("Read?")
    if st.button("Add Book"):
        if title and author:
            new_book = {
                'title': title,
                'author': author,
                'year': year,
                'genre': genre,
                'read': read
            }
            add_book(library, new_book)
            st.success(f"Book '{title}' added!")
        else:
            st.error("Title and Author are required.")

elif menu == "Remove Book":
    st.subheader("❌ Remove a Book")
    title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove"):
        updated_library = remove_book(library, title)
        if len(updated_library) < len(library):
            library = updated_library
            st.success(f"Book '{title}' removed.")
        else:
            st.warning("Book not found.")

elif menu == "Search Books":
    st.subheader("🔍 Search Books")
    query = st.text_input("Search by title or author")
    if query:
        results = search_books(library, query)
        if results:
            for book in results:
                st.write(book)
        else:
            st.info("No matching books found.")

elif menu == "View Library":
    st.subheader("📖 Your Library")
    if library:
        for book in library:
            st.markdown(f"**{book['title']}** by {book['author']} ({book['year']}) - *{book['genre']}* - {'✅ Read' if book['read'] else '📖 Unread'}")
    else:
        st.info("Your library is empty.")

elif menu == "Statistics":
    st.subheader("📊 Library Statistics")
    total, read, unread, genres = get_statistics(library)
    st.write(f"**Total Books:** {total}")
    st.write(f"**Books Read:** {read}")
    st.write(f"**Books Unread:** {unread}")
    st.write(f"**Genres:** {', '.join(genres) if genres else 'None'}")
