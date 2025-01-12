#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 21:42:04 2025

@author: Jorge Cabrera-Moreno
         Postdoctoral Fellow
         University of Zurich
         Institute of Evolutionary Anthropology
         Evolutionary Cognition Group
         Zurich, Switzerland
        
         Description:
            Web Portafolio
"""
from flask import Flask, render_template

app = Flask(__name__)  # Initialize the Flask app

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for the "About Me" page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)  # Run the Flask app in debug mode