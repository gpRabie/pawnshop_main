// Copyright (c) 2022, Rabie Moses Santillan and contributors
// For license information, please see license.txt

frappe.ui.form.on('Provisional Receipt', {
	refresh: function(frm) {
		frm.set_query('pawn_ticket_type', () => {
			return {
				"filters": {
					"name": 
					[
						'in',
						[
							"Pawn Ticket Jewelry", 
							"Pawn Ticket Non Jewelry"
						]
					]
				}
			}
		})
	},

	pawn_ticket_no: function(frm){
		if (frm.doc.transaction_type == "Redemption") {
			frm.set_value('total', cur_frm.doc.principal_amount);
		}
	},

	transaction_type: function(frm){
		show_payment_fields(frm);
		if (frm.doc.transaction_type == "Redemption") {
			frm.set_value('total', cur_frm.doc.principal_amount);
			frm.set_df_property('amortization', 'hidden', 1);
			frm.set_df_property('interest_payment', 'hidden', 1);
			frm.set_df_property('additional_amortization', 'hidden', 1);
		} else {
			frm.set_value('total', 0.00);
		}
	},

	amortization: function(frm){
		frm.set_value('total', parseFloat(frm.doc.total) + parseFloat(frm.doc.amortization))
		frm.refresh_field('total')
	},

	interest_payment: function(frm){
		frm.set_value('total', parseFloat(frm.doc.total) + parseFloat(frm.doc.interest_payment))
		frm.refresh_field('total')
	},

	discount: function(frm){
		frm.set_value('total', parseFloat(frm.doc.total) - parseFloat(frm.doc.discount))
		frm.refresh_field('total')
	},

	additional_amortization: function(frm){
		frm.set_value('total', parseFloat(frm.doc.total) + parseFloat(frm.doc.additional_amortization))
		frm.refresh_field('total')
	}
});

function show_payment_fields(frm) {
	frm.set_df_property('amortization', 'hidden', 0);
	frm.set_df_property('interest_payment', 'hidden', 0);
	frm.set_df_property('additional_amortization', 'hidden', 0);
}

