from flask import Blueprint, render_template , url_for,redirect,request,jsonify
from flask import Flask
from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob
from googletrans import Translator
import google.generativeai as palm



palm.configure(api_key='AIzaSyCw9UHFLxolOl9fEBLnwFedqMBC6Sj8nPk')
# Use the palm.list_models function to find available models:
models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
model = models[0].name
def solution(name):
    prompt = name
    completion = palm.generate_text(
        model=model,
        prompt=prompt,
        temperature=0,
        # The maximum length of the response
        max_output_tokens=800,
    )
    result=completion.result 
    return result




#blogpost
languages = {
      "Spanish": 'es',
      "Chinese": 'zh-CN',
      "bengali": 'bn',
      "german": 'de',
      "hindi": 'hi',
      "Italian": 'it'
  }
text="Anatomy is the identification and description of the structures of living things. It is a branch of biology and medicine. People who study anatomy study the body, how it is made up, and how it works. The study of anatomy dates back more than 2,000 yearsTrusted Source, to the Ancient Greeks. There are three broad areas: human anatomy animal anatomy — zootomy plant anatomy — phytotomy Human anatomy is the study of the structures of the human body. An understanding of anatomy is key to the practice of medicine and other areas of health. The word “anatomy” comes from the Greek words “ana,” meaning “up,” and “tome,” meaning “a cutting.” Traditionally, studies of anatomy have involved cutting up, or dissecting, organisms. Now, however, imaging technology can show us much about how the inside of a body works, reducing the need for dissection. Below, learn about the two main approaches: microscopic anatomy and gross, or macroscopic, anatomy."
# Check if the user's input matches a language in the dictionary
translator = Translator()
from flask import Flask, render_template, request,url_for,redirect
app=Flask(__name__)
result=text
#blogpost

app=Flask(__name__)
@app.route("/")
def welcome1():
 return render_template("welcome1.html")
@app.route("/home")
def home():
 return render_template("home.html")

@app.route("/profile") 
def profile():
 return render_template("profile.html")

@app.route("/about")
def back():
 return render_template("about.html")

@app.route("/blog")
def blog():
  return render_template("blog.html")


#blogpost
@app.route("/blogpost")
def blogpost():
  return render_template('blogpost.html', output=text)

@app.route('/<string:language>',methods=['GET','POST'])
def welcome2(language):
    result = translator.translate(text, dest=language).text
    return render_template('blogpost.html', output=result)


@app.route('/submit',methods=['GET'])
def submit():
    selected_fruit = request.args.get('Language')
    if selected_fruit=='english':
        language='en'
    else:
        language=languages[selected_fruit]
    return(redirect(url_for('welcome2',language=language)))
#blogpost


@app.route("/contact")
def contact():
 return render_template("contact.html")

@app.route("/content_librery")
def contact_librery():
 return render_template("content_library.html")
 
@app.route("/courses")
def courses():
 return render_template("courses.html")

@app.route("/login")
def helloworld():
    return render_template("login.html")

database = {'sohambiswas05@gmail.com': '555', 'roshnimitra02@gmail.com': '222', 'sourashissarkar3@gmail.com': '333'}

@app.route('/hom', methods=['POST', 'GET'])
def login():
    name1 = request.form['email']
    pwd = request.form['pass']
    if name1 not in database:
        return render_template('login.html')
        flash('Invalid User', category='error')
    
    else:
        if database[name1] != pwd:
            return render_template('login.html')
            flash('Incorrect user', category='error')
            
        else:
            return render_template('home.html', name=name1)
            flash('Logged in successfully!', category='error')
        
@app.route("/playlist")
def playlist():
 return render_template("playlist.html")

@app.route("/register")
def register():
 return render_template("register.html")

@app.route("/research")
def research():
 return render_template("research.html")

@app.route("/search")
def search():
  return render_template("search.html")

@app.route("/teacher_profile")
def teacher_profile():
 return render_template("teacher_profile.html")

@app.route("/teachers")
def teachers():
 return render_template("teachers.html")

@app.route("/update")
def update():
 return render_template("update.html")

@app.route("/watch-video")
def watch_video():
 return render_template("watch-video.html")

@app.route("/index1234")
def index1234():
 return render_template("index1234.html")

@app.route("/chat")
def chat_assistant():
    return render_template('bot.html')
#healthbot
@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']
    bot_response = generate_response(user_message)  # Implement your bot logic here
    return jsonify({'response': bot_response})

def generate_response(user_message):
    # Implement your chatbot logic here
    responses = solution(user_message)
    return responses
#healthbot
@app.route("/voice")
def index():
    return render_template('bot copy.html')

@app.route('/process_voice', methods=['POST'])
def process_voice():
    user_message = request.form['user_message']
    bot_response = generate_response(user_message)  # Implement your bot logic here
    return jsonify({'response': bot_response})

def generate_response(user_message):
    res=solution(user_message)
    return res
@app.route("/output")
def output():
 return render_template("output.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)


