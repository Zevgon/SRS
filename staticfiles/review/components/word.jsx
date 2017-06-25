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

  submitGuess(e, wordId, guess) {
    e.preventDefault();
    this.props.dispatch(updateWord(wordId, guess));
    this.setState({
      guess: '',
    });
  }

  render() {
    return (
      <div>
        <div>{this.props.word.foreign}</div>
        <div>{this.props.numCurrent}/{this.props.total}</div>
        <form>
          <input type="text" value={this.state.guess} onChange={this.updateGuess} />
          <button onClick={(e) => this.submitGuess(e, this.props.word.id, this.state.guess)}></button>
        </form>
      </div>
    );
  }
}

const mapStateToProps = ({ wordCount }) => ({
  total: wordCount.total,
});

export default connect(mapStateToProps)(Word);
