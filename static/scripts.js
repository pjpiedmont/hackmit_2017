var drawCircle2 = function(num) {
	// var num = Math.floor(Math.random() * 100);
	$("#hidden").addClass('visible');
	$("body").css("overflow", "hidden");
	setTimeout(function() {
		$('.ko-progress-circle__fill').addClass('animate');
		$('.ko-progress-circle').attr('data-progress', num);
		var numAnim = new CountUp("percent", 0, num);
		if (!numAnim.error) {
			numAnim.start();
		} else {
			console.error(numAnim.error);
		}
	}, 500);
	setTimeout(function() {
		$('.ko-progress-circle__fill').css("animation-play-state", "paused");
	}, 2500);
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
			url: document.getElementById('url').value,
			text: document.getElementById('text').value
		},

		success: function(res) {
			// $("#accuracy").html(res);
			// $("#results").css({
			// 	"height" : "100px",
			// 	"visibility" : "visible"
			// });
			console.log(res);
			drawCircle2(res);
			// setTimeout(function() {
			// 	$('.ko-progress-circle .ko-progress-circle__slice .ko-progress-circle__fill').css("animation-play-state", "paused");
			// }, 1000);
		}
	})
})

function headerHeight() {
	height = $(window).height();
	$("header, section").css("height", height + "px");
}

$(document).ready(function() {
	headerHeight();
})

$(window).resize(function() {
	headerHeight();
})