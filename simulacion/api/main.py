from flask import Flask, sessions
from flask import jsonify
from config import config
from models import db, Country, Usuario, Precio_moneda, Moneda, Cuenta_bancaria, Usuario_tiene_moneda, Consulta
from flask import request
from flask import render_template,redirect

def create_app(enviroment):
	app = Flask(__name__)
	app.config.from_object(enviroment)
	with app.app_context():
		db.init_app(app)
		db.create_all()
	return app
	
# obtener id cuando se requiera 
def getMaxID(tabla,id):
	max = 0
	lista = [ fila.json() for fila in tabla.query.all() ]
	for i in lista:
		if(max<=i[id]):
			max=i[id]
	return max+1

# Accedemos a la clase config del archivo config.py
enviroment = config['development']
app = create_app(enviroment)

# Rutas para Tablas -> allTabla.html
# usuario
@app.route('/api/usuario', methods=['GET'])
def IndexTablausuario():
	users = [ fila.json() for fila in Usuario.query.all() ]
	id = Usuario.getID()
	return render_template('allTabla.html', lista=users, nombre="usuario", id=id)

# pais
@app.route('/api/pais', methods=['GET'])
def IndexTablapais():
	pais = [ fila.json() for fila in Country.query.all() ]
	id = Country.getID()
	return render_template('allTabla.html', lista=pais, nombre="pais", id=id)

# precio_moneda
@app.route('/api/precio_moneda', methods=['GET'])
def IndexTabla_precio_moneda():
	precio_moneda = [ fila.json() for fila in Precio_moneda.query.all() ]
	id = Precio_moneda.getID()
	return render_template('allTabla.html', lista=precio_moneda, nombre="precio_moneda", id=id)

# moneda
@app.route('/api/moneda', methods=['GET'])
def IndexTabla_moneda():
	moneda = [ fila.json() for fila in Moneda.query.all() ]
	id = Moneda.getID()
	return render_template('allTabla.html', lista=moneda, nombre="moneda", id=id)

# cuenta_bancaria
@app.route('/api/cuenta_bancaria', methods=['GET'])
def IndexTabla_cuenta_bancaria():
	cuenta_bancaria = [ fila.json() for fila in Cuenta_bancaria.query.all() ]
	id = Cuenta_bancaria.getID()
	return render_template('allTabla.html', lista=cuenta_bancaria, nombre="cuenta_bancaria", id=id)

# usuario_tiene_moneda
@app.route('/api/usuario_tiene_moneda', methods=['GET'])
def IndexTabla_usuario_tiene_moneda():
	usuario_tiene_moneda = [ fila.json() for fila in Usuario_tiene_moneda.query.all() ]
	id = Usuario_tiene_moneda.getID()
	return render_template('allTabla.html', lista=usuario_tiene_moneda, nombre="usuario_tiene_moneda", id=id)

# READ
@app.route('/api/<nombre_tabla>/read/<id>', methods=['GET'])
def get_user(id,nombre_tabla):
	lista = id.split('=')
	if len(lista) == 1:
		if nombre_tabla == "usuario":
			ide =Usuario.getID()
			return render_template('read.html', id=ide, tabla=nombre_tabla,data=Usuario.query.filter_by(id=id).first().json()) 
		elif nombre_tabla == "pais":
			ide =Country.getID()
			return render_template('read.html', id=ide, tabla=nombre_tabla,data=Country.query.filter_by(cod_pais=id).first().json())
		elif nombre_tabla == "cuenta_bancaria":
			ide =Cuenta_bancaria.getID()
			return render_template('read.html', id=ide, tabla=nombre_tabla,data=Cuenta_bancaria.query.filter_by(numero_cuenta=id).first().json())
		elif nombre_tabla == "moneda":
			ide =Moneda.getID()
			return render_template('read.html', id=ide, tabla=nombre_tabla,data=Moneda.query.filter_by(id=id).first().json())	
	elif len(lista) == 2:
		if nombre_tabla == "precio_moneda":
			ide =Precio_moneda.getID()
			return render_template('read.html', id=ide, tabla=nombre_tabla,data=Precio_moneda.query.filter_by(id_moneda=lista[0],fecha=lista[1]).first().json())
		elif nombre_tabla == "usuario_tiene_moneda":
			ide =Usuario_tiene_moneda.getID()
			return render_template('read.html', id=ide,tabla=nombre_tabla,data=Usuario_tiene_moneda.query.filter_by(id_usuario=lista[0],id_moneda=lista[1]).first().json())

