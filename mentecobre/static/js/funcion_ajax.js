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

	$('#dataTablecategoria').DataTable();  	

	$.fn.dataTable.moment( 'D-M-YYYY' );
	$('#gregoriotable').DataTable( {
	"paging": false,
	"searching":false,
	"info": false,


	});
	$('#perfiltabla').DataTable( {
	"searching":false,
	"info": false,


	});  
	
    $('#gregoriomodal').modal({show:true});
	
	$('.counter-value').each(function(){
			$(this).prop('Counter',0).animate({
				Counter: $(this).text()
			},{
				duration: 3500,
				easing: 'swing',
				step: function (now){
					$(this).text(Math.ceil(now));
				}
			});
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
	marcado = false
	if($('#enlacecopperen').prop('checked') == true ){ 
		marcado = true }
	$.ajax({
		url: "/mentecobre/marcarrevisado",
		method:"POST",
		data:  {'revisado':revisadoselect, 'id':id, 'notas':revisadonotas, 'checked':marcado},
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

function mostrar_perfil(id){
	var token = $('input[name=csrfmiddlewaretoken]').val();
	$.ajax({
		url: "/mentecobre/perfil",
		method:"POST",
		data:  {'id':id},
		dataType: "json",
		success: function(response){
			console.log("BIEN")
			var user = JSON.parse(response["usuario"]);
			var articulos =  JSON.parse(response["articulos"]);
			console.log(user)
			var userfields = user[0]["fields"];
			var username= userfields["username"];
			var groups = userfields["groups"];
			var grupo=""
			if (groups == 2 )
				grupo = "Traductor"
			else if (groups == 1)
				grupo = "Revisor"
			else
				grupo = "Traductor, Revisor"
			var usernotas = userfields["notas"]
			console.log(groups)
			console.log(grupo)
			console.log(articulos)
			var table = `
				<div class="card-body">
					<h3> ${username}</h3>
					<p> ${grupo} </p>
					 <form method="POST" id="form-usernotas" class="form-tr">						
						<textarea name="notes" id="usuarionotas" maxlength="1000">${usernotas}</textarea>
						<input id="submit_newcause" type="Submit" value="Anotar" class='btn btn-secondary'/>
					</form>
					<hr>
					<table id="gregorio-perfil-table" class="table table-bordered table-striped">
						<thead>
							<th> Artículo </th>
							<th> Estado </th>
						</thead>
						<tbody>`
						for (var i = 0; i< articulos.length; i++){
							var articulosfields = articulos[i]["fields"];
							var articulostitle = articulosfields["tituloEs"]
							var articulostraducido = articulosfields["traducido"]
							if (articulostraducido == null) {
								var estado = "En curso"
							}
							else {
								var estado = "Traducido"
							}
							table += `
									<tr> <td> ${articulostitle}  </td> 
									<td> ${estado}</td>
									</tr> `
						
						}
						
				table += `</tbdoy>
					</table>
				</div>`
			$("#perfilusuario").html(table)
			$('#gregorio-perfil-table').DataTable( {
				"searching":false,
				"info": false,


			});  	
			$("#form-usernotas").submit(function(ev){
					ev.preventDefault()
					updateuser(this, username)
				});
		}
		
	});
	
}

 function updateuser (form, username){
	 console.log(form)
	 var serializedData = $(form).serialize();
	 console.log(serializedData)
	 var notas = form.usuarionotas.value
	 console.log(notas)
	 console.log(username)
	 $.ajax({
            type: 'POST',
            url: "/mentecobre/updateuser",
            data: {'notas':notas, 'username':username},
            success: function (response) {
			  console.log('bien')
			  

            },
            error: function (response) {
            }
			});
	
 }

