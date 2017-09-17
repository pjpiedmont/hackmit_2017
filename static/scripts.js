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
			address: document.getElementById('url').value,
			text: document.getElementById('text').value
		},

		success: function() {
			console.log("success");
		}
	})
})