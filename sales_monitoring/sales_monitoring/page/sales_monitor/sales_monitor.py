import frappe, psutil, time, platform, os, datetime
from datetime import date


global desctable

@frappe.whitelist()
def get_sales_order(**kwargs):
	res = frappe._dict({})
	if not ('System Manager' in [i.role for i in frappe.get_doc('User', frappe.session.user).roles]):
		return res
	
	#doc = frappe.db.get_list('Sales Order', 
	#	filters={
	#		'status': 'Draft'
	#	},
	#	fields=['customer', 'customer_name'],
	#	as_dict=True
	#)

	doc = frappe.db.sql("""select name, customer, customer_name, transaction_date, grand_total, owner from `tabSales Order` where status = 0""", as_dict = True)

	if not doc:
		desctable = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html", {"nama": "SALES ORDER"})
		res.desctable = desctable
		return res

	desctable = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html", {"nama": "SALES ORDER", "document":doc})

	#for d in doc:
	#	desctable = frappe.render_template(
	#		"sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html",
	#		context=dict(
	#		customer = d.customer,
	#		customer_name = d.customer_name,
	#	))

	res.desctable = desctable
	return res


@frappe.whitelist()
def get_sales_invoice(**kwargs):
	today = date.today()
	res = frappe._dict({})
	if not ('System Manager' in [i.role for i in frappe.get_doc('User', frappe.session.user).roles]):
		return res

	doc = frappe.db.sql("""select name, customer, customer_name, posting_date, grand_total, owner from `tabSales Invoice` where posting_date = %s""", (today), as_dict = True)

	if not doc:
		invoices = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/invoices.html", {"nama": "SALES INVOICE"})
		res.invoices = invoices
		return res

	invoices = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/invoices.html", {"nama": "SALES INVOICE", "document":doc})

	res.invoices = invoices
	return res

