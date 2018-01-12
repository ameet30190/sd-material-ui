import React from 'react';
import { mount, shallow } from 'enzyme';
import Snackbar from 'material-ui/Snackbar';
import SDSnackbar from '../SDSnackbar.react';

describe('SDSnackbar', () => {
  it('renders', () => {
    const component = shallow(
      <SDSnackbar id='test-id' open={false} message='test message' />
    );

    expect(component.props().id).toEqual('test-id');
    expect(component.find(Snackbar).length).toBe(1);
  });

  it('opens and closes', () => {
    const component = shallow(
      <SDSnackbar id='test-id' open={false} message='test message' />
    );

    expect(component.state().open).toEqual(false);
    component.setProps({open: true});
    expect(component.state().open).toEqual(true);
    component.setProps({open: false});
    expect(component.state().open).toEqual(false);
  });

  it('closes automatically', () => {
    const component = shallow(
      <SDSnackbar id='test-id' autoHideDuration={500} open={false} message='test message' />
    );

    expect(component.state().open).toEqual(false);
    component.setProps({open: true});
    expect(component.state().open).toEqual(true);
    setTimeout(() => expect(component.state().open).toEqual(false), 600);
  });

  it('fires events', () => {
    const mockFire = jest.fn();
    const component = mount(
      <SDSnackbar
        id='test-id'
        message='test message'
        open={true}
        action='ready, aim...'
        fireEvent={mockFire}
      />
    );

    component.find('button').simulate('click');
    expect(mockFire.mock.calls.length).toEqual(1);
  });

  it('renders without fireEvent', () => {
    const component = shallow(
      <SDSnackbar id='test-id' open={false} message='test message' fireEvent={null} />
    );

    expect(component.find(Snackbar).length).toBe(1);
  });

  it('increments n_clicks', () => {
    const mockProps = jest.fn();
    const component = mount(
      <SDSnackbar
        id='test-id'
        action='click me'
        message='test message'
        open={true}
        n_clicks={1}
        setProps={mockProps}
      />
    );

    component.find('button').simulate('click');
    expect(mockProps).toHaveBeenCalledWith({n_clicks: 2});
  });
});
