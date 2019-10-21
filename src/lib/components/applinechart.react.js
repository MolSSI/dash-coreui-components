import React, { Component } from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';
import { Line } from 'react-chartjs-2';

const propTypes = {

	 id: PropTypes.string,

	 className: PropTypes.string,

	 tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),

	 style: PropTypes.object


}

const defaultProps = {
	id: 'linechart',
	tag: 'div'
}

class applinechart extends Component{

	constructor(props) {
		super(props)
		this.state = {
			chartdata: {
				labels: ['M', 'T', 'W', 'T', 'F', 'S', 'S', 'M', 'T', 'W', 'T', 'F', 'S', 'S', 'M', 'T', 'W', 'T', 'F', 'S', 'S', 'M', 'T', 'W', 'T', 'F', 'S', 'S'],
			    datasets: [{
				    label: 'My First dataset',
				    backgroundColor: 'transparent',
				    borderColor: 'chartreuse',
				    pointHoverBackgroundColor: '#fff',
				    borderWidth: 2,
				    data: [165, 180, 70, 69, 77, 57, 125, 165, 172, 91, 173, 138, 155, 89, 50, 161, 65, 163, 160, 103, 114, 185, 125, 196, 183, 64, 137, 95, 112, 175]
					},  {
				    label: 'My Second dataset',
				    backgroundColor: 'transparent',
				    borderColor: '#F9183D',
				    pointHoverBackgroundColor: '#fff',
				    borderWidth: 2,
				    data: [92, 97, 80, 100, 86, 97, 83, 98, 87, 98, 93, 83, 87, 98, 96, 84, 91, 97, 88, 86, 94, 86, 95, 91, 98, 91, 92, 80, 83, 82]
				    }, {
				    label: 'My Third dataset',
				    backgroundColor: 'transparent',
				    borderColor: '#1897F9',
				    pointHoverBackgroundColor: '#fff',
				    borderWidth: 1,
				    borderDash: [8, 5],
				    data: [65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65]
				    }]
			},

			chartoption: {
				    maintainAspectRatio: false,
				    legend: {
				      display: false
				    },
				    scales: {
				      xAxes: [{
				        gridLines: {
				          drawOnChartArea: false
				        }
				      }],
				      yAxes: [{
				        ticks: {
				          beginAtZero: true,
				          maxTicksLimit: 5,
				          stepSize: Math.ceil(250 / 5),
				          max: 250
				        }
				      }]
				    },
				    elements: {
				      point: {
				        radius: 0,
				        hitRadius: 10,
				        hoverRadius: 4,
				        hoverBorderWidth: 3
				      }
				
				}
			}
		}
	}


	render() {

		const { id, className, tag: Tag, ...attributes } = this.props;

		const classes = classNames(className, 'chart');

		return(
			<Tag id={id} className={classes} {...attributes}>
          		<Line 
          			data = {this.state.chartdata}
          			options={this.state.chartoption}
          		/>
        	</Tag>

		);
	}
}

applinechart.propTypes = propTypes;
applinechart.defaultProps = defaultProps;

export default applinechart;