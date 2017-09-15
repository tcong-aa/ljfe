$('.main_search').click(function(event) {
	$('#floatlayer').show();
});

$('body').click(function(event) {
	if ($('#floatlayer').is(event.target)) {
		$('#floatlayer').hide();
	}
})

$('.typeahead.tt-input').focus(function(event) {
	alert('w');
	$('.typeahead.tt-input').addClass('twitter-typeahead_hover');
});

$('#the-basics .typeahead').typeahead({
	hint: true,
	minLength: 1,
}, {
	name: 'states',
	async: true,
	source: function(q, cb, process) {
		return $.get('/proxy', {}, function(data) {
			var communities = data.rows.map(function(item) {
				return {
					name: item.name,
					district_name: item.district_name,
					bizcircle_name: item.bizcircle_name
				}
			});
			return process(communities);
		}, 'json');
	},
	templates: {
		empty: [
			'<div class="empty-message">',
			'unable to find any Best Picture winners that match the current query',
			'</div>'
		].join('\n'),
		suggestion: Handlebars.compile('<div class="search_return10"><span class="search_return12">{{ name }}</span><span class="search_return11">{{ bizcircle_name }}</span><span class="search_return11">{{ district_name }}</span></div>')
	}
});