# -*- coding: utf-8 -*-
"""
Created on Mon May 18 17:03:46 2020

@author: gouth
"""

from flask import Flask,render_template,request
import pickle
import numpy as np
model=pickle.load(open("projectfinal1.pkl",'rb'))
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("basic.html")
@app.route('/login',methods=['POST'])
def login():
    file=request.form['s']
    file1=request.form['st']
    file2=request.form['time']
    file3=request.form['wages']
    file4=request.form['year']
    
    if(file1=="california city"):
        s1,s2,s3,s4,s5=1,0,0,0,0
    if(file1=="new york"):
        s1,s2,s3,s4,s5=0,0,0,0,1
    if(file1=="texas"):
        s1,s2,s3,s4,s5=0,0,0,1,0
    if(file1=="jersey"):
        s1,s2,s3,s4,s5=0,0,1,0,0
    if(file1=="florida"):
        s1,s2,s3,s4,s5=0,1,0,0,0
    if(file=="computer occupations"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,0,1,0,0,0,0,0
    elif(file=="Financial Occupation"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,1,0,0,0,0
    elif(file=="Management Occupation"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,1,0,0,0
    elif(file=="Architechture & Enginneering"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,1,0,0,0,0,0,0,0
    elif(file=="Business Occupation"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,1,0,0,0,0,0,0
    elif(file=="Medical Occupation"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,1,0
    elif(file=="Marketing Occupation"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,1,0,0
    elif(file=="Advance Science"):
        a1,a,a3,a4,a5,a6,a7,a8,a9=1,0,0,0,0,0,0,0,0
    else:
        a1,a,a3,a4,a5,a6,a7,a8,a9=0,0,0,0,0,0,0,0,1
    y_pred=[[2]]
    total=[[a1,a,a3,a4,a5,a6,a7,a8,a9,s1,s2,s3,s4,s5,file2,int(file3),int(file4)]]
    y_pred=model.predict(np.array(total))
    
    if (y_pred==[[2]]):
        return render_template("basic.html",showcase="  ")
        
    if(y_pred==[[0]]):
         return render_template("basic.html",showcase="your visa is confirmed")
    else:
         return render_template("basic.html",showcase="your visa is rejected")
    
if(__name__)=='__main__':
     app.run(debug=False)