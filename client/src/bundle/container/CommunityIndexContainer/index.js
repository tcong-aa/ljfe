import React, { Component } from 'react';

import CommunityMain from '../../component/CommunityMain';

class CommunityIndexContainer extends Component {
	render () {
		// <div>{ this.props.community_id }</div>
		return (
			<div>
				<CommunityMain />
			</div>
		);
	}
}

export default CommunityIndexContainer;
