import React, { Component } from 'react';

import './index.css';
import '../../../share/css/color.css';

class CommunityMain extends Component {
	render(){
		return (
			<aside>
				<div>
					<h2>望海风情海岸</h2>
					<span className="message_code">000073</span>
				</div>
				<div className="message_price">
					<span className="message_price_1 color_up priceup">8800.73</span>
					<span className="message_price_2 color_up">+ 13.31%</span>
					<span className="message_price_1"></span>
				</div>
				<div id="message_main">
					<span className="message_main_1">环翠区</span>
					<span className="message_main_1">2012年</span>
					<span className="message_main_1">6600户</span>
				</div>
				<div className="message_chengjiao">
					<table id="message_chengjiao_set">
						<thead>
							<tr className="message_chengjiao_card">
								<th className="message_chengjiao_card_1" width="25%">均价</th>
								<th className="message_chengjiao_card_2" width="20%">面积</th>
								<th className="message_chengjiao_card_2" width="20%">总价</th>
								<th className="message_chengjiao_card_2">成交时间</th>
							</tr>
						</thead>
						<tbody>
							<tr className="message_chengjiao_card">
								<td className="message_chengjiao_card_1 color_down" width="25%">8600.00元</td>
								<td className="message_chengjiao_card_2" width="20%">140m<sup>2</sup></td>
								<td className="message_chengjiao_card_2" width="20%">124.6万</td>
								<td className="message_chengjiao_card_2">2013-03-01</td>
							</tr>
							<tr className="message_chengjiao_card">
								<td className="message_chengjiao_card_1 color_up" width="25%">8900.80元</td>
								<td className="message_chengjiao_card_2" width="20%">140m<sup>2</sup></td>
								<td className="message_chengjiao_card_2" width="20%">124.6万</td>
								<td className="message_chengjiao_card_2">2013-03-01</td>
							</tr>
							<tr className="message_chengjiao_card">
								<td className="message_chengjiao_card_1 color_up" width="25%">7900.80元</td>
								<td className="message_chengjiao_card_2" width="20%">140m<sup>2</sup></td>
								<td className="message_chengjiao_card_2" width="20%">124.6万</td>
								<td className="message_chengjiao_card_2">2013-03-01</td>
							</tr>
							<tr className="message_chengjiao_card">
		                        <td className="message_chengjiao_card_1 color_down" width="25%">7600.80元</td>
		                        <td className="message_chengjiao_card_2" width="20%">140m<sup>2</sup></td>
		                        <td className="message_chengjiao_card_2" width="20%">124.6万</td>
		                        <td className="message_chengjiao_card_2">2013-03-01</td>
		                    </tr>
		                    <tr className="message_chengjiao_card">
								<td className="message_chengjiao_card_1 color_down" width="25%">7600.80元</td>
								<td className="message_chengjiao_card_2" width="20%">140m<sup>2</sup></td>
								<td className="message_chengjiao_card_2" width="20%">124.6万</td>
								<td className="message_chengjiao_card_2">2013-03-01</td>
							</tr>
						</tbody>
					</table>
				</div>
			</aside>
		);
	}
}

export default CommunityMain;
