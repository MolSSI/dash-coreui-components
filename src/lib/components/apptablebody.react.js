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
	id: 'tablebody',
	tag: 'tr'
}

class apptablebody extends Component {
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

apptablebody.propTypes = propTypes;
apptablebody.defaultProps = defaultProps;

export default apptablebody;
