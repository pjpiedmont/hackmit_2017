function drawCircle() {	
	var circle = new ProgressBar.Circle('#container', {
		color: '#FCB03C',
		text: {
				value: '50'
		}
	});
	console.log("draw");
	circle.animate(0.5);  // Number from 0.0 to 1.0
}

var drawCircle2 = function() {
	$('.ko-progress-circle__fill').addClass('animate');
	$('.ko-progress-circle').attr('data-progress', Math.floor(Math.random() * 100));
	setTimeout(function() {
		$('.ko-progress-circle__fill').css("animation-play-state", "paused");
	}, 1000);
}
// setTimeout(window.randomize, 200);
// $('.ko-progress-circle').click(window.randomize);

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
			// $("#accuracy").html(res);
			// $("#results").css({
			// 	"height" : "100px",
			// 	"visibility" : "visible"
			// });
			console.log(res);
			drawCircle2();
			// setTimeout(function() {
			// 	$('.ko-progress-circle .ko-progress-circle__slice .ko-progress-circle__fill').css("animation-play-state", "paused");
			// }, 1000);
		}
	})
})