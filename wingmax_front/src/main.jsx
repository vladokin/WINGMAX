import { Provider } from 'react-redux'
import { BrowserRouter as Router } from 'react-router-dom'
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import store from './store/configureStore'
import './assets/styles/tailwind.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <Provider store = {store}>
    <Router>
      <App />
    </Router>
  </Provider>,
)
