$("#check_accuracy").submit(function(e) {
    e.preventDefault();

	var $form = $(this);
	var url = "/";

	var posting = $.post(url,
	{
		address: $("#url"),
		text: $("#text")
	});

	posting.done(function(data) {
		alert("posted");
	})
})