from flask import Flask, jsonify, request

from storage import all_articles, liked_articles, not_liked_articles
from demographic_filtering import output
from content_filtering import get_recommendations

app = Flask(__name__)

@app.route("/get-article")
def get_article():
    movie_data = {
        "url": all_articles[0][11],
        "title": all_articles[0][12],
        "text": all_articles[0][13],
        "lang": all_articles[0][14],
        "total_events": all_articles[0][15]
    }
    return jsonify({
        "data": movie_data,
        "status": "success"
    })

@app.route("/liked-article", methods=["POST"])
def liked_article():
    article = all_articles[0]
    liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-article", methods=["POST"])
def unliked_article():
    article = all_articles[0]
    not_liked_articles.append(article)
    all_articles.pop(0)
    return jsonify({
        "status": "success"
    }), 201

# API to return most popular articles.
@app.route("/popular-articles")
def popular_articles():
    
    return "Top 20 articles using demographic filtering method" 

# API to return top 10 similar articles using content based filtering method.
@app.route("/recommended-articles")
def recommended_articles():
    
    return "Top 10 articles using content based filtering method" 

# run the app
if __name__ == "__main__":
    app.run()