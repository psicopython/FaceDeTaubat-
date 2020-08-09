from . import db, ma

from datetime import datetime



class ImgPost(db.Model):
	
	__tablename__='imgPost'
	
	id = db.Column(db.Integer,primary_key=True)
	id_post = db.Column(db.Integer,db.ForeignKey('post.id'),nullable=False)
	data_upl = db.Column(db.DateTime,default=datetime.utcnow(),nullable=False)
	imagem_dt = db.Column(db.BLOB,nullable=False)
	post = db.relationship('Post')
	
	
	def __init__(self,id_post,imagem):
		self.id_post = id_post
		self.imagem_dt = imagem.read()
		


class ImgPostSchema(ma.SQLAlchemyAutoSchema):
	class Meta:
		model = ImgPost
		include_fk = True



imgSchema = ImgPostSchema()
imgs_Schema = ImgPostSchema(many=True)