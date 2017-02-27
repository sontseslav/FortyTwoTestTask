$(function() {
	//function for polling
	console.log("Loaded!"); // sanity check
	function poll() {
		console.log("start polling");
		setTimeout(function() {
			$.ajax({
				url: "requests",
				type : "GET",
				data: {},
				success: function(json) {
					console.log(json); // log the returned json to the console
				},
				error : function(xhr,errmsg,err) {
					console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
				},
				dataType: "json",
				complete: poll
			});
		}, 5000);
	}
	poll();
});
