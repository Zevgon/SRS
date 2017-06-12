export const reducer = (state = {words: []}, action) => {
  switch (action.type) {
    case 'RECEIVE_WORDS':
      return Object.assign({}, {words: action.payload});
    default:
      return state;
  }
};
