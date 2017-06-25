import React from 'react';
import { connect } from 'react-redux';
import { fetchWords } from '../actions';
import Word from './word';
import './app.less';

class App extends React.Component {
  constructor(props) {
    super(props);
  }

  componentDidMount() {
    this.props.dispatch(fetchWords());
  }

  render() {
    return (
      <div>
        {this.props.words.length ? <Word word={this.props.words[0]} /> : null}
      </div>
    );
  }
}

const mapStateToProps = ({ words }) => ({
  words,
});

export default connect(mapStateToProps)(App);
