import { createStore, applyMiddleware } from 'redux';
import {
  wordReducer,
  statsReducer,
  wordCountReducer,
  revealReducer,
} from './reducers';
import thunkMiddleware from 'redux-thunk';
import { combineReducers } from 'redux';

const initialState = {
  words: [],
  stats: [],
  wordCount: {
    total: 0,
    current: 0,
  }
}

const rootReducer = combineReducers({
  words: wordReducer,
  stats: statsReducer,
  wordCount: wordCountReducer,
  revealed: revealReducer,
});

const store = createStore(rootReducer, initialState, applyMiddleware(thunkMiddleware));

export default store;