# UPDATE
@app.route('/api/<nombre_tabla>/edit/<id>', methods=['GET'])
def get_users(id,nombre_tabla):
	listaPaises = [ fila.json() for fila in Country.query.all() ]
	lista = id.split('=')
	if len(lista) == 1:
		if nombre_tabla == "usuario":
			data=Usuario.query.filter_by(id=id).first()
			ide = Usuario.getID()
			datos= data.json()
			return render_template('edit.html',tabla=nombre_tabla, datos=datos, nombre='usuario',id=ide,listaPaises=listaPaises)
		elif nombre_tabla == "pais":
			data=Country.query.filter_by(cod_pais=id).first()
			ide =Country.getID()
			datos= data.json()
			return render_template('edit.html',tabla=nombre_tabla, datos=datos, nombre='pais',id=ide)
		elif nombre_tabla == "cuenta_bancaria":
			data=Cuenta_bancaria.query.filter_by(numero_cuenta=id).first()
			ide = Cuenta_bancaria.getID()
			datos= data.json()
			return render_template('edit.html', tabla=nombre_tabla,datos=datos, nombre='cuenta_bancaria',id=ide)
		elif nombre_tabla == "moneda":
			data=Moneda.query.filter_by(id=id).first()
			ide = Moneda.getID()
			datos= data.json()
			return render_template('edit.html', tabla=nombre_tabla,datos=datos, nombre='moneda',id=ide)
	elif len(lista) == 2:
		if nombre_tabla == "usuario_tiene_moneda":
			data=Usuario_tiene_moneda.query.filter_by(id_usuario=lista[0],id_moneda=lista[1]).first()
			ide = Usuario_tiene_moneda.getID()
			datos= data.json()
			return render_template('edit.html',tabla=nombre_tabla, datos=datos, nombre='usuario_tiene_moneda',id=ide)
		elif nombre_tabla == "precio_moneda":
			data=Precio_moneda.query.filter_by(id_moneda=lista[0],fecha=lista[1]).first()
			ide = Precio_moneda.getID()
			datos= data.json()
			return render_template('edit.html',tabla=nombre_tabla, datos=datos, nombre='precio_moneda',id=ide)

@app.route('/api/<nombre_tabla>/update/<id>', methods=['PUT','POST'])
def update_fila(id,nombre_tabla):
	lista = id.split('=')
	if len(lista) == 1:
		if nombre_tabla == "usuario":
			try:
				fila = Usuario.query.filter_by(id=id).first()
				fila.nombre=request.form["nombre"]
				fila.apellido=request.form["apellido"]
				fila.correo=request.form["correo"]
				fila.contraseña=request.form["contraseña"]
				fila.pais=request.form["pais"]
				fila.update()
				return redirect('/api/usuario')
			except:
				return False
		elif nombre_tabla == "pais":
			try:
				fila = Country.query.filter_by(cod_pais=id).first()
				fila.nombre=request.form["nombre"]
				fila.update()
				return redirect('/api/pais')
			except:
				return False
		elif nombre_tabla == "cuenta_bancaria":
			try:
				fila = Cuenta_bancaria.query.filter_by(numero_cuenta=id).first()
				fila.id_usuario=request.form["id_usuario"]
				fila.balance=request.form["balance"]
				fila.update()
				return redirect('/api/cuenta_bancaria')
			except:
				return False
		elif nombre_tabla == "moneda":
			try:
				fila = Moneda.query.filter_by(id=id).first()
				fila.nombre=request.form["nombre"]
				fila.sigla=request.form["sigla"]
				fila.update()
				return redirect('/api/moneda')
			except:
				return False
	elif len(lista) == 2:
		if nombre_tabla == "usuario_tiene_moneda":
			try:
				fila = Usuario_tiene_moneda.query.filter_by(id_usuario=lista[0],id_moneda=lista[1]).first()
				fila.balance=request.form["balance"]
				fila.update()
				return redirect('/api/usuario_tiene_moneda')
			except:
				return False
		elif nombre_tabla == "precio_moneda":
			try:
				fila = Precio_moneda.query.filter_by(id_moneda=lista[0],fecha=lista[1]).first()
				fila.valor=request.form["valor"]
				fila.update()
				return redirect('/api/precio_moneda')
			except:
				return False
                        
