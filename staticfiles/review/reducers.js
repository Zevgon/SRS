const getNumForward = knowStatus => (
  knowStatus * 20
);

const getUpdatedWords = (words, numForward) => {
  if (numForward === 0) {
    return Array.from(words);
  } else if (numForward >= words.length) {
    return words.slice(1);
  }
  return words.slice(1, numForward).concat([words[0]]).concat(words.slice(numForward));
}

export const wordReducer = (words = [], action) => {
  switch (action.type) {
    case 'RECEIVE_WORDS':
      return action.payload;
    case 'RECEIVE_ERROR':
      return error;
    case 'RECEIVE_GUESS':
      const numForward = getNumForward(action.knowStatus);
      return getUpdatedWords(words, numForward);
    default:
      return words;
  }
};

export const statsReducer = (stats = [], action) => {
  return stats;
}
