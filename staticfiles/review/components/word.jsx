import React, { Component } from 'react';
import { connect } from 'react-redux';
import { updateWord } from '../actions';

class Word extends Component {
  constructor(props) {
    super(props);
    this.state = {
      guess: '',
    };
    this.submitGuess = this.submitGuess.bind(this);
    this.updateGuess = this.updateGuess.bind(this);
  }

  updateGuess(e) {
    this.setState({
      guess: e.target.value,
    });
  }

  submitGuess(wordId, guess) {
    this.props.dispatch(updateWord(wordId, guess));
  }

  render() {
    return (
      <div>
        <div>{this.props.word.foreign}</div>
        <input type="text" value={this.state.guess} onChange={this.updateGuess} />
        <button onClick={() => this.submitGuess(this.props.word.id, this.state.guess)}></button>
      </div>
    );
  }
}

export default connect()(Word);
