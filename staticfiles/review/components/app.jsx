import React from 'react';
import { connect } from 'react-redux';
import { fetchWords } from '../actions';

const App = props => {
  if (!props.words.length) {
    props.dispatch(fetchWords());
  }
  return (
    <div>{props.words}</div>
  );
};

const mapStateToProps = ({ words }) => ({
  words,
});

export default connect(mapStateToProps)(App);
