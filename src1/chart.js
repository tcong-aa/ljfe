// switch week or month
$('.chart_tools_chart_type_month').click(function (event) {
	$(this).addClass('chart_tools_chart_type_now');
	$('.chart_tools_chart_type_week').removeClass('chart_tools_chart_type_now');
});
$('.chart_tools_chart_type_week').click(function (event) {
	$(this).addClass('chart_tools_chart_type_now');
	$('.chart_tools_chart_type_month').removeClass('chart_tools_chart_type_now');

	doFetchData('/week_prices');
});

