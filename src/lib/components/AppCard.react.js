import React, { Component } from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';

const propTypes = {

	 children: PropTypes.node,

	 id: PropTypes.string,

	 className: PropTypes.string,

	 tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),

	 style: PropTypes.object


}

const defaultProps = {
	id: 'card',
	tag: 'div'
}

class AppCard extends Component {
	render() {
		const { id, className, children, tag: Tag, ...attributes } = this.props;

		const classes = classNames(className, 'card');

		return (
      
        <Tag id={id} className={classes} {...attributes}>
          {children}
        </Tag>
      
    	);
	}
}

AppCard.propTypes = propTypes;
AppCard.defaultProps = defaultProps;

export default AppCard;
