import React, { Component } from 'react';
import { Dropdown } from 'reactstrap';
import PropTypes from 'prop-types';

const propTypes = {
  /**
   * The children. 
   */
  children: PropTypes.node,

  /**
   * The ID used to identify this component in Dash callbacks, defaults to `AppHeaderdropdown`.
   */
  id: PropTypes.string,

  /**
   * The dropdown direction, defaults to `down`.
   */
  direction: PropTypes.string
};

const defaultProps = {
  id: 'AppHeaderdropdown',
  direction: 'down'
};

/**
 * CoreUI header dropdown menu component.
 */
class AppHeaderdropdown extends Component {
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      dropdownOpen: false
    };
  }

  toggle() {
    this.setState({
      dropdownOpen: !this.state.dropdownOpen
    });
  }

  render() {
    const { children, id, ...attributes } = this.props;
    return (
      <Dropdown id={id} nav isOpen={this.state.dropdownOpen} toggle={this.toggle} {...attributes}>
        {children}
      </Dropdown>
    );
  }
}

AppHeaderdropdown.propTypes = propTypes;
AppHeaderdropdown.defaultProps = defaultProps;

export default AppHeaderdropdown;
