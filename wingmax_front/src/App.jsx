import { CookieConsent } from "react-cookie-consent";
import {  Routes, Route } from 'react-router-dom';
import Home from './pages/Home.jsx';
import Login from './pages/Login.jsx';
import RegisterCustomer from './pages/RegisterCustomer.jsx';
import RegisterAirline from './pages/RegisterAirline.jsx';
import ForgotPassword from './pages/ForgotPassword.jsx';
import Flights from './pages/Flights.jsx';
import Dashboard from "./pages/Dashboard.jsx";


function App() {
  return (
    <>
    <Routes>
        <Route exact path = '/' element = { <Home/> }/>
        <Route exact path = '/login' element = { <Login/> }/>
        <Route exact path = '/register-customer' element = { <RegisterCustomer/> }/>
        <Route exact path = '/register-airline' element = { <RegisterAirline/> }/>
        <Route exact path = '/forgot-password' element = { <ForgotPassword/> }/>
        <Route exact path = '/flights' element = { <Flights/> }/>
        <Route exact path = '/dashboard' element = { <Dashboard/> }/>
    </Routes>
    {/* <CookieConsent
      style={{background: "white",color:'black'}}
      buttonStyle={{background:"#0ea5e9", color:'white', fontSize:'0.75rem', lineHeight:'1rem', textTransform:'uppercase', borderRadius:'0.25rem'}}
      buttonText='Accept'
      expires={1}
      overlay='true'>
      This website uses cookies to enhance the user experience, please accept.
      </CookieConsent> */}
    </>
  )
}

export default App
