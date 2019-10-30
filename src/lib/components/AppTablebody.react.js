import React, { Component } from 'react';
import classNames from 'classnames';
import PropTypes from 'prop-types';

const propTypes = {

  /**
    * The children
   */
  children: PropTypes.node,
 
  /**
   * The ID used to identify this component in Dash callbacks, defaults to `AppTableBody`.
   */
  id: PropTypes.string,
 
  /**
   * The CSS class name, defaults to `apptablebody`.
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
	id: 'tablebody',
	tag: 'tr'
}

/**
 * CoreUI apptablebody component.
 */
class AppTableBody extends Component {
	render() {
		const { id, className, children, tag: Tag, data, ...attributes } = this.props;

		const body = data;
		var tr = [];
		
		tr = body.map(item => {
    		var temp = item.map(ele => {
        	return <td>{ele}</td>
    		})
    		return temp
		})

		

		return (
      
        
        <Tag id={id} {...attributes}>
        	{tr}
            {children}
        </Tag>
        
      
    	);
	}
}

AppTableBody.propTypes = propTypes;
AppTableBody.defaultProps = defaultProps;

export default AppTableBody;
