$(function() {
	// This function gets cookie with a given name
    function getCookie(name) {
    	//console.log('get cookies');
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    //console.log('cookie: ' + csrftoken);
    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

	//function for polling
	//console.log("Loaded!"); // sanity check
	function poll() {
		//console.log("start polling");
		setTimeout(function() {
			$.ajax({
				url: "requests",
				type : "POST",
                //empty request
				data: {},
				success: function(response) {
					//console.log("response: " + response); // log the returned data to the console
                    var content = $("#target").html();
                    //console.log("content: " + content);
                    content += response;
                    var contentRows = (content.match(/<tr>/g) || []).length;
                    var responseRows = (response.match(/<tr>/g) || []).length;
                    title = $('title').text();
                    title = title.replace(/.*/, responseRows + " new requests listed");
                    console.log(title);
                    $('title').text(title).delay(2000).queue(function(n) {
                        $(this).text("42 Coffee Cups Test Assignment - Requests");
                        n();
                    });
                    //console.log("contentRows: " + contentRows);
                    //console.log("responseRows: " + responseRows);
                    if (contentRows > 10) {
                        var index = contentRows - 10;
                        for (var i = 0; i < index; i++) {
                            //removing first row
                            content = content.replace(/<tr>(.|\W)*?<\/tr>/, '');
                        }
                    }
                    content = content.replace(/\n/g, '');
                    console.log("content: " + content);
                    $("#target").html(content);
				},
				error: function(xhr,errmsg,err) {
                    console.log("error: " + errmsg);
					console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
				},
				dataType: "html",
				complete: poll
			});
		}, 5000);
	}
	poll();
});
