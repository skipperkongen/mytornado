$(function() {
	$('input[type=text]').focus(function() {
		$(this).val('');
	}).blur(function() {
		var el = $(this);
		if(el.val() == '') {
             el.val(el.attr('data-default'));			
		}
	});

	$('input[type=submit]').button();

	$('a#whoweare').click(function() {
		$( "#infobox_whoweare" ).dialog( "open" );
		return false;
	});
	
	$('a#whatis').click(function() {
		$( "#infobox_whatis" ).dialog( "open" );
		return false;
	});
	
	$('.infobox').dialog({
		width: 500,
		autoOpen: false,
		show: "clip",
		hide: "fold"
	});
});