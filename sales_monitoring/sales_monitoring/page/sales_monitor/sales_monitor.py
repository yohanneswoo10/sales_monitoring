import frappe, psutil, time, platform, os, datetime
from datetime import date


global desctable

@frappe.whitelist()
def get_sales_order(**kwargs):
	today = date.today()
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

	doc = frappe.db.sql("""select name, customer, customer_name, transaction_date, grand_total, owner, status from `tabSales Order` \
				where status != 'Cancelled' OR transaction_date = %s""", (today), as_dict = True)

	if not doc:
		desctable = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html", {"nama": "SALES ORDER"})
		res.desctable = desctable
		return res

	desctable = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/desctable.html", {"nama": "SALES ORDER", "document":doc})

	res.desctable = desctable
	return res


@frappe.whitelist()
def get_sales_invoice(**kwargs):
	today = date.today()
	res = frappe._dict({})
	if not ('System Manager' in [i.role for i in frappe.get_doc('User', frappe.session.user).roles]):
		return res

	doc = frappe.db.sql("""select t1.name as name, t1.customer as customer, t1.customer_name as customer_name, t1.posting_date as posting_date, \
				t1.grand_total as grand_total, t1.owner as owner, t2.sales_order as sales_order \
				from `tabSales Invoice` as t1 \
				inner join `tabSales Invoice Item` as t2 on t2.parent = t1.name \
				where t1.posting_date = %s""", (today), as_dict = True)

	if not doc:
		invoices = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/invoices.html", {"nama": "SALES INVOICE"})
		res.invoices = invoices
		return res

	invoices = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/invoices.html", {"nama": "SALES INVOICE", "document":doc})

	res.invoices = invoices
	return res


@frappe.whitelist()
def get_so_item(**kwargs):
        today = date.today()
        res = frappe._dict({})
        if not ('System Manager' in [i.role for i in frappe.get_doc('User', frappe.session.user).roles]):
                return res

        doc = frappe.db.sql("""select t1.name as name, t1.customer_name as customer_name, t1.transaction_date as posting_date, t1.status, \
                                t2.item_name as item, t2.qty as qty, t2.price_list_rate as price, t2.discount_percentage as discper, t2.discount_amount as discamt, t2.rate as harga \
                                from `tabSales Order` as t1 \
                                inner join `tabSales Order Item` as t2 on t2.parent = t1.name \
                                where t1.status != 'Cancelled' AND t1.status != 'Closed' AND t1.status != 'Completed' """, as_dict = True)

        if not doc:
                soitem = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/soitem.html", {"nama": "SALES ORDER ITEM"})
                res.soitem = soitem
                return res

        soitem = frappe.render_template("sales_monitoring/sales_monitoring/page/sales_monitor/soitem.html", {"nama": "SALES ORDER ITEM", "document":doc})

        res.soitem = soitem
        return res
