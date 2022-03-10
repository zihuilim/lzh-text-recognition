#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, request, render_template


# In[2]:


app = Flask(__name__)


# In[5]:


from textblob import TextBlob

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method=="POST":
        t = request.form.get("text")
        print(t)
        r = TextBlob(t).sentiment
        
        return(render_template("index.html", results=r))  
    else:
        return(render_template("index.html", results="2"))


# In[ ]:


if __name__ == "__main__":
    app.run()

