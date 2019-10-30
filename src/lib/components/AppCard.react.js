import React, { Component } from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';

const propTypes = {

  /**
    * The children
   */
  children: PropTypes.node,
  
  /**
   * The ID used to identify this component in Dash callbacks, defaults to `AppSidebar`.
   */
  id: PropTypes.string,
  
  /**
   * The CSS class name, defaults to `appcard`.
   */
  className: PropTypes.string,
  
  /**
   * The HTML tag.
   */
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
  
  /**
   * The CSS style.
   */
  style: PropTypes.object

}

const defaultProps = {
	id: 'card',
	tag: 'div'
}

/**
 * CoreUI appcard component.
 */
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
