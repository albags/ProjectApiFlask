from flask import Flask 
from flask import g 
from flask import jsonify
from flask import abort
from flask import render_template

from models import ActionTypes
from models import Activities
from models import Assays
from models import ComponentClass
from models import ComponentSequences
from models import ComponentSynonyms
from models import CompoundRecord
from models import CompoundStructures
from models import DrugIndication
from models import DrugMechanism
from models import Formulations
from models import IndicationRefs
from models import MoleculeDictionary
from models import Products
from models import ProteinClassification
from models import TargetClass
from models import TargetComponents
from models import TargetDictionary
from models import TargetType

from models import DATABASE

app = Flask(__name__)
PORT = 5000
DEBUG = True
HOST = '0.0.0.0'

# define the data loop
loopDataOptions = ['data/action_type/', 'data/action_type/:ACTION_TYPE', 'data/activities/', 'data/activities/:ID', 'data/assays/', 'data/assays/:ID', 'data/component_class/', 
'data/component_class/:ID', 'data/component_sequences/', 'data/component_sequences/:ID', 'data/component_synonyms/', 'data/component_synonyms/:ID', 'data/component_record/', 
'data/component_record/:ID', 'data/compound_structures/', 'data/compound_structures/:MOLREGNO', 'data/drug_indication/', 'data/drug_indication/:ID', 'data/drug_mechanism/', 
'data/drug_mechanism/:ID', 'data/formulations/', 'data/formulations/:ID', 'data/indication_refs/', 'data/indication_refs/:ID', 'data/molecule_dictionary/', 
'data/molecule_dictionary/:MOLREGNO', 'data/products/', 'data/products/:TRADE_NAME', 'data/products/:ID', 'data/protein_classification/', 'data/protein_classification/:ID', 
'data/target_class/', 'data/target_class/:ID', 'data/target_components/', 'data/target_components/:ID', 'data/target_dictionary/', 'data/target_dictionary/:ID', 'data/target_type/', 
'data/target_type/:TARGET_TYPE']

@app.before_request
def before_request():
	g.db = DATABASE
	g.db.get_conn()

@app.after_request
def after_request(request):
	g.db.close()
	return request

@app.errorhandler(404)
def not_found(error):
	return jsonify(generate_response(404, error='Register not found.'))

@app.route('/', methods=['GET'])
def index():
	return render_template("index.html", options=loopDataOptions)

@app.route('/api/data/action_type/', methods=['GET'])
def getActionType():
	action_types = ActionTypes.select()
	action_types = [action_type.to_json() for action_type in action_types]
	return jsonify(generate_response(data=action_types, nameDB="action_type"))

@app.route('/api/data/action_type/<string:action_type>', methods=['GET'])
def getActionTypeByAction(action_type):
	action_type = try_action_type(action_type)
	return jsonify(generate_response(data=action_type.to_json(), nameDB="action_type"))

@app.route('/api/data/activities/', methods=['GET'])
def getActivities():
	activities = Activities.select()
	activities = [activity.to_json() for activity in activities]
	return jsonify(generate_response(data=activities, nameDB="activities"))

@app.route('/api/data/activities/<int:activity_id>', methods=['GET'])
def getActivitiesById(activity_id):
	activity = try_activity(activity_id)
	return jsonify(generate_response(data=activity.to_json(), nameDB="activities"))

@app.route('/api/data/assays/', methods=['GET'])
def getAssays():
	assays = Assays.select()
	assays = [assay.to_json() for assay in assays]
	return jsonify(generate_response(data=assays, nameDB="assays"))

@app.route('/api/data/assays/<int:assay_id>', methods=['GET'])
def getAssaysById(assay_id):
	assay = try_assay(assay_id)
	return jsonify(generate_response(data=assay.to_json(), nameDB="assays"))

@app.route('/api/data/component_class/', methods=['GET'])
def getcomponent_class():
	component_class = ComponentClass.select()
	component_class = [component.to_json() for component in component_class]
	return jsonify(generate_response(data=component_class, nameDB="component_class"))

