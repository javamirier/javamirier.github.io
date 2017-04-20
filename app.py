from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.
URLs that will call the index() function if running app.py on localhost:
	http://localhost:5000/
	http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
	return render_template('index.html') # located in templates/


@app.route('/about')
def about():
	return render_template('about.html')
    
@app.route('/brandBMWDetails')
def brandBMWDetails():
	return render_template('brandBMWDetails.html')
    
@app.route('/brandChevroletDetails')
def brandChevroletDetails():
	return render_template('brandChevroletDetails.html')

@app.route('/brandFordDetails')
def brandFordDetails():
	return render_template('brandFordDetails.html')

@app.route('/brandindex')
def brandindex():
	return render_template('brandindex.html')

@app.route('/brandMercedesDetails')
def brandMercedesDetails():
	return render_template('brandMercedesDetails.html')

@app.route('/brandNissanDetails')
def brandNissanDetails():
	return render_template('brandNissanDetails.html')

@app.route('/brandVWDetails')
def brandVWDetails():
	return render_template('brandVWDetails.html')
    
@app.route('/classCoupe')
def classCoupe():
	return render_template('classCoupe.html')
    
@app.route('/classHatchback')
def classHatchback():
	return render_template('classHatchback.html')
    
@app.route('/classindex')
def classindex():
	return render_template('classindex.html')
    
@app.route('/classPickup')
def classPickup():
	return render_template('classPickup.html')
    
@app.route('/classSedan')
def classSedan():
	return render_template('classSedan.html')
    
@app.route('/classSUV')
def classSUV():
	return render_template('classSUV.html')

@app.route('/classVan')
def classVan():
	return render_template('classVan.html')
    
@app.route('/modelBMWI3')
def modelBMWI3():
	return render_template('modelBMWI3.html')    
    
@app.route('/modelBMWM4')
def modelBMWM4():
	return render_template('modelBMWM4.html')

@app.route('/modelBMWX1')
def modelBMWX1():
	return render_template('modelBMWX1.html')        
    
@app.route('/modelChevroletCruze')
def modelChevroletCruze():
	return render_template('modelChevroletCruze.html')

@app.route('/modelChevroletExpress')
def modelChevroletExpress():
	return render_template('modelChevroletExpress.html')    
    
@app.route('/modelChevroletSilverado')
def modelChevroletSilverado():
	return render_template('modelChevroletSilverado.html')

@app.route('/modelFordExplorer')
def modelFordExplorer():
	return render_template('modelFordExplorer.html')
    
@app.route('/modelFordFocusRS')
def modelFordFocusRS():
	return render_template('modelFordFocusRS.html')

@app.route('/modelFordMustang')
def modelFordMustang():
	return render_template('modelFordMustang.html')
    
@app.route('/modelindex')
def modelindex():
	return render_template('modelindex.html')

@app.route('/modelMBCClass')
def modelMBCClass():
	return render_template('modelMBCClass.html')
    
@app.route('/modelMBG63')
def modelMBG63():
	return render_template('modelMBG63.html')

@app.route('/modelMBSprinter')
def modelMBSprinter():
	return render_template('modelMBSprinter.html')
    
@app.route('/modelNissanArmada')
def modelNissanArmada():
	return render_template('modelNissanArmada.html')

@app.route('/modelNissanGTR')
def modelNissanGTR():
	return render_template('modelNissanGTR.html')
    
@app.route('/modelNissanVersa')
def modelNissanVersa():
	return render_template('modelNissanVersa.html')

@app.route('/modelVWAmarok')
def modelVWAmarok():
	return render_template('modelVWAmarok.html')
    
@app.route('/modelVWCrafter')
def modelVWCrafter():
	return render_template('modelVWCrafter.html')

@app.route('/modelVWJetta')
def modelVWJetta():
	return render_template('modelVWJetta.html')
    
'''	
@app.route('/page3')
def page3():
	dict = {'string1' : 'Testing.', 'string2' : 'Hello, World!'}
	return render_template('page3.html', strings = dict) # Example of argument passing to HTML template
'''    
	
if __name__ == '__main__':
	app.run() # Run application
