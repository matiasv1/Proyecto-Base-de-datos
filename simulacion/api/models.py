from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship, selectin_polymorphic

db = SQLAlchemy()

# Tabla usuario
class Usuario(db.Model):
	__tablename__= 'usuario'
	id=db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False)
	apellido = db.Column(db.String(50), nullable=False)
	correo = db.Column(db.String(50), nullable=False)
	contraseña = db.Column(db.String(100), nullable=False)
	pais= db.Column(db.Integer, db.ForeignKey('pais.cod_pais'))
	fecha_registro = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp())
	cuenta_bancaria = db.relationship('Cuenta_bancaria',cascade="all,delete", lazy='dynamic')
	relacion_Usuario_tiene_moneda = db.relationship('Usuario_tiene_moneda',cascade="all,delete", lazy='dynamic')
	name_id=["id"]
	@classmethod
	def getID(self):
		return self.name_id
	def jsonColumnMod():
		return ['nombre','apellido','correo','contraseña','pais']
	def create(cls,id,nombre, apellido, correo, contraseña, pais):
		user = Usuario(id=id,nombre=nombre,apellido=apellido,correo=correo,contraseña=contraseña,pais=pais)
		return user.save()
	def json(self):
		return {'id':self.id,
			'nombre':self.nombre,
			'apellido':self.apellido,
			'correo':self.correo,
			'contraseña':self.contraseña,
			'pais':self.pais}
	def update(self):
		self.save()	
	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False	
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()
			return True
		except:
			return False

# Tabla pais
class Country(db.Model):
	__tablename__= 'pais'
	cod_pais=db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(50), nullable=False)
	user = db.relationship('Usuario', lazy='dynamic')
	name_id = ["cod_pais"]
	@classmethod
	def getID(self):
		return self.name_id
	def jsonColumnMod():
		return ['nombre']
	def create(cls, cod_pais, nombre):
		country = Country(cod_pais=cod_pais, nombre=nombre)
		return country.save()
	def json(self):
		return {
			'cod_pais': self.cod_pais,
			'nombre': self.nombre
		}
	def update(self):
		self.save()	
	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False	
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()
			return True
		except:
			return False
# Tabla precio_moneda
class Precio_moneda(db.Model):
	__tablename__= 'precio_moneda'
	id_moneda = db.Column(db.Integer,db.ForeignKey('moneda.id'),nullable=False,primary_key=True)
	fecha = db.Column(db.DateTime(), nullable=False, default=db.func.current_timestamp(),primary_key=True)
	valor = db.Column(db.Float,  nullable=False)
	name_id = ["id_moneda","fecha"]
	@classmethod
	def getID(self):
		return self.name_id
	def jsonColumnMod():
		return ['id_moneda','valor']
	def create(cls, id_moneda,valor):
		precio_moneda = Precio_moneda(id_moneda=id_moneda,valor=valor)
		return precio_moneda.save()
	def json(self):
		return {
			'id_moneda': self.id_moneda,
			'fecha': self.fecha,
			'valor': self.valor
		}
	def update(self):
		self.save()	
	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False	
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()
			return True
		except:
			return False

# Tabla moneda
class Moneda(db.Model):
	__tablename__= 'moneda'
	id = db.Column(db.Integer,primary_key=True)
	sigla = db.Column(db.String(10),nullable=False)
	nombre = db.Column(db.String(80),nullable=False)
	relacion_Precio_moneda = db.relationship('Precio_moneda',cascade="all,delete", lazy='dynamic')
	relacion_Usuario_tiene_moneda = db.relationship('Usuario_tiene_moneda',cascade="all,delete",  lazy='dynamic')
	name_id = ["id"]
	@classmethod
	def getID(self):
		return self.name_id
	def jsonColumnMod():
		return ['sigla','nombre']
	def create(cls, id,sigla,nombre):
		moneda = Moneda(id=id,sigla=sigla,nombre=nombre)
		return moneda.save()
	def json(self):
		return {
			'id': self.id,
			'sigla': self.sigla,
			'nombre': self.nombre
		}
	def update(self):
		self.save()	
	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False	
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()
			return True
		except:
			return False

	
# Tabla cuenta_bancaria
class Usuario_tiene_moneda(db.Model):
	__tablename__='usuario_tiene_moneda'
	id_usuario=db.Column(db.Integer,db.ForeignKey('usuario.id'), primary_key=True)
	id_moneda=db.Column(db.Integer,db.ForeignKey('moneda.id'), primary_key=True)
	balance=db.Column(db.Float, nullable=False)
	name_id = ["id_usuario","id_moneda"]
	@classmethod
	def getID(self):
		return self.name_id
	def jsonColumnMod():
		return ["id_usuario","id_moneda",'balance']
	def json(self):
		return {
			'id_usuario': self.id_usuario,
			'id_moneda': self.id_moneda,
			'balance': self.balance
		}
	def create(cls, id_usuario,id_moneda,balance):
		utm = Usuario_tiene_moneda(id_usuario=id_usuario,id_moneda=id_moneda,balance=balance)
		return utm.save()
	def update(self):
		self.save()	
	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False	
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()
			return True
		except:
			return False
