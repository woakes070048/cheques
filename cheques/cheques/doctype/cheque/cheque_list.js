frappe.listview_settings['Cheque'] = {
	get_indicator: function(doc) {
		color = {
			'Activo': 'green',
			'Inactivo': 'red'
		}
		return [__(doc.estado), color[doc.estado], "estado,=," + doc.estado];
	}

};
