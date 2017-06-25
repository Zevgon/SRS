import React from 'react';
import { connect } from 'react-redux';
import {
  fetchWords,
  updateWord,
} from '../actions';

import './app.less';

window.updateWord = updateWord;

class App extends React.Component {
  constructor(props) {
    super(props);
    this.guess = this.guess.bind(this);
  }

  guess() {
    this.props.dispatch(updateWord(1, 'one'));
  }

  componentDidMount() {
    this.props.dispatch(fetchWords());
  }

  render() {
    let formatted = [];
    this.props.words.forEach((word, idx) => {
      formatted.push((
        <ul className='word-info' key={word.english + word.foreign}>
          <li>{idx + 1}</li>
          <li>English: {word.english}</li>
          <li>Foreign: {word.foreign}</li>
          <li>Pronunciation: {word.pronunciation}</li>
        </ul>
      ));
    });
    return (
      <div>
        <button onClick={this.guess}></button>
        {formatted}
      </div>
    );
  }
}


const mapStateToProps = ({ words }) => ({
  words,
});

export default connect(mapStateToProps)(App);
