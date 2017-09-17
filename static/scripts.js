$("#check_accuracy").submit(function(e) {
	e.preventDefault();
	
	alert("hello");

	var $form = $(this);
	var url = "/analyze";

	alert("world");

	var posting = $.post(url,
	{
		address: document.getElementById('url').value,
		text: document.getElementById('text').value
	});

	posting.done(function(data) {
		alert("posted");
	})
})