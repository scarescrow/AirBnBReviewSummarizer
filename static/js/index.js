$(document).ready(function(){
    $('select').formSelect();
    $('select > option').css('font-size', '40px');
    $('#city_submit').click(function() {
        var city = $('select').val();
        if (city === null) {
            M.toast({html: "Please select a city!"});
            return false;
        } else {
            window.location.href = "/city/" + city
        }
    })
});