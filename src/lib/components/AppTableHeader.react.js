import React, { Component } from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';

const propTypes = {

	 children: PropTypes.node,

	 id: PropTypes.string,

	 className: PropTypes.string,

	 tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),

	 style: PropTypes.object,

	 data: PropTypes.any


}

const defaultProps = {
	id: 'tableheader',
	tag: 'tr'
}

class AppTableHeader extends Component {
	render() {
		const { id, className, children, tag: Tag, data, ...attributes } = this.props;

		const classes = classNames(className, 'table');

		const headers = data;
		const th = [];
		headers.forEach(item => {
			const temp = <th>{item}</th>
			th.push(temp)
		})


		return (
      
        <Tag id={id} className={classes} {...attributes}>
        	{th}
            {children}
        </Tag>
      
    	);
	}
}

AppTableHeader.propTypes = propTypes;
AppTableHeader.defaultProps = defaultProps;

export default AppTableHeader;