@app.route('/api/data/component_class/<int:comp_class_id>', methods=['GET'])
def getcomponent_classById(comp_class_id):
	component = try_component_class(comp_class_id)
	return jsonify(generate_response(data=component.to_json(), nameDB="component_class"))

@app.route('/api/data/component_sequences/', methods=['GET'])
def getComponentSequences():
	component_sequences = ComponentSequences.select()
	component_sequences = [sequence.to_json() for sequence in component_sequences]
	return jsonify(generate_response(data=component_sequences, nameDB="component_sequences"))

@app.route('/api/data/component_sequences/<int:component_id>', methods=['GET'])
def getComponentSequencesById(component_id):
	component = try_component_sequences(component_id)
	return jsonify(generate_response(data=component.to_json(), nameDB="component_sequences"))

@app.route('/api/data/component_synonyms/', methods=['GET'])
def getComponentSynonyms():
	component_synonyms = ComponentSynonyms.select()
	component_synonyms = [synonyms.to_json() for synonyms in component_synonyms]
	return jsonify(generate_response(data=component_synonyms, nameDB="component_synonyms"))

@app.route('/api/data/component_synonyms/<int:compsyn_id>', methods=['GET'])
def getComponentSynonymsById(compsyn_id):
	synonym = try_component_synonyms(compsyn_id)
	return jsonify(generate_response(data=synonym.to_json(), nameDB="component_synonyms"))

@app.route('/api/data/component_record/', methods=['GET'])
def getCompoundRecord():
	component_record = CompoundRecord.select()
	component_record = [record.to_json() for record in component_record]
	return jsonify(generate_response(data=component_record, nameDB="component_record"))

@app.route('/api/data/component_record/<int:record_id>', methods=['GET'])
def getCompoundRecordById(record_id):
	record = try_compound_record(record_id)
	return jsonify(generate_response(data=record.to_json(), nameDB="component_record"))

@app.route('/api/data/compound_structures/', methods=['GET'])
def getCompoundStructures():
	compound_structures = CompoundStructures.select()
	compound_structures = [record.to_json() for record in compound_structures]
	return jsonify(generate_response(data=compound_structures, nameDB="compound_structures"))

@app.route('/api/data/compound_structures/<int:molregno>', methods=['GET'])
def getCompoundStructuresById(molregno):
	compoundStructure = try_compound_structures(molregno)
	return jsonify(generate_response(data=compoundStructure.to_json(), nameDB="compound_structures"))

@app.route('/api/data/drug_indication/', methods=['GET'])
def getDrugIndication():
	drug_indication = DrugIndication.select()
	drug_indication = [indication.to_json() for indication in drug_indication]
	return jsonify(generate_response(data=drug_indication, nameDB="drug_indication"))

@app.route('/api/data/drug_indication/<int:drugind_id>', methods=['GET'])
def getDrugIndicationById(drugind_id):
	indication = try_drug_indication(drugind_id)
	return jsonify(generate_response(data=indication.to_json(), nameDB="drug_indication"))

@app.route('/api/data/drug_mechanism/', methods=['GET'])
def getDrugMechanism():
	drug_mechanism = DrugMechanism.select()
	drug_mechanism = [mechanism.to_json() for mechanism in drug_mechanism]
	return jsonify(generate_response(data=drug_mechanism, nameDB="drug_mechanism"))

@app.route('/api/data/drug_mechanism/<int:mec_id>', methods=['GET'])
def getDrugMechanismById(mec_id):
	mechanism = try_drug_mechanism(mec_id)
	return jsonify(generate_response(data=mechanism.to_json(), nameDB="drug_mechanism"))

@app.route('/api/data/formulations/', methods=['GET'])
def getFormulations():
	formulations = Formulations.select()
	formulations = [formulation.to_json() for formulation in formulations]
	return jsonify(generate_response(data=formulations, nameDB="formulations"))

@app.route('/api/data/formulations/<string:formulation_id>', methods=['GET'])
def getFormulationsByProduct(formulation_id):
	formulation = try_formulations(formulation_id)
	return jsonify(generate_response(data=formulation.to_json(), nameDB="formulations"))

