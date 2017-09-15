$('.main_search').keyup(function (event) {
	console.log(event.target.value);
	// ajax

	// function (data) {
		let communities = [{community_name: '小区', community_id: '000088'}]
		let lists = '';
		for(let i = 0; i < communities.length; i++) {
			let li = `
				<li>
					<span class="search_result_1">${ communities[i].community_name }</span>
					<span class="search_result_2">${ communities[i].community_id }</span>
				</li>
			`;
			lists += li;
		}
		
		$('#search_result ul').html(lists);
		$('#search_result').show();
	// }
});

$('.main_search').click(function (event) {
	$(this).addClass('main_search_hover');
});

$('.typeahead.tt-input').focus(function (event) {
	alert('w')
	$('.typeahead.tt-input').addClass('twitter-typeahead_hover');
});


