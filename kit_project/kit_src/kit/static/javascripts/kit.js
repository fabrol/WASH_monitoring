function deleteReporter(elem, pk, name) {
    if (confirm('Are you sure you want to remove ' + name + '?')) {
        $(elem).parents('tr').remove();
        $.post('../user/' + pk + '/delete/', function(data) {});
    }
}

function editReporter(elem, pk) {
    overlay_loading_panel($(elem).parents('tr'));
    $(elem).parents('tr').load('../user/' + pk + '/edit/', '', function() {
        $('#div_panel_loading').hide();
    });
}

function editSubmission(elem, pk){
	overlay_loading_panel($(elem).parents('tr'));
	$(elem).parents('tr').load('../reports/submissions/' + pk + '/edit/', '', function(){
		$('#div_panel_loading').hide();
	});

}

function deleteLocation(elem, pk, name) {
    if (confirm('Are you sure you want to remove ' + name + '?')) {
        $(elem).parents('tr').remove();
        $.post('../location/' + pk + '/delete/', function(data) {});
    }
}

function editLocation(elem, pk) {
    overlay_loading_panel($(elem).parents('tr'));
    $(elem).parents('tr').load('../location/' + pk + '/view/', '', function() {
        $('#div_panel_loading').hide();
    });
}

function deleteReport(elem, pk, name) {
    if (confirm('Are you sure you want to remove ' + name + '?')) {
        $(elem).parents('tr').remove();
        $.post('/xforms/' + pk + '/delete/', function(data) {});
    }
}

function editReport(elem, pk, name) {
	    overlay_loading_panel($(elem).parents('tr'));
		    $(elem).parents('tr').load('../xforms/' + pk + '/edit/', '', function() {
				        $('#div_panel_loading').hide();
						    });
}

function submitForm(link, action, resultDiv) {
    form = $(link).parents("form");
    form_data = form.serializeArray();
    resultDiv.load(action, form_data);
}

