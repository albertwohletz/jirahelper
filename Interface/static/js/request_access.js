/**
 * Created by albertlwohletz on 7/21/14.
 */

// Captures 'request access' button click
$("#request").click( function() {
        var reason = $("#description").val();

        // If they entered a description, send request, otherwise prompt for one.
        if (reason.length > 0){
            var access_type = $('input:radio[name=access]:checked').val();
            var space_name = $("#space_name").val();
            RequestAccess(access_type, space_name, reason);
        } else {
            alert('Please enter a description for why you want access.');
        }
   }
);

// Sends api call to add that request.
function RequestAccess(access_type, space_name, reason){
    $.ajax({
        url: '/api/request_access?type='+access_type+"&space_name="+space_name+"&reason="+reason,
        cache: false,
        dataType: "HTTP",
        type: "POST"
    });
}