@app.route('/api/data/indication_refs/', methods=['GET'])
def getIndicationRefs():
	indication_refs = IndicationRefs.select()
	indication_refs = [indication.to_json() for indication in indication_refs]
	return jsonify(generate_response(data=indication_refs, nameDB="indication_refs"))

@app.route('/api/data/indication_refs/<int:indref_id>', methods=['GET'])
def getIndicationRefsById(indref_id):
	indication = try_indication_refs(indref_id)
	return jsonify(generate_response(data=indication.to_json(), nameDB="indication_refs"))

@app.route('/api/data/molecule_dictionary/', methods=['GET'])
def getMoleculeDictionary():
	molecule_dictionary = MoleculeDictionary.select()
	molecule_dictionary = [molecule.to_json() for molecule in molecule_dictionary]
	return jsonify(generate_response(data=molecule_dictionary, nameDB="molecule_dictionary"))

@app.route('/api/data/molecule_dictionary/<int:molregno>', methods=['GET'])
def getMoleculeDictionaryById(molregno):
	molecule = try_molecule_dictionary(molregno)
	return jsonify(generate_response(data=molecule.to_json(), nameDB="molecule_dictionary"))

@app.route('/api/data/products/', methods=['GET'])
def getPoducts():
	products = Products.select()
	products = [molecule.to_json() for molecule in products]
	return jsonify(generate_response(data=products, nameDB="products"))

@app.route('/api/data/products/tradeName/<string:trade_name>', methods=['GET'])
def getProductsByTradeName(trade_name):
	product = try_products_trade_name(trade_name)
	return jsonify(generate_response(data=product.to_json(), nameDB="products"))

@app.route('/api/data/products/productId/<string:product_id>', methods=['GET'])
def getProductsByProductId(product_id):
	product = try_product_id(product_id)
	return jsonify(generate_response(data=product.to_json(), nameDB="products"))

@app.route('/api/data/protein_classification/', methods=['GET'])
def getProteinClassification():
	proteins = ProteinClassification.select()
	proteins = [protein.to_json() for protein in proteins]
	return jsonify(generate_response(data=proteins, nameDB="protein_classification"))

@app.route('/api/data/protein_classification/<int:protein_class_id>', methods=['GET'])
def getProteinClassificationById(protein_class_id):
	protein = try_protein_classification(protein_class_id)
	return jsonify(generate_response(data=protein.to_json(), nameDB="protein_classification"))

@app.route('/api/data/target_class/', methods=['GET'])
def getTargetClass():
	targets = TargetClass.select()
	targets = [target.to_json() for target in targets]
	return jsonify(generate_response(data=targets, nameDB="target_class"))

@app.route('/api/data/target_class/<int:target_class_id>', methods=['GET'])
def getTargetClassById(target_class_id):
	target = try_target_class(target_class_id)
	return jsonify(generate_response(data=target.to_json(), nameDB="target_class"))

@app.route('/api/data/target_components/', methods=['GET'])
def getTargetComponents():
	targets = TargetComponents.select()
	targets = [target.to_json() for target in targets]
	return jsonify(generate_response(data=targets, nameDB="target_components"))

@app.route('/api/data/target_components/<int:targcomp_id>', methods=['GET'])
def getTargetComponentsById(targcomp_id):
	target = try_target_components(targcomp_id)
	return jsonify(generate_response(data=target.to_json(), nameDB="target_components"))

@app.route('/api/data/target_dictionary/', methods=['GET'])
def getTargetDictionary():
	targets = TargetDictionary.select()
	targets = [target.to_json() for target in targets]
	return jsonify(generate_response(data=targets, nameDB="target_dictionary"))

@app.route('/api/data/target_dictionary/<int:tid>', methods=['GET'])
def getTargetDictionaryById(tid):
	target = try_target_dictionary(tid)
	return jsonify(generate_response(data=target.to_json(), nameDB="target_dictionary"))

@app.route('/api/data/target_type/', methods=['GET'])
def getTargetTypes():
	targets = TargetType.select()
	targets = [target.to_json() for target in targets]
	return jsonify(generate_response(data=targets, nameDB="target_type"))

