$(document).ready(function(){
  $('#paciente-espera').on('click', function(e){
    $.ajax({
      url: Urls.agenda_espera(),
      type: 'get',  
      success: function(data){
        $('.paciente-espera-lista').html(data);
      }
    });
  });  

  $.fn.modal.Constructor.prototype.enforceFocus = function () {};

  agudezaclose();
  
  $('.dropify').dropify({
    messages: {
      'default': 'Arrastra y suelta un archivo aquí o haz clic',
      'replace': 'Arrastra y suelta o haz clic para reemplazar',
      'remove':  'Eliminar',
      'error':   'Vaya, sucedió algo mal.'
    }
  });

  var drEvent = $('#input-file-events').dropify();

  drEvent.on('dropify.beforeClear', function(event, element) {
      return confirm("Do you really want to delete \"" + element.file.name + "\" ?");
  });

  drEvent.on('dropify.afterClear', function(event, element) {
      alert('File deleted');
  });

  drEvent.on('dropify.errors', function(event, element) {
      console.log('Has Errors');
  });

  var drDestroy = $('#input-file-to-destroy').dropify();
  drDestroy = drDestroy.data('dropify')
  $('#toggleDropify').on('click', function(e) {
      e.preventDefault();
      if (drDestroy.isDropified()) {
          drDestroy.destroy();
      } else {
          drDestroy.init();
      }
  });
  $('.examen-list').slimScroll({    
    height: '375px',
    size: "5px",
    color: '#dcdcdc' 
 });
});

$(document).keydown(function(e) { 
  if (e.keyCode == 38) {
    $(this).next('.form-control').focus();
  } 
  if (e.keyCode == 40) {
    $(this).prev('.form-control').focus();
  }
});

$('#historiac').on('click', function(e){
  $thisUrl = $(this).attr('data-url');
  $.ajax({
    url: $thisUrl,
    type: 'get',  
    success: function(data){
      $('#lmcontenido').html(data);
      $('#lmodal').modal('show');
    }
  });
});

$('#recetar').on('click', function(e){
  $('#recetaform')[0].reset();
  $("#id_medicamento").val('').trigger("change");
  $('#receta-modal').modal('show');
});

$('#examen-clinico').on('click', function(e){    
  $('#examen-modal').modal('show');
});

$('#form-guardar').on('submit', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $.toast({
          heading: 'Administracion Consulta',
          text: 'Se ha Guardado el registro con exito.',
          position: 'top-right',
          loaderBg:'#ff6849',
          icon: 'success',
          hideAfter: 3500, 
          stack: 6
        });
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#diagform').on('submit', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('.enviod').val('');
        $("#diagnosticos").html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#examenform').on('submit', function (e) {
  e.preventDefault();
  var $formData = new FormData(this);
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      cache: false,
      contentType: false,
      processData: false,            
      success: function(data){
        location.reload();
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#recetaform').on('submit', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('#recetaform')[0].reset();
        $("#id_medicamento").val("").trigger("change");
        $("#recetas").html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

var autoguardado = function(){
  var $formData = $("#form-guardar").serialize();
  var $formArray = {};
  $.each($("#diagform").serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $("#form-guardar").attr('action');
  var $thisMethod = $("#form-guardar").attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        if(!data.success){
            $.toast({
            heading: 'Mensaje del Sistema',
            text: "Esta historia no existe, ha sido borrado",
            position: 'top-right',
            loaderBg:'#ff6849',
            icon: 'error',
            hideAfter: 3500
          });
        }
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $.toast({
            heading: 'Mensaje del Sistema',
            text: "El Servidor ha caido, o esta Historia a sido Eliminada, los datos no han sido guardados",
            position: 'top-right',
            loaderBg:'#ff6849',
            icon: 'error',
            hideAfter: 3500
          });
      }
  });
};

$('#tratform').on('submit', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('.envioct').val('1');
        $('.enviot').val('');
        $("#tratamientos").html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  });
});

$('#controlform').on('submit', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('.enviocontrol').val('');
        $("#controles").html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#diagnosticos').on('submit', '.form-eliminar-diag', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('#diagnosticos').html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#tratamientos').on('submit', '.form-eliminar-trat', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('#tratamientos').html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#controles').on('submit', '.form-eliminar-control', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('#controles').html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

$('#recetas').on('submit', '.form-eliminar-receta', function (e) {
  e.preventDefault();
  var $formData = $(this).serialize();
  var $formArray = {};
  $.each($(this).serializeArray(), function (i, field) {
    $formArray[field.name] = field.value; 
  });
  var $thisUrl = $(this).attr('action');
  var $thisMethod = $(this).attr('method');
  $.ajax({
      method: $thisMethod,
      url: $thisUrl,
      data: $formData,
      success: function(data){
        $('#recetas').html(data);
      },
      error: function(xhr,errmsg,err) {
        // Show an error
        $('#results').html("<div class='alert-box alert radius' data-alert>"+
        "Oops! We have encountered an error. <a href='#' class='close'>&times;</a></div>"); // add error to the dom
        console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  })
});

function imprimirlista(e, obj)
{
  e.preventDefault();
  this_url = $(obj).attr('href');
  window.open(this_url,"reporte","height=600,width=700,status=no, toolbar=no,menubar=no,location=no,scrollbars=yes");
}

$('.autoguardado').on('change', function(){
  autoguardado();
});

$('#id_medicamento').select2({
  language: 'es',
  ajax: {
    url: "/medicamento/medicamento-autocomplete/",
    dataType: 'json',
    delay: 250,
    data: function(params) {
        return {
            q: params.term, // search term
            page: params.page
        };
    },
    processResults: function(data, params) {
        // parse the results into the format expected by Select2
        // since we are using custom formatting functions we do not need to
        // alter the remote JSON data, except to indicate that infinite
        // scrolling can be used
        params.page = params.page || 1;
        return {
            results: data.results,
            pagination: {
                more: (params.page * 30) < data.total_count
            }
        };
    },
    cache: true
  },
  templateSelection: function(selection) {
    console.log('templateSelection', selection);
    $('#id_indicacion').val(selection.indicacion);
    $('#id_presentacion').val(selection.presentacion);
    return selection.text;

  },
  escapeMarkup: function(markup) {
      return markup;
  }, // let our custom formatter work
  minimumInputLength: 2,
  
});
function agudeza() {
    $(".agudeza").hide();
    $("#visor").show();
}
function agudezaclose() {
    $(".agudeza").show();
    $("#visor").hide();
}