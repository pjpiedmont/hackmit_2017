$("#check_accuracy").submit(function(e) {
	e.preventDefault();

	// var data = {
	// 	address: document.getElementById('url').value,
	// 	text: document.getElementById('text').value
	// }

	$.ajax({
		type: "POST",
		url: "/analyze",
		data: {
			csrfmiddlewaretoken: '{{ csrf_token }}',
			address: document.getElementById('url').value,
			text: document.getElementById('text').value
		},

		success: function(res) {
			$("#accuracy").html(res);
			$("#results").css("height", "100px");
		}
	})
})