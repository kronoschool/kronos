// this is the code to handle the chunks
// i'm practicing my commentings , don't laugh
// tried to comment and space clearly
// we'll run it through a minifier later,
// to remove whitespace / comments

$(function () {


    // display, if not chunks exist
    var noChunks = function () {

        $nochunks = $('<div id="nochunks" />');
        $nochunks
            .append('<p>Add some chunks ...</p>')
            .hide()
            .appendTo($('#chunks'))
            .fadeIn('slow');

    }


    // actions on chunks
    var addHooks = function () {

        $('a.foots').click(function () {
            
            // what action are you performing on the chunk?
            var action = this.href.split('#')[1];

            switch (action) {
                
                case "remove":
                    $parent = $(this).parents('.chunk');
                    $parent
                        .fadeOut('slow', function () {

                            $(this).remove();
                            if($('#chunks').children().length < 1) { noChunks(); }

                        });
                    break;
                    
                };

            return false;

        });

    }

        
    // add a chunk
    $('a.add').click(function () {


        // what type of chunk are you creating?
        var type = this.href.split('#')[1];


        // this is the footer of the chunk, while editing
        var $chunkfoot = $('<div class="chunkfoot" />');
        var $chunkmenu = $('<div class="chunkmenu" />');
        $chunkmenu.append($('<ul>'
            + '<li><a class="foots" href="#cancel">Cancel</a></li>'
            + '<li><a class="foots" href="#save">Save</a></li>'
            + '<li><a class="foots" href="#remove">Remove</a></li>'
            + '</ul>'));
        $chunkfoot.append($chunkmenu);


        // this generate the main chunk edit form
        var $chunkcontent = $('<div class="chunkcontent" />');
        var $editchunk = $('<p>Sorry, I don\'t support this type of chunk yet.</p>');
        if(type == 'text') {
            $editchunk = $('<textarea rows="4" cols="80" /></textarea>');
        }
        $chunkcontent.append($editchunk);
 
        
        // adds the chunk to the page
        var $chunk = $('<div class="chunk" />');
        $chunk
            .append($chunkcontent)
            .append($chunkfoot)
            .hide()
            .appendTo($('#chunks'));
   
           
        // gets rid of the "Add some chunks ..." msg, if there aint' any
        if($('#nochunks').length > 0) {

            $('#nochunks').fadeOut('slow', function () { 
            
                $(this).remove();
                $chunk.fadeIn();

            });

        } else { $chunk.fadeIn('slow'); }
  
        
        // adds the remove chunk listeners
        addHooks();

        // don't follow the url
        return false;


    });


    // run, cause there ain't no chunks
    noChunks();


});
