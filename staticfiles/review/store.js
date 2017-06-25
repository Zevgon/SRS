import { createStore, applyMiddleware } from 'redux';
import { wordReducer, statsReducer } from './reducers';
import thunkMiddleware from 'redux-thunk';
import { combineReducers } from 'redux';

const initialState = {
  words: [],
  stats: [],
}

const rootReducer = combineReducers({
  words: wordReducer,
  stats: statsReducer,
});

const store = createStore(rootReducer, initialState, applyMiddleware(thunkMiddleware));

export default store;
