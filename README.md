# **Overview of Film Recomendator Django App**
A web application built with Django that provides movie suggestions based on natural language prompts. Using ChromaDB, the app performs vector searches to find the best matches.

This app uses **chromaDB vectorized database** that can vectorize movies data by:
- Title
- Overview
- Genre
- Release Date
- Key Words


# **Features**
- Log in/Register/Logout
- Query to get movie suggestion by a prompt
- Top searches page
- Each user has his own search history
- Simple and slick Bootstrap5 design

> Original movies data stored in `data_uploading/json_data/` directory. Taken from the **TMDв** along with the movies posters.

# **Installation**
> Python 3.10+ is required.

1. **Clone the repository:**
```bash
git clone https://github.com/yeghor/Movie-Recommender.git
cd Movie-Recommender
```
2. **Create a virtual enviroment:**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate
```

3. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create and fill chromaDB collections with movies data**
```bash
cd data_uploading
python upload_chroma_data.py
cd ..
```

5. **Set up the database:**
```bash
# Note that --run-syncdb flag is required as local apps don't have migrations
python manage.py migrate --run-syncdb
```

6. **Create a superuser:**
```bash
python manage.py createsuperuser
```

7. **Run the development server:**
```bash
python manage.py runserver
```

## Usage
- Navigate **to http://127.0.0.1:8000** in your web browser.
- Sign up for an account or log in.
- Open main page, and start making queries.