# Tabla cuenta_bancaria
class Cuenta_bancaria(db.Model):
	__tablename__='cuenta_bancaria'
	numero_cuenta=db.Column(db.Integer, primary_key=True)
	id_usuario=db.Column(db.Integer,db.ForeignKey('usuario.id'))
	balance=db.Column(db.Float, nullable=False)
	name_id = ["numero_cuenta"]
	@classmethod
	def getID(self):
		return self.name_id
	def jsonColumnMod():
		return ['id_usuario','balance']
	def create(cls, numero_cuenta,id_usuario,balance):
		country= Cuenta_bancaria(numero_cuenta=numero_cuenta,id_usuario=id_usuario,balance=balance)
		return country.save()
	def json(self):
		return {
            'numero_cuenta': self.numero_cuenta,
            'id_usuario': self.id_usuario,
            'balance': self.balance
			}
	def update(self):
		self.save()
	def save(self):
		try:
			db.session.add(self)
			db.session.commit()
			return self
		except:
			return False
	def delete(self):
		try:
			db.session.delete(self)
			db.session.commit()
			return True
		except:
			return False

class Consulta():
	def consulta_1(year):
		try:
			result = db.session.execute('SELECT usuario.nombre as "Nombre", usuario.apellido as "Apellido", DATE(fecha_registro) as "Fecha de Registro" FROM usuario WHERE EXTRACT(YEAR FROM (DATE(usuario.fecha_registro))) = {0};'.format(year))
			return result
		except:
			return False
	def consulta_2(valor):
		try:
			result = db.session.execute('SELECT cuenta_bancaria.numero_cuenta as "Id Cuenta", cuenta_bancaria.balance as "Balance" FROM cuenta_bancaria WHERE cuenta_bancaria.balance > {0} and cuenta_bancaria.numero_cuenta is NOT NULL and cuenta_bancaria.balance is NOT NULL;'.format(valor))
			return result
		except:
			return False
	def consulta_3(pais): 
		try:
			result = db.session.execute("SELECT pais.nombre as \"País\", usuario.nombre as \"Nombre\", usuario.apellido as \"Apellido\" FROM usuario inner join pais on pais.cod_pais=usuario.pais WHERE pais.nombre ='{0}';".format(pais))
			return result
		except:
			return False
	def consulta_4(moneda):
		try:
			result = db.session.execute("SELECT moneda.nombre as \"Nombre\", MAX (precio_moneda.valor) as \"Valor Máximo\" FROM moneda INNER JOIN precio_moneda ON moneda.id = precio_moneda.id_moneda WHERE moneda.nombre = '{0}' GROUP BY moneda.nombre;".format(moneda))
			return result
		except:
			return False
	def consulta_5(sigla):
		try:
			result = db.session.execute("SELECT moneda.sigla as \"Moneda\", SUM(usuario_tiene_moneda.balance) as \"Cantidad Total\" FROM usuario_tiene_moneda LEFT JOIN moneda ON usuario_tiene_moneda.id_moneda = moneda.id WHERE moneda.sigla = '{0}' GROUP BY moneda.sigla;".format(sigla))
			return result
		except:
			return False
	def consulta_6():
		try:
			result = db.session.execute("SELECT moneda.nombre as \"Nombre\", COUNT(moneda.id) as \"Cantidad Usuarios\" From moneda INNER JOIN usuario_tiene_moneda ON moneda.id = usuario_tiene_moneda.id_moneda GROUP BY moneda.nombre ORDER BY COUNT(moneda.id) DESC LIMIT 3;")
			return result
		except:
			return False
	def consulta_7(mes,year):
		try:
			result = db.session.execute("SELECT moneda.nombre as \"Moneda\", count(valor) as \"Veces que cambió valor\"FROM moneda INNER JOIN  precio_moneda ON moneda.id=precio_moneda.id_moneda WHERE EXTRACT(MONTH FROM (DATE(precio_moneda.fecha))) = '{0}' and EXTRACT(YEAR FROM (DATE(precio_moneda.fecha))) = '{1}' GROUP BY moneda.nombre ORDER BY count(valor) DESC LIMIT 1;".format(mes,year))
			return result
		except:
			return False
	def consulta_8(user):
		try:
			result = db.session.execute("SELECT usuario.nombre as \"Nombre\", usuario.apellido as \"Apellido\", moneda.nombre as \"Nombre Moneda\", MAX(usuario_tiene_moneda.balance) as \"Cantidad\" FROM usuario INNER JOIN usuario_tiene_moneda ON usuario.id = usuario_tiene_moneda.id_usuario INNER JOIN moneda ON usuario_tiene_moneda.id_moneda = moneda.id WHERE usuario.id = {0} GROUP BY usuario.nombre, usuario.apellido, moneda.id ORDER BY MAX(usuario_tiene_moneda.balance) DESC LIMIT 1;".format(user))
			return result
		except:
			return False

	
	