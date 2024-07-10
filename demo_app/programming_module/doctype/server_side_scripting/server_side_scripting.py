# Copyright (c) 2024, Narender and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document


class ServerSideScripting(Document):
    
	pass




#  *********************************************************  Server Side Call  *********************************************************
# ---------------------------------------------------------- js ---------------------------------------------------------------------
	# enable: function(frm) {
	# 		frm.call({
	# 			doc: frm.doc,
	# 			method: 'frm_call',
	# 			args: {
	# 				msg: "Hello"
	# 			},
	# 			freeze: true,
	# 			freeze_message: __('Calling frm_call Method'),
	# 			callback: function(r) {
	# 				frappe.msgprint(r.message)
					
	# 				// frappe.msgprint("Server Side calling Compleated")

	# 				// frm.refresh_field('medication_orders');
	# 			}
	# 		});
	# 	}
########## py 

	# @frappe.whitelist()
	# def frm_call(self,msg):
	# 	import time
	# 	time.sleep(5)
		# frappe.msgprint(msg)

		# self.mob_no= 77677656

		# return "Hi This Message from frm_call"
        


#  *********************************************************  Server Side Call end  *********************************************************




# ********************************************************* Server Side Call ************************************************************
# ---------------------------------------------------------         js      --------------------------------------------------------------	
	# enable: function(frm) {
	# 		frappe.call({
	# 			method: "demo_app.programming_module.doctype.server_side_scripting.server_side_scripting.frappe_call",
	# 			args: {
	# 				msg: "Hello"
	# 			},
	# 			freeze: true,
	# 			freeze_message: __('Calling frappe_call Method'),
	# 			callback: function(r) {
	# 				frappe.msgprint(r.message)
	# 			}
	# 		});
	# 	}

########## py 
# @frappe.whitelist()
# def frappe_call(msg):
# 	# import time
# 	# time.sleep(5)
# 	# frappe.msgprint(msg)

# 	return "Hi This Message from frappe_call"


# ********************************************************* Server Side Call end ************************************************************
 


# 1.. *************************************** Server Side Event ***************************************
	
	
	# def validate(self):
	# 	frappe.msgprint("Hello Namaste! This is a custom message from Server Side Scripting.")



	# def before_save(self):
	# 	frappe.throw("Hello Frappe From 'befor_save' Before Save Event")

	# def before_insert(self):
	# 	frappe.throw("Hello Frappe From 'befor_insert' Before Insert Event")


	# def after_insert(self):
	# 	frappe.throw("Hello Frappe From 'after_insert' After Insert Event")
	
	# def before_submit(self):
	# 	frappe.msgprint("Hello Frappe From 'before_submit' Before Submit Event")
    

	# def on_update(self):
	# 	frappe.msgprint("Hello Frappe From 'on_update' On Update Event")
    

	# def on_cancel(self):
	# 	frappe.msgprint("Hello Frappe From 'on_cancel' On Cancel Event")
    

	# def on_submit(self):
	# 	frappe.msgprint("Hello Frappe From 'on_submit' On Submit Event")

	# def on_trash(self):
	# 	frappe.msgprint("Hello Frappe From 'on_trash' On Trash Event")
    

	# def on_change(self):
	# 	frappe.msgprint("Hello Frappe From 'on_change' On Change Event")
    

	# def on_rename(self):
	# 	frappe.msgprint("Hello Frappe From 'on_rename' On Rename Event")
    

	# def after_delete(self):
	# 	frappe.msgprint("Hello Frappe From 'after_delete' After Delete Event")	


	




#     def vaildate(self):
# 	frappe.msgprint("Hello Namaste! This is a custom message from Server Side Scripting.")




# *************************************** Server Side Event end ***************************************



# *************************************** Value fetching ***************************************


	# def validate(self):
	# 	frappe.msgprint(_("Hello My Full Name is '{0}' ").format(
	#         self.first_name+" "+self.middle_name+" "+self.laste_name))
		


# def validate(self):
# 	for row in self.get('table_1'):
# 		frappe.msgprint(_(
# 			"{0}. Hello My Full Name is '{1}' and relation is '{2}' ").format(
# 		     row.idx,row.name1, row.relation))



#  *************************************** Value fetching end ***************************************


#  ************************************** frappe.get_doc(doctype, name) **************************************



	# frappe.get_doc(doctype, name)

	# def validate(self):
	# 	self.get_documnet()

	# def get_documnet(self):
	# 	doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
	# 	frappe.msgprint(_("Hello My Full Name is '{0}'  and Age is {1}").format(
	# 		doc.first_name, doc.age))
		

	# 	for row in doc.get("family_member"):
	# 		frappe.msgprint(_(
	# 			"{0}. Hello My Full Name is '{1}' and relation is '{2}' ").format(
	# 			row.idx,row.name1, row.relation))


	# ************************************** frappe.get_doc(doctype, name) end **************************************	



	# ************************************frappe.new_doc(doc_type)************************************
#4..................................... ''' create a new Document '''  .............................................

# frappe.new_doc(doctype)
	
	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Thakur'
	# 	doc.last_name = 'Shab'
	# 	doc.age = 21
	# 	doc.append("family_members",{   "name1":"Sonu",
	# 									"relation":"Friend",
	# 									"age":21
	# 								})
	# 	doc.insert()

# ************************************frappe.new_doc(doc_type) end************************************


