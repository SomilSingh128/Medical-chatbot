import os
import sys
import google.generativeai as genai
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv

app = Flask(__name__)

def generate_prompt(query, context):
    escaped = context.replace("'","").replace('"', "").replace("\n"," ")
    prompt = ("""
  You are a helpful and informative chatbot that answer questions using text from the reference context included below. \
  Respond in a complete sentence, being comprehensive, include all relevant background information. \
  You are talking to a non-technical audience, so be sure to break down complicated concepts and \
  strike a friendly and converstional tone. \
  If the context is irrelevant to the answer, you may ignore it.
                QUESTION: '{query}'
                CONTEXT: '{context}'
              
              ANSWER:
              """).format(query=query, context=context)
    return prompt

def get_relevant_context_from_db(query):
    context = ""
    embedding_function=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = Chroma(persist_directory="./chroma_db_nccn", embedding_function=embedding_function)
    search_results = vector_db.similarity_search(query, k=6)
    for result in search_results:
        context += result.page_content + "\n"
    return context

def generate_answer(prompt):
    load_dotenv()
    genai.configure(api_key=os.environ['GEMINI_API_KEY'])
    model = genai.GenerativeModel(model_name='gemini-pro')
    answer = model.generate_content(prompt)
    return answer.text

@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    query = request.form["msg"]
    context = get_relevant_context_from_db(query)
    prompt = generate_prompt(query=query, context=context)
    answer = generate_answer(prompt=prompt)
    return answer

if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)
    /my 