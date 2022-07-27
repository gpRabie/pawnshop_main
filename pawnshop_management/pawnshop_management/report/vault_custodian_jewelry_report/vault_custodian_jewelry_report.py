# Copyright (c) 2013, Rabie Moses Santillan and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import today

def execute(filters=None):
	columns, data = [], []
	columns = get_columns()
	data2 = frappe.get_all('Pawn Ticket Jewelry', fields=['date_loan_granted'])
	for i in range(len(data2)):
		if not date_has_duplicate(data2[i]['date_loan_granted']):
			in_count = frappe.db.count('Pawn Ticket Jewelry', {'date_loan_granted': data2[i]['date_loan_granted'], 'workflow_state': 'Active'})

			out_count = frappe.db.count('Pawn Ticket Jewelry', {'date_loan_granted': data2[i]['date_loan_granted'], 'workflow_state': 'Redeemed'})

			total_count = data2[i]['total_count'] = frappe.db.count('Pawn Ticket Jewelry', {'workflow_state':['Active', 'Expired']})

			data.append({'date_loan_granted': data2[i]['date_loan_granted'], 'in_count': int(in_count), 'out_count': int(out_count), 'total_count': int(total_count)})
			print(data)
	return columns, data


def get_columns():
	columns = [
		{
			'fieldname': 'date_loan_granted',
			'label': 'Date',
			'fieldtype': 'Date',
			'width': 200
		},

		{
			'fieldname': 'in_count',
			'label': 'IN',
			'fieldtype': 'Int',
			'width': 100
		},

		{
			'fieldname': 'out_count',
			'label': 'OUT',
			'fieldtype': 'Int',
			'width': 100
		},

		{
			'fieldname': 'total_count',
			'label': 'Total',
			'fieldtype': 'Int',
			'width': 100
		}
	]
	return columns

def date_has_duplicate(date):
	has_duplicate = False
	data = frappe.get_all('Pawn Ticket Jewelry', 
		filters= {
			'date_loan_granted': ['<', today()]
		},
		fields=['date_loan_granted']
	)
	for date_loan_granted in data:
		if date_loan_granted['date_loan_granted'] == date:
			has_duplicate = True
			return has_duplicate
	return has_duplicate