# DELETE
@app.route('/api/<nombre_tabla>/delete/<id>', methods = ['REMOVE','GET'])
def delete_fila(id,nombre_tabla):
	lista = id.split('=')
	if len(lista) == 1:
		if nombre_tabla == "usuario":
			try:
				fila = Usuario.query.filter_by(id=id).first()
				fila.delete()
				return redirect('/api/usuario')
			except:
				return False
		elif nombre_tabla == "pais":
			try:
				fila = Country.query.filter_by(cod_pais=id).first()
				fila.delete()
				return redirect('/api/pais')
			except:
				return False
		elif nombre_tabla == "cuenta_bancaria":
			try:
				fila = Cuenta_bancaria.query.filter_by(numero_cuenta=id).first()
				fila.delete()
				return redirect('/api/cuenta_bancaria')
			except:
				return False
		elif nombre_tabla == "moneda":
			try:
				fila = Moneda.query.filter_by(id=id).first()
				fila.delete()
				return redirect('/api/moneda')
			except:
				return False
	elif len(lista) == 2:
		if nombre_tabla == "usuario_tiene_moneda":
			try:
				fila = Usuario_tiene_moneda.query.filter_by(id_usuario=lista[0],id_moneda=lista[1]).first()
				fila.delete()
				return redirect('/api/usuario_tiene_moneda')
			except:
				return False
		elif nombre_tabla == "precio_moneda":
			try:
				fila = Precio_moneda.query.filter_by(id_moneda=lista[0],fecha=lista[1]).first()
				fila.delete()
				return redirect('/api/precio_moneda')
			except:
				return False  

# CREATE
@app.route('/api/<nombre_tabla>/create', methods=['POST','GET'])
def direccionar(nombre_tabla):
	mensaje = ""
	if nombre_tabla == "usuario":
		datos = Usuario.jsonColumnMod()
		ide = Usuario.getID()
	elif nombre_tabla == "pais":
		datos = Country.jsonColumnMod()
		ide = Country.getID()
	elif nombre_tabla == "moneda":
		datos = Moneda.jsonColumnMod()
		ide = Moneda.getID()
	elif nombre_tabla == "precio_moneda":
		datos = Precio_moneda.jsonColumnMod()
		ide = Precio_moneda.getID()
		mensaje = "Ingresar un id_moneda existente "
	elif nombre_tabla == "cuenta_bancaria":
		datos = Cuenta_bancaria.jsonColumnMod()
		ide = Cuenta_bancaria.getID()
		mensaje = "Ingresar un id_usuario existente"
	elif nombre_tabla == "usuario_tiene_moneda":
		datos = Usuario_tiene_moneda.jsonColumnMod()
		ide = Usuario_tiene_moneda.getID()
		mensaje = "Ingresar una combinación id_usuario - id_moneda que existan"
	listaPaises = [ fila.json() for fila in Country.query.all() ]
	return render_template('create.html', datos=datos,tabla=nombre_tabla,id=ide,listaPaises=listaPaises, mensaje=mensaje)
# Action -> formulario
@app.route('/api/<nombre_tabla>/createRow', methods=['POST'])
def create_user(nombre_tabla):
	if nombre_tabla == "usuario":
		id = getMaxID(Usuario,'id')
		nombre = request.form["nombre"]
		apellido = request.form["apellido"]
		correo = request.form["correo"]
		contraseña = request.form["contraseña"]
		pais=request.form["pais"]
		Usuario.create(Usuario,id,nombre,apellido,correo,contraseña,pais)
	elif nombre_tabla == "pais":
		cod_pais = getMaxID(Country,'cod_pais')
		nombre = request.form["nombre"]
		Country.create(Country,cod_pais,nombre)
	elif nombre_tabla == "moneda":
		id = getMaxID(Moneda,'id')
		sigla = request.form["sigla"]
		nombre = request.form["nombre"]
		Moneda.create(Moneda,id,sigla,nombre)
	elif nombre_tabla == "precio_moneda":# posible error
		id_moneda = request.form["id_moneda"]
		valor = request.form["valor"]
		Precio_moneda.create(Precio_moneda,id_moneda,valor)
	elif nombre_tabla == "cuenta_bancaria":# posible error
		numero_cuenta = getMaxID(Cuenta_bancaria,'numero_cuenta')
		id_usuario = request.form["id_usuario"]
		balance = request.form["balance"]
		Cuenta_bancaria.create(Cuenta_bancaria,numero_cuenta,id_usuario,balance)
	elif nombre_tabla == "usuario_tiene_moneda":# posible error
		id_usuario = request.form["id_usuario"]
		id_moneda = request.form["id_moneda"]
		balance = request.form["balance"]
		
		Usuario_tiene_moneda.create(Usuario_tiene_moneda,id_usuario,id_moneda,balance)
	
	return redirect('/api/'+nombre_tabla)

