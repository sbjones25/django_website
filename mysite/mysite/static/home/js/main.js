function storeInSession(){
    window.sessionStorage['submit'] = document.getElementById('txtId').value;
}

function checkSubmitStatus(){
    if(window.sessionStorage['submit']){
        alert('The form was submitted by '+ window.sessionStorage['submit']);
        window.sessionStorage['submit'] = '';
    }
}

function searchPhotos () {
    query = document.getElementById('search_text').value;
    console.log(query)
    $.ajax({
        url: 'home/search',
        type: 'get', // This is the default though, you don't actually need to always mention it
        data: {'search' : query},
        success: function(data) {
            console.log(data);
            // sliderHtml = $("#slider").html()
            // for (var i = 0; i < data.length; i++) {
            //     console.log(data[i]['main'])
            //     $(sliderHtml).empty()
            //     $(sliderHtml).prepend($('<img>',{src:data[i]['main']}))
            // };
            // $("#slider").replaceWith(sliderHtml)
            fotorama = $('#slider').data('fotorama');
            fotorama.load(data)
            console.log('done')
        },
        failure: function(data) { 
            console.log('Got an error dude');
        }
    }); 
}