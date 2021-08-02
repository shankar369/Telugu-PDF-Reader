// Show filename, show clear button and change browse 
//button text when a valid extension file is selected
$(".browse-button input:file").change(function (){
    $("input[name='pdf_file']").each(function() {
      var fileName = $(this).val().split('/').pop().split('\\').pop();
      $(".filename").val(fileName);
      $(".browse-button-text").html('<i class="fa fa-refresh"></i> Change');
      $(".clear-button").show();
    });
  });
  
  //actions happening when the button is clicked
  $('.clear-button').click(function(){
      $('.filename').val("");
      $('.clear-button').hide();
      $('.browse-button input:file').val("");
      $(".browse-button-text").html('<i class="fa fa-folder-open"></i> Browse'); 
  }); 

  console.log("scripts loaded")