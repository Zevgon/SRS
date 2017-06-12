import React from 'react';
import { connect } from 'react-redux';
import { fetchWords } from '../actions';
import './app.less';

const App = props => {
  if (!props.words.length) {
    props.dispatch(fetchWords());
  }
  let formatted = [];
  props.words.forEach(word => {
    formatted.push((
      <ul className='word-info' key={word.english + word.foreign}>
        <li>English: {word.english}</li>
        <li>Foreign: {word.foreign}</li>
        <li>Pronunciation: {word.pronunciation}</li>
      </ul>
    ));
  });
  return (
    <ul>{formatted}</ul>
  );
};

const mapStateToProps = ({ words }) => ({
  words,
});

export default connect(mapStateToProps)(App);
