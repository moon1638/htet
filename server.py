from flask import Flask,render_template
import json
w=json.load(open("worldl.json"))

app= Flask(__name__)
page_size=20
@app.route('/')
def mainPage():
	return render_template('index.html',w=w[0:page_size])
@app.route('/begin/<b>')
def beginPage(b):
	bn=int(b)
	return render_template('index.html',w=w[bn:bn+page_size],
		page_number=bn, page_size=page_size)


@app.route('/continent/<a>')
def continentPage(a):
	cl=[c['name'] for c in w if c['continent']==a ]
	return render_template('continent.html',length_of_cl=len(cl),
		cl=cl,
		a=a
		)
@app.route('/country/<i>')
def countryPage(i):
	return render_template('country.html',c=w[int(i)])

@app.route('/countryByName/<n>')
def countryByNamePage(n):
	c = None
	for x in w:
		if x['name'] == n:
			c = x
	return render_template(
		'country.html',
		c = c)

app.run(host='0.0.0.0', port=5638, debug=True)