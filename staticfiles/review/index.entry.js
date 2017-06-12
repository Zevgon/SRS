import React from 'react';
import { render } from 'react-dom';
import App from './components/app';
import { Provider } from 'react-redux';
import store from './store';


document.addEventListener('DOMContentLoaded', () => {
  const play = document.getElementById('play');
  render(
    <Provider store={store}>
      <App />
    </Provider>, play
  );
  window.store = store;
});
