#@imports


from flask import Flask,url_for
from flask import render_template

app=Flask(__name__)

#@app logics goes here

#@Home page....

@app.route('/')
def Home():
   return render_template('index.html')

#@Blog page ...


@app.route('/Blogs')
def Blogs():
   return render_template('blogs.html')
#@Services page ...

@app.route('/Services')
def Services():
   return render_template('services.html')
#@project page ...


@app.route('/Projects')
def Projects():
   return render_template('projects.html')


#@end ...

if __name__=="__main__":
	app.run(debug=True)
