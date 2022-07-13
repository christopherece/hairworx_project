$("#location").change(function () {
   const siteId = $(this).val();  // get the selected subject ID from the HTML dropdown list 
   $.ajax({                       // initialize an AJAX request
       type: "POST",
       url: '{% url "get_stylist_ajax" %}',
       data: {
           'site_id': siteId,       // add the country id to the POST parameters
           'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
       },
       success: function (data) {   // `data` is from `get_topics_ajax` view function
           let html_data = '<option value="">---------</option>';
           data.forEach(function (data) {
               html_data += `<option value="${data.id}">${data.name}</option>`
           });
           $("stylist_name").html(html_data); // replace the contents of the topic input with the data that came from the server
       }
   });
});
