import frappe, psutil, time, platform, os, datetime

global desctable

@frappe.whitelist()
def get_sales_order(**kwargs):
	res = frappe._dict({})
	if not ('System Manager' in [i.role for i in frappe.get_doc('User', frappe.session.user).roles]):
		return res
	
	doc = frappe.db.get_list('Sales Order', 
		filters={
			'status': 'Draft'
		},
		fields=['customer', 'customer_name'],
		as_list=True
	)
	desctable = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html", context=dict(customer="asd", customer_name="qwe"))

	#for d in doc:
	#	desctable = frappe.render_template(
	#		"sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html",
	#		context=dict(
	#		customer = {0},
	#		customer_name = {1},
	#	)).format(d.customer, d.customer_name)

	res.desctable = desctable
	return res
