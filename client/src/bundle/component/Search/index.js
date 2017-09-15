import React, { Component } from 'react';

import './index.css';

class Search extends Component {
	constructor () {
		super();
		this.state = {
			searchText: '',
			ifShowDownCard: false
		}
	}
	onChange = (event) => {
		let target = event.target;
		this.setState({
			searchText: target.value
		});
		// ajax
	}
	render () {
		return (
			<div id="search">
	            <input type="text" id="main_search" onChange={this.onChange} />
	            <i name="search"></i>
	            <i name="reset"></i>
	            {
	            	this.state.ifShowDownCard == false ? '' :
	            	(
		            	<div id="search_result">
			                <ul>
			                    <li><span className="search_result_1">华润威海湾九里</span><span className="search_result_2">000080</span></li><li><span className="search_result_1">华润威海湾九里</span><span className="search_result_2">000080</span></li><li><span className="search_result_1">华润威海湾九里</span><span className="search_result_2">000080</span></li>
			                    <li></li>
			                    <li></li>
			                </ul>
			            </div>
	            	)
	            }
	            
	        </div>
		);
	}
}

export default Search;