import React, { Component } from 'react';

import '../../../share/css/color.css';

class KChart extends Component {
	componentDidMount(){
		
	}
	render(){
		return (
			<section id="section_main">
				<div id="main_chart">
					<iframe title="kachrt" src="http://localhost:8086/kchart.html/#/1000&700&data" frameBorder="0"></iframe>
				</div>
			</section>
		);
	}
}

export default KChart;