# 5..************************************* frappe.delete_doc(doctype, name)*************************************
# frappe.delete_doc(doctype, name)

	# def validate(self):
	# 	frappe.delete_doc('Client Side Scripting', '15')


# 5..************************************* frappe.delete_doc(doctype, name) end*************************************	


# 6..**************************************** Document Methods *****************************************

#### doc.insert()

	# def validate(self):
	# 	self.new_document()

	# def new_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Ravi'
	# 	doc.age = 26
	# 	doc.insert()
	

	# some escape hatches that can be used to skip certain checks
	# doc.insert(
	#     ignore_permissions=True, # ignore write permissions during insert
	#     ignore_links=True, # ignore Link validation in the document
	#     ignore_if_duplicate=True, # dont insert if DuplicateEntryError is thrown
	#     ignore_mandatory=True # insert even if mandatory fields are not set
	# )

##### doc.save()

	# def validate(self):
	# 	self.save_document()

	# def save_document(self):
	# 	doc = frappe.new_doc('Client Side Scripting')
	# 	doc.first_name = 'Harendar'
	# 	doc.age = 24
	# 	doc.save()

	# 	doc.save(
	#     ignore_permissions=True, # ignore write permissions during insert
	#     ignore_version=True # do not create a version record
	# )

# doc.delete()

	# def validate(self):
	# 	self.delete_document()

	# def delete_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', '17')
	# 	doc.delete()

# doc.db_set()

	# def validate(self):
	# 	self.db_set_document()

	# def db_set_document(self):
	# 	doc = frappe.get_doc('Client Side Scripting', 'PR-0013')
	# 	doc.db_set('age', 45)


# 6..**************************************** Document Methods end *****************************************	



# 7.. ***************************************** Database API *****************************************

# frappe.db.get_list(doctype, filters, or_filters, fields, order_by, group_by, start, page_length)

	# def validate(self):
	# 	self.get_list()

	# def get_list(self):
	# 	doc = frappe.db.get_list('Client Side Scripting',
	# 			filters={
	# 				'enable': 1
	# 			},
	# 			fields=['first_name', 'age']
	# 			)
	# 	for d in doc:
	# 		frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))


#  7.. ***************************************** Database API end *****************************************

#  8..******************************************************************************************

# frappe.db.get_value(doctype, name, fieldname) or frappe.db.get_value(doctype, filters, fieldname)

	# def validate(self):
	# 	self.get_value()

	# def get_value(self):
	# 	first_name, age = frappe.db.get_value('Client Side Scripting', '18', ['first_name', 'age'])
	# 	frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(first_name,age))





#  8..******************************************************************************************



# 9..******************************************************************************************

# frappe.db.set_value(doctype, name, fieldname, value)
	
	# def validate(self):
	# 	self.set_value()

	# def set_value(self):
	# 	frappe.db.set_value('Client Side Scripting', '18', 'age', 24)

	# 	first_name, age = frappe.db.get_value('Client Side Scripting', '22', ['first_name', 'age'])
	# 	frappe.msgprint(_("The Parent First Name is {0} and new age is {1}").format(first_name,age))

# 9..******************************************************************************************


#  10..******************************************************************************************

# frappe.db.exists(doctype, name)
	
	# def validate(self):
	# 	if frappe.db.exists('Client Side Scripting', '18'): # True
	# 		frappe.msgprint(_("The Document is Exists in Database"))	
	# 	else:
	# 		frappe.msgprint(_("The Document does not Exists in Database"))	


#  10..******************************************************************************************


# 11..******************************************************************************************


# frappe.db.count(doctype, filters)
	
	# def validate(self):
	# 	doc_count = frappe.db.count('Client Side Scripting', {'enable': 1}) # True
	# 	frappe.msgprint(_("The Enable Document Count is {0}").format(doc_count))


# 11..******************************************************************************************


# 12..******************************************************************************************

# # frappe.db.sql(query, filters, as_dict)

	# def validate(self):
	# 	self.sql()

	# def sql(self):

	# 	data = frappe.db.sql("""
	# 							SELECT
	# 								first_name,
	# 								age
	# 							FROM 
	# 								`tabClient Side Scripting` 
	# 							WHERE 
	# 								enable = 1
	# 						""", as_dict=1)

	# 	for d in data:
	# 		frappe.msgprint(_("The Parent First Name is {0} and age is {1}").format(d.first_name,d.age))



# 12..******************************************************************************************


# 13..**************************************Start****************************************************


# frm.call method

	# def list_all_parent_docs(self,doctype):
		
	# 	data = frappe.get_all(doctype,fields=["*"])

	# 	for d in data:
	# 		self.append("parent_list",{
	# 			"full_name":d.full_name,
	# 			"age":d.age
	# 		})



# 13..****************************************End**************************************************




# 14..**************************************Start****************************************************

# call method  through hooks.py(programming app hook file)
	
	# def validate(self):
	# 	self.hook_call_method()

	# def hook_call_method(doc, method=None):
	# 	frappe.msgprint("Hello Frappe from hooks.py Document Events")





# 14..****************************************End**************************************************





# 15..**************************************Start****************************************************



# Scheduled Tasks 
# note: 


# def scheduled_tasks():
# 	frappe.msgprint(_("The Document dds dfdff is Exists in Database"))	

	# frappe.msgprint("Hello Frappe from hooks.py Scheduled Tasks")


# 15..****************************************End**************************************************
