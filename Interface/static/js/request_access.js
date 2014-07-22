/**
 * Created by albertlwohletz on 7/21/14.
 */

// Captures 'request access' button click
$("#request").click( function() {
        var desc = $("#description").val();
        if (desc.length > 0){
            // If they entered a description, send request.

        } else {
            alert('Please enter a description for why you want access.');
        }
   }
);