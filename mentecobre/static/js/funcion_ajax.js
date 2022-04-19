 $.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
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
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});
 

$(document).ready(function() {
	$('#dataTable').DataTable();  
  });
 
function asignar_articulo_traducción(user, id){
	console.log(user)
	$.ajax({
		url: "/mentecobre/asignartraducciones",
		method:"POST",
		data:  {'user':user, 'id':id},
		dataType: "json",
		success: function(response){
			var dialog = bootbox.dialog({
			title: 'Save',
			message: "Se ha asignado el nuevo artículo a tu nombre",
					buttons: {
						 ok: {
								label: "Close",
								className: 'btn-info',
								callback: function(){
								}
								
						}
					}
			  });
		
		}
		
	});
	
}

function marcar_traducido(traducidoselect, id){
	traducido = traducidoselect
	console.log(traducido)
	$.ajax({
		url: "/mentecobre/marcartraducido",
		method:"POST",
		data:  {'traducido':traducido, 'id':id},
		dataType: "json",
		success: function(response){
			var dialog = bootbox.dialog({
			title: 'Save',
			message: "Se ha marcado el artículo como traducido",
					buttons: {
						 ok: {
								label: "Close",
								className: 'btn-info',
								callback: function(){
								}
								
						}
					}
			  });
		
		},
		error: function(response){
			var errors = response.responseJSON;
				console.log(errors)
				if ($.isEmptyObject(errors) == false) {
						$('#formtraducidoselect')
							.closest('.form-group')
							.addClass('has-error')
							.append('<span class="help-block" style="color:rgb(255,0,0);">' + value + '</span>');
					
				}
							
				}
		
	});
	
}


function marcar_revisado(revisadoselect, id){
	revisado = revisadoselect
	console.log(revisado)
	$.ajax({
		url: "/mentecobre/marcarrevisado",
		method:"POST",
		data:  {'revisado':revisado, 'id':id},
		dataType: "json",
		success: function(response){
			var dialog = bootbox.dialog({
			title: 'Save',
			message: "Se ha actualizado el estado de la revisión.",
					buttons: {
						 ok: {
								label: "Close",
								className: 'btn-info',
								callback: function(){
								}
								
						}
					}
			  });
		
		},
		error: function(response){
			var errors = response.responseJSON;
				console.log(errors)
				if ($.isEmptyObject(errors) == false) {
						$('#formrevisadoselect')
							.closest('.form-group')
							.addClass('has-error')
							.append('<span class="help-block" style="color:rgb(255,0,0);">' + value + '</span>');
					
				}
							
				}
		
	});
	
}
function asignar_articulo_revision(user, id){
	console.log(user)
	$.ajax({
		url: "/mentecobre/asignarrevisiones",
		method:"POST",
		data:  {'user':user, 'id':id},
		dataType: "json",
		success: function(response){
			var dialog = bootbox.dialog({
			title: 'Save',
			message: "Se ha asignado el nuevo artículo a tu nombre",
					buttons: {
						 ok: {
								label: "Close",
								className: 'btn-info',
								callback: function(){
								}
								
						}
					}
			  });
		
		}
		
	});
	
}