import React, { Component } from 'react';
import { connect } from 'react-redux';
import {
  updateWord,
  revealWord,
  unrevealWord,
  hideWord,
  shuffle,
} from '../actions';

class Word extends Component {
  constructor(props) {
    super(props);
    this.state = {
      guess: '',
    };
    this.submitGuess = this.submitGuess.bind(this);
    this.updateGuess = this.updateGuess.bind(this);
    this.reveal = this.reveal.bind(this);
    this.shuffle = this.shuffle.bind(this);
  }

  updateGuess(e) {
    this.setState({
      guess: e.target.value,
    });
  }

  submitGuess(e, wordId, guess) {
    e.preventDefault();
    this.props.dispatch(updateWord(wordId, guess));
    this.props.dispatch(hideWord());
    this.setState({
      guess: '',
    });
  }

  reveal(e) {
    e.preventDefault();
    this.props.dispatch(revealWord());
  }

  unreveal(e) {
    e.preventDefault();
    this.props.dispatch(unrevealWord());
  }

  shuffle(e) {
    e.preventDefault();
    this.props.dispatch(shuffle());
  }

  render() {
    const revealButton = (
      <button onClick={this.props.revealed ? e => this.unreveal(e) : e => this.reveal(e)}>
        {this.props.revealed ? 'Unreveal' : 'Reveal'}
      </button>
    );
    return (
      <div className="card">
        <div className="card-top">
          Q.
          <div>{this.props.numCurrent}/{this.props.total}</div>
        </div>
        <div className="word">{this.props.revealed ?
          this.props.word.english : this.props.word.foreign}
        </div>
        <form className="guess-form">
          <input
            className="guess-field"
            placeholder="Enter Guess"
            type="text"
            value={this.state.guess}
            onChange={this.updateGuess}
          />
          <button onClick={(e) => this.submitGuess(e, this.props.word.id, this.state.guess)}>
            Submit Guess
          </button>
          {revealButton}
          <button onClick={this.shuffle}>Shuffle</button>
        </form>
      </div>
    );
  }
}

const mapStateToProps = ({ wordCount, revealed }) => ({
  total: wordCount.total,
  revealed,
});

export default connect(mapStateToProps)(Word);
