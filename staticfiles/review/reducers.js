const getNumForward = knowStatus => {
  if (knowStatus === 0) return 0;
  return parseInt(10 * (2 ** (knowStatus - 1)));
};

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

export const wordCountReducer = (wordCounts = {total: 0, current: 0}, action) => {
  switch (action.type) {
    case 'RECEIVE_WORDS':
      return Object.assign({}, wordCounts, { total: action.payload.length });
    default:
      return wordCounts;
  }
}

export const revealReducer = (revealed = false, action) => {
  switch (action.type) {
    case 'REVEAL_WORD':
      return true;
    case 'HIDE_WORD':
      return false;
    default:
      return revealed
  }
}
