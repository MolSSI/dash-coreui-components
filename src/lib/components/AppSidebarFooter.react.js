import React, { Component } from 'react';
import PropTypes from 'prop-types';
import classNames from 'classnames';

const propTypes = {
  /**
   * The children.
   */
  children: PropTypes.node,

  /**
   * The ID used to identify this component in Dash callbacks, defaults to `AppSidebarfooter`.
   */
  id: PropTypes.string,

  /**
   * The CSS class name, defaults to `sidebar-footer`.
   */
  className: PropTypes.string,

  /**
   * The HTML tag, defaults to `div`.
   */
  tag: PropTypes.oneOfType([PropTypes.func, PropTypes.string])
};

const defaultProps = {
  id: 'AppSidebarfooter',
  tag: 'div'
};

/**
 * CoreUI sidebar footer component.
 */
class AppSidebarfooter extends Component {
  render() {
    const { id, className, children, tag: Tag, ...attributes } = this.props;

    const classes = classNames(className, 'sidebar-footer');
    const footer = children ? 
      <Tag id={id} className={classes} {...attributes} >
        {children}
      </Tag>
     : null;

    return (
      footer
    );
  }
}

AppSidebarfooter.propTypes = propTypes;
AppSidebarfooter.defaultProps = defaultProps;

export default AppSidebarfooter;
