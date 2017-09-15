import React, { Component } from 'react';
import { withRouter } from 'react-router-dom';
import CommunityIndexContainer from '../../container/CommunityIndexContainer';
import KChart from '../../component/KChart';

class CommunityIndexScene extends Component {
	render () {
		console.log(this.props.match.params);
		let community_id = this.props.match.params.community_id.slice(1);
		return (
			<div>
				<KChart community_id={ community_id } />
				<div id="empty"></div>	
				<CommunityIndexContainer community_id={ community_id } />
			</div>
		);
	}
}

export default withRouter(CommunityIndexScene);