@app.route('/api/data/target_type/<string:target_type>', methods=['GET'])
def getTargetTypesByTargetType(target_type):
	target = try_target_type(target_type)
	return jsonify(generate_response(data=target.to_json(), nameDB="target_type"))

def try_action_type(action):
	try:
		action_type = ActionTypes.get(ActionTypes.action_type == action)
		return action_type
	except ActionTypes.DoesNotExist:
		abort(404)

def try_activity(id):
	try:
		activity = Activities.get(Activities.activity_id == id)
		return activity
	except Activities.DoesNotExist:
		abort(404)

def try_assay(id):
	try:
		assay = Assays.get(Assays.assay_id == id)
		return assay
	except Assays.DoesNotExist:
		abort(404)

def try_component_class(id):
	try:
		component = component_class.get(component_class.comp_class_id == id)
		return component
	except component_class.DoesNotExist:
		abort(404)

def try_component_sequences(id):
	try:
		component = ComponentSequences.get(ComponentSequences.component_id == id)
		return component
	except ComponentSequences.DoesNotExist:
		abort(404)

def try_component_synonyms(id):
	try:
		synonym = ComponentSynonyms.get(ComponentSynonyms.compsyn_id == id)
		return synonym
	except ComponentSynonyms.DoesNotExist:
		abort(404)

def try_compound_record(id):
	try:
		record = CompoundRecord.get(CompoundRecord.record_id == id)
		return record
	except CompoundRecord.DoesNotExist:
		abort(404)

def try_compound_structures(id):
	try:
		structure = CompoundStructures.get(CompoundStructures.molregno == id)
		return structure
	except CompoundStructures.DoesNotExist:
		abort(404)

def try_drug_indication(id):
	try:
		indication = DrugIndication.get(DrugIndication.drugind_id == id)
		return indication
	except DrugIndication.DoesNotExist:
		abort(404)

def try_drug_mechanism(id):
	try:
		mechanism = DrugMechanism.get(DrugMechanism.mec_id == id)
		return mechanism
	except DrugMechanism.DoesNotExist:
		abort(404)

def try_formulations(formulation_id):
	try:
		formulation = Formulations.get(Formulations.formulation_id == formulation_id)
		return formulation
	except Formulations.DoesNotExist:
		abort(404)

def try_indication_refs(id):
	try:
		indication = IndicationRefs.get(IndicationRefs.indref_id == id)
		return indication
	except IndicationRefs.DoesNotExist:
		abort(404)

def try_molecule_dictionary(id):
	try:
		molecule = MoleculeDictionary.get(MoleculeDictionary.molregno == id)
		return molecule
	except MoleculeDictionary.DoesNotExist:
		abort(404)

def try_products_trade_name(trade_name):
	try:
		product = Products.get(Products.trade_name == trade_name)
		return product
	except Products.DoesNotExist:
		abort(404)

def try_product_id(product_id):
	try:
		product = Products.get(Products.product_id == product_id)
		return product
	except Products.DoesNotExist:
		abort(404)

def try_protein_classification(id):
	try:
		protein = ProteinClassification.get(ProteinClassification.protein_class_id == id)
		return protein
	except ProteinClassification.DoesNotExist:
		abort(404)

def try_target_class(id):
	try:
		target = TargetClass.get(TargetClass.target_class_id == id)
		return target
	except TargetClass.DoesNotExist:
		abort(404)

def try_target_components(id):
	try:
		target = TargetComponents.get(TargetComponents.targcomp_id == id)
		return target
	except TargetComponents.DoesNotExist:
		abort(404)

def try_target_dictionary(id):
	try:
		target = TargetDictionary.get(TargetDictionary.tid == id)
		return target
	except TargetDictionary.DoesNotExist:
		abort(404)

def try_target_type(target_type):
	try:
		target = TargetType.get(TargetType.target_type == target_type)
		return target
	except TargetType.DoesNotExist:
		abort(404)

def generate_response(status=200, data=None, error="OK", nameDB=None):
	return {'status':status, 'data':data, 'error':error, 'name':nameDB}

if __name__ == '__main__':
	app.run(host=HOST, port=PORT, debug=DEBUG)
