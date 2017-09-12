from peewee import *

DATABASE = MySQLDatabase('project_fda', host='database', user='user', passwd='userpwd')

class ActionTypes(Model):
	class Meta:
		database = DATABASE
		db_table = 'action_type'

	action_type = CharField(primary_key=True)
	description = TextField()

	def to_json(self):
		return {'action_type':self.action_type, 'description':self.description}

class Activities(Model):
	class Meta:
		database = DATABASE
		db_table = 'activities'

	activity_id = IntegerField(primary_key=True)
	assay_id = IntegerField()
	record_id = IntegerField()
	molregno = IntegerField()
	standard_value = FloatField()
	standard_units = TextField()
	standard_type = TextField()

	def to_json(self):
		return {'activity_id':self.activity_id, 'assay_id':self.assay_id, 'record_id':self.record_id, 'molregno':self.molregno, 'standard_value':self.standard_value, 
		'standard_units':self.standard_units, 'standard_type':self.standard_type}

class Assays(Model):
	class Meta:
		database = DATABASE
		db_table = 'assays'

	assay_id = IntegerField(primary_key=True)
	tid = IntegerField()

	def to_json(self):
		return {'assay_id':self.assay_id, 'tid':self.tid}

class ComponentClass(Model):
	class Meta:
		database = DATABASE
		db_table = 'component_class'

	comp_class_id = IntegerField(primary_key=True) 
	protein_class_id = IntegerField()
	component_id = IntegerField()

	def to_json(self):
		return {'comp_class_id':self.comp_class_id, 'protein_class_id':self.protein_class_id, 'component_id':self.component_id}

class ComponentSequences(Model):
	class Meta:
		database = DATABASE
		db_table = 'component_sequences'

	component_id = IntegerField(primary_key=True)
	accession = CharField()
	organism = TextField() 

	def to_json(self):
		return {'component_id':self.component_id, 'accession':self.accession, 'organism':self.organism}

class ComponentSynonyms(Model):
	class Meta:
		database = DATABASE
		db_table = 'component_synonyms'

	compsyn_id = IntegerField(primary_key=True)
	component_id = IntegerField()
	component_synonym = TextField() 

	def to_json(self):
		return {'compsyn_id':self.compsyn_id, 'component_id':self.component_id, 'component_synonym':self.component_synonym}

class CompoundRecord(Model):
	class Meta:
		database = DATABASE
		db_table = 'compound_record'

	record_id = IntegerField(primary_key=True)
	molregno = IntegerField()

	def to_json(self):
		return {'record_id':self.record_id, 'molregno':self.molregno}

class CompoundStructures(Model):
	class Meta:
		database = DATABASE
		db_table = 'compound_structures'

	molregno = IntegerField(primary_key=True)
	standard_inchi_key = CharField()
	canonical_smiles = TextField()

	def to_json(self):
		return {'molregno':self.molregno, 'standard_inchi_key':self.standard_inchi_key, 'canonical_smiles':self.canonical_smiles}

class DrugIndication(Model):
	class Meta:
		database = DATABASE
		db_table = 'drug_indication'

	drugind_id = IntegerField(primary_key=True)
	record_id = IntegerField()
	molregno = IntegerField()
	max_phase_for_ind = IntegerField()
	mesh_id = CharField()
	mesh_heading = TextField()
	efo_id = TextField()
	efo_term = TextField()

	def to_json(self):
		return {'drugind_id':self.drugind_id, 'record_id':self.record_id, 'molregno':self.molregno, 'max_phase_for_ind':self.max_phase_for_ind, 'mesh_id':self.mesh_id, 
		'mesh_heading':self.mesh_heading, 'efo_id':self.efo_id, 'efo_term':self.efo_term}

class DrugMechanism(Model):
	class Meta:
		database = DATABASE
		db_table = 'drug_mechanism'

	mec_id = IntegerField(primary_key=True)
	record_id = IntegerField()
	molregno = IntegerField()
	mechanism_of_action = TextField()
	tid = IntegerField()
	action_type = TextField()

	def to_json(self):
		return {'mec_id':self.mec_id, 'record_id':self.record_id, 'molregno':self.molregno, 'mechanism_of_action':self.mechanism_of_action, 'tid':self.tid, 
		'action_type':self.action_type}

class Formulations(Model):
	class Meta:
		database = DATABASE
		db_table = 'formulations'

	formulation_id = IntegerField(primary_key=True)
	record_id = IntegerField()
	product_id = CharField()
	molregno = IntegerField()

	def to_json(self):
		return {'formulation_id':self.formulation_id, 'product_id':self.product_id, 'record_id':self.record_id, 'molregno':self.molregno}

class IndicationRefs(Model):
	class Meta:
		database = DATABASE
		db_table = 'indication_refs'

	indref_id = IntegerField(primary_key=True)
	drugind_id = IntegerField()
	ref_type = CharField()
	ref_id = TextField()
	ref_url = TextField()

	def to_json(self):
		return {'indref_id':self.indref_id, 'drugind_id':self.drugind_id, 'ref_type':self.ref_type, 'ref_id':self.ref_id, 'ref_url':self.ref_url}

class MoleculeDictionary(Model):
	class Meta:
		database = DATABASE
		db_table = 'molecule_dictionary'

	molregno = IntegerField(primary_key=True)
	pref_name = TextField()
	chembl_id = CharField()
	indication_class = TextField()

	def to_json(self):
		return {'molregno':self.molregno, 'pref_name':self.pref_name, 'chembl_id':self.chembl_id, 'indication_class':self.indication_class}

class Products(Model):
	class Meta:
		database = DATABASE
		db_table = 'products'

	product_id = TextField(primary_key=True)
	trade_name = TextField()

	def to_json(self):
		return {'trade_name':self.trade_name, 'product_id':self.product_id}

class ProteinClassification(Model):
	class Meta:
		database = DATABASE
		db_table = 'protein_classification'

	protein_class_id = IntegerField(primary_key=True)
	pref_name = TextField()
	target_class_id = IntegerField()

	def to_json(self):
		return {'protein_class_id':self.protein_class_id, 'pref_name':self.pref_name, 'target_class_id':self.target_class_id}

class TargetClass(Model):
	class Meta:
		database = DATABASE
		db_table = 'target_class'

	target_class_id = IntegerField(primary_key=True)
	target_class = TextField()

	def to_json(self):
		return {'target_class_id':self.target_class_id, 'target_class':self.target_class}

class TargetComponents(Model):
	class Meta:
		database = DATABASE
		db_table = 'target_components'

	targcomp_id = IntegerField(primary_key=True)
	component_id = IntegerField()
	tid = IntegerField()

	def to_json(self):
		return {'tid':self.tid, 'component_id':self.component_id, 'targcomp_id':self.targcomp_id}

class TargetDictionary(Model):
	class Meta:
		database = DATABASE
		db_table = 'target_dictionary'

	tid = IntegerField(primary_key=True)
	target_type = CharField()
	pref_name = TextField()
	organism = TextField()
	chembl_id = CharField()

	def to_json(self):
		return {'tid':self.tid, 'target_type':self.target_type, 'pref_name':self.pref_name, 'organism':self.organism, 'chembl_id':self.chembl_id}

class TargetType(Model):
	class Meta:
		database = DATABASE
		db_table = 'target_type'

	target_type = CharField(primary_key=True)
	target_desc = TextField()

	def to_json(self):
		return {'target_type':self.target_type, 'target_desc':self.target_desc}








