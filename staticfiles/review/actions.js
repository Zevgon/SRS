export const fetchWords = () => {
  const url = '/api/play';

  return (dispatch) => {
    const ret = fetch(url)
    .then(r => r.json())
    .then(r => {
      dispatch(wordsReceived(r))
    })
    .catch(error => {
      dispatch(errorReceived);
    });
  }
};

export const wordsReceived = words => {
  return {
    type: 'RECEIVE_WORDS',
    payload: words,
  }
}

export const errorReceived = error => {
  return {
    type: 'RECEIVE_ERROR',
    payload: error,
  }
}
