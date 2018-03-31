$(document).ready(function(){
	$("#region_selector").change(function(){
		$.ajax({
			type: "GET",

			data: {
				"region_id": $("#region_selector").val(),
			},

			url: "/get_towns_list/",

			dataType: "html",
			cache: false,

			success: function(data){
				if(data == 'None'){
					console.log('None');

				}
				else {
					$("#town_selector").removeClass('d-none')
					$("#town_selector").html(data)
				}
			}

		});
	});
});