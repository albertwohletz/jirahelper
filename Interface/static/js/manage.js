/**
 * Created by albertlwohletz on 7/22/14.
 */
jQuery(".yes").click(function(e){
    e.preventDefault();
    var row = $(this).parent().parent().children();
    var user=row[0].innerHTML;
    var space=row[1].innerHTML;
    var access=row[2].innerHTML;

    $.ajax({
        url: '/api/approve_request?user='+user+"&space_name="+space + "&access=" + access,
        cache: false,
        dataType: "HTTP",
        type: "POST"
    });

    row.remove();
});

jQuery(".no").click(function(e){
    e.preventDefault();
    var row = $(this).parent().parent().children();
    var user=row[0].innerHTML;
    var space=row[1].innerHTML;

    $.ajax({
        url: '/api/remove_request?user='+user+"&space_name="+space,
        cache: false,
        dataType: "HTTP",
        type: "POST"
    });

    row.remove();
});
