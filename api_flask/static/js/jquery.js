$(document).ready(function(){

});

function checkInput(option, loopIndex) {
	$('.requestDiv').hide();
	$('.reponseDiv').hide();

	var id_div = "";
	id_div = "#form" + loopIndex;
	$(id_div).show();

	var index = "";
	index = option.indexOf(":");
	var input = "";
	input = "#input" + loopIndex;
	if (index > -1) {
		var res_input = option.split(":");
		var p_input = "#inputName" + loopIndex;
		$(p_input).append(res_input[res_input.length - 1]);
		$(".idNeeded").show();
		$(".idNoNeeded").hide();
	} else {
		$(".idNeeded").hide();
		$(".idNoNeeded").show();
	}
}

function apiRequest(url, loopIndex) {
	var response_status = "";
	var response_msg = "";
	var response_data = "";
	var response_name = "";
	var id_div = "";
	id_div = "#response" + loopIndex;
	var input = "";
	input = "#input" + loopIndex;
	var res_url = url.split(":");

	$.ajax({
		url: '/api/' + res_url[0] + $(input).val(),
		data: $(input).serialize(),
		dataType: 'json',
		type: 'GET',
		success: function(response) {
			$(id_div).show();

			response_status = response.status;
			$(".responseStatus").html(response_status);

			response_msg = response.error;
			$(".responseMsg").html(response_msg);

			response_data = JSON.stringify(response.data, undefined, 2);
			response_name = response.name;
			$(".responseData").html("{ ");
			$(".responseData").append("<br>");
			$(".responseData").append(response_name);
			$(".responseData").append(response_data);
			$(".responseData").append("<br>");
			$(".responseData").append(" }");

			console.log(response.data);			
		},
		error: function(error) {
			console.log(error);
		}
	});
}