# Rutas para consultas
@app.route('/api/consulta-<num_consulta>', methods=['GET'])	
def responderConsultas(num_consulta):
	data = []
	if num_consulta == '1':
		datos = [2015,2016,2017,2018,2019,2020,2021]
		data = [0]
	elif num_consulta == '3':
		datos = [ fila.json() for fila in Country.query.all()]
	elif num_consulta == '4' or num_consulta == '5':
		datos = [ fila.json() for fila in Moneda.query.all() ]
	elif num_consulta == '7':
		datos = [[1,2,3,4,5,6,7,8,9,10,11,12],[2015,2016,2017,2018,2019,2020,2021]]
		data = [0,0]
	elif num_consulta == '8':
		datos = [ fila.json() for fila in Usuario.query.order_by(Usuario.id).all()]
	else:
		datos = []
	return render_template('consultas.html',num_consulta=num_consulta, datos=datos,data=data, result=False)

@app.route('/api/consulta-<num_consulta>/execute', methods=['POST','GET'])
def get_custom(num_consulta):
	datos = []
	if num_consulta == '1': 
		datos = [2015,2016,2017,2018,2019,2020,2021]
		year = request.form["consulta_1"]
		data = year
		result = [dict(result) for result in Consulta.consulta_1(year=year).fetchall()]
	elif num_consulta == '2': 
		valor = request.form["consulta_2"]
		result = [dict(result) for result in Consulta.consulta_2(valor=valor).fetchall()]
		lista = [] 
		data = valor
		for elem in result:
			dicc = {}
			dicc["Id Cuenta"]=int(elem['Id Cuenta'])
			dicc["Balance"]=float(elem['Balance'])
			lista.append(dicc)
		result = lista
	elif num_consulta == '3':
		pais = request.form["consulta_3"]
		data = pais
		datos = [ fila.json() for fila in Country.query.all() ]
		result = [dict(result) for result in Consulta.consulta_3(pais=pais).fetchall()]
	elif num_consulta == '4':
		datos = [ fila.json() for fila in Moneda.query.all() ]
		moneda = request.form["consulta_4"]
		data = moneda
		result = [dict(result) for result in Consulta.consulta_4(moneda=moneda).fetchall()]
		lista = [] 
		for elem in result:
			dicc = {}
			dicc["Nombre"]=elem['Nombre']
			dicc["Valor Máximo"]=float(elem["Valor Máximo"])
			lista.append(dicc)
		result = lista
	elif num_consulta == '5':
		sigla = request.form["consulta_5"]
		data = sigla
		result = [dict(result) for result in Consulta.consulta_5(sigla=sigla).fetchall()]
		lista = [] 
		datos = [ fila.json() for fila in Moneda.query.all() ]
		for elem in result:
			dicc = {}
			dicc["Moneda"]=elem["Moneda"]
			dicc["Cantidad Total"]=float(elem['Cantidad Total'])
			lista.append(dicc)
			result = lista
	elif num_consulta == '6':
		data = []
		result = [dict(result) for result in Consulta.consulta_6().fetchall()]
	elif num_consulta == '7':
		mes = request.form["consulta_7_mes"]
		year = request.form["consulta_7_year"]
		datos = [[1,2,3,4,5,6,7,8,9,10,11,12],[2015,2016,2017,2018,2019,2020,2021]]
		data = [mes,year]
		result = [dict(result) for result in Consulta.consulta_7(mes=mes,year=year).fetchall()]
	elif num_consulta == '8':
		user = request.form["consulta_8"]
		result = [dict(result) for result in Consulta.consulta_8(user=user).fetchall()]
		data = user
		datos = [ fila.json() for fila in Usuario.query.order_by(Usuario.id).all()]
		for elem in result:
			for atr in elem:
				if atr == 'max':
					elem['max']=float(elem['max'])
	valores = []
	k = []
	try:
		for c in result[0].keys():
			
			k.append(c)
	except:
		k = []
		
	valores.append(k)
	valores.append(result)
	return render_template('consultas.html',num_consulta=num_consulta, datos=datos, data=data, result=True, valores=valores)
		



	
	

if __name__ == '__main__':
	app.run(debug=True)
