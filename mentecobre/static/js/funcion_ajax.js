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
	$('#dataTable').DataTable( {
	"searching":false
	});  
  });
 
function asignar_articulo_traducción(id){
	$.ajax({
		url: "/mentecobre/asignartraducciones",
		method:"POST",
		data:  {'id':id},
		dataType: "json",
		success: function(response){
			console.log("BIEN")
		
		},
		error:function(response){
			var dialog = bootbox.dialog({
			title: 'Save',
			message: "Algo ha fallado",
					buttons: {
						 ok: {
								label: "Close",
								className: 'btn-info',
								callback: function(result){
									window.location.reload();
								}
								
						}
					}
			  });
		}
		
	});
	
}

function marcar_traducido(traducidoselect, id, notas){
	traducido = traducidoselect
	console.log(traducido)
	$.ajax({
		url: "/mentecobre/marcartraducido",
		method:"POST",
		data:  {'traducido':traducido, 'id':id,'notas':notas},
		dataType: "json",
		success: function(response){
			console.log("BIEN")
		
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


function marcar_revisado(revisadoselect, id, revisadonotas){
	revisado = revisadoselect
	console.log(revisado)
	$.ajax({
		url: "/mentecobre/marcarrevisado",
		method:"POST",
		data:  {'revisado':revisadoselect, 'id':id, 'notas':revisadonotas},
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
function asignar_articulo_revision(id){
	$.ajax({
		url: "/mentecobre/asignarrevisiones",
		method:"POST",
		data:  {'id':id},
		dataType: "json",
		success: function(response){
			console.log("BIEN")
		
		}
		
	});
	
}