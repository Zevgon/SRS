export const wordReducer = (words = [], action) => {
  switch (action.type) {
    case 'RECEIVE_WORDS':
      return action.payload;
    case 'RECEIVE_ERROR':
      return error;
    default:
      return words;
  }
};

export const statsReducer = (stats = [], action) => {
  return stats;
}
