import { postJson } from '../common/utils';

export const fetchWords = () => {
  const url = '/api/play';

  return (dispatch) => {
    const ret = fetch(url)
    .then(r => r.json())
    .then(r => {
      dispatch(wordsReceived(r))
    })
    .catch(() => {
      dispatch(receiveError)
    });
  };
};

export const updateWord = (wordId, english) => {
  const data = {
    wordId,
    english,
  };

  return dispatch => {
    postJson('/api/guess/', data).then(res => {
      dispatch(receiveGuess(res.knowStatus))
    }).catch(() => {
      dispatch(receiveError)
    });
  };


  // return (dispatch) => {
  //   const ret = fetch(url)
  //   .then(r => r.json())
  //   .then(knowStatus => {
  //     dispatch(receiveGuess(knowStatus));
  //   })
  //   .catch(error => {
  //     dispatch(receiveError)
  //   });
  // };
}

export const receiveGuess = knowStatus => {
  return {
    type: 'RECEIVE_GUESS',
    knowStatus: parseInt(knowStatus, 10),
  };
}

export const wordsReceived = words => {
  return {
    type: 'RECEIVE_WORDS',
    payload: words,
  }
}

export const receiveError = error => {
  return {
    type: 'RECEIVE_ERROR',
    payload: error,
  };
}

export const revealWord = () => {
  return {
    type: 'REVEAL_WORD',
  }
}

export const hideWord = () => {
  return {
    type: 'HIDE_WORD',
  }
}
