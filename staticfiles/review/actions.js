export const fetchWords = () => {
  const url = '/api/play';

  return (dispatch) => {
    const ret = fetch(url)
    .then(r => r.json())
    .then(r => {
      dispatch(wordsReceived(r))
    })
    .catch(url);
  }
};

export const wordsReceived = words => {
  return {
    type: 'RECEIVE_WORDS',
    words
  }
}
