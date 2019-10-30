import React, { Component } from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';

const propTypes = {

  /**
    * The children
   */
  children: PropTypes.node,
 
  /**
   * The ID used to identify this component in Dash callbacks, defaults to `AppTableHeader`.
   */
  id: PropTypes.string,
 
  /**
   * The CSS class name, defaults to `apptableheader`.
   */
  className: PropTypes.string,
 
  /**
   * The HTML tag.
   */
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string]),
 
  /**
   * The CSS style.
   */
  style: PropTypes.object,
 
  /**
   * The Data.
   */
  data: PropTypes.any

}

const defaultProps = {
	id: 'tableheader',
	tag: 'tr'
}

/**
 * CoreUI apptableheader component.
 */
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
