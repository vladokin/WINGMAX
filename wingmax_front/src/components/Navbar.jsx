import { NavLink, useNavigate } from 'react-router-dom'
import { useDispatch } from 'react-redux'
import React from 'react'
import { logoutUser } from '../store/slices/accounts/loginSlice.js'
import RegisterDropDown from './RegisterDropDown.jsx'

function Navbar() {
  const dispatch = useDispatch()
  const navigate = useNavigate()
  const userInfo = JSON.parse(localStorage.getItem('userInfo'))

  const logoutHandler = () => {
    dispatch(logoutUser())
    navigate('/')
  }

  return (
    <>
      <nav className="top-0 fixed z-50  w-full flex flex-wrap items-center justify-between px-2 py-3 navbar-expand-lg bg-white shadow">
        <div className="container px-4 mx-auto flex flex-wrap items-center justify-between">
          <div className="w-full relative flex justify-between lg:w-auto lg:static lg:block lg:justify-start">
            <NavLink to="/">
              <img className='w-40' src="/WINGMAX-logo.png" alt="logo" />
            </NavLink>
          </div>
          <div
            className="lg:flex flex-grow items-center bg-white lg:bg-opacity-0 lg:shadow-none"  >
            <ul className="flex flex-col lg:flex-row list-none lg:ml-auto">
            <li className="nav-item">
              <NavLink to = '/' className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-neutral-400 hover:text-sky-500 hover:opacity-75"  >
                Home
              </NavLink>
            </li>
            <li className="nav-item">
              <NavLink to = '/login' className="px-3 py-2 flex items-center text-xs uppercase font-bold leading-snug text-neutral-400 active:text-sky-500 hover:text-sky-500 hover:opacity-75" >
                Dashboard
              </NavLink>
            </li>
            
            </ul>
          </div>
          <div
            className="lg:flex flex-grow items-center bg-white lg:bg-opacity-0 lg:shadow-none" >
            {userInfo ? (
              <ul className="flex flex-col lg:flex-row list-none lg:ml-auto">
                <li className="flex items-center">
                  <button
                    className="bg-sky-500 text-white active:bg-sky-600 font-bold uppercase text-xs px-4 py-2 rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
                    onClick={logoutHandler}
                  >
                  <i className="fas fa-right-from-bracket"></i> Logout
                  </button>
                </li>
              </ul>
              ) : (
                <ul className="flex flex-col lg:flex-row list-none lg:ml-auto">
              <li className="flex items-center">
                <NavLink to = '/login'>
                  <button
                    className="text-sky-500 bg-transparent border border-solid border-sky-500 hover:bg-sky-500 hover:text-white active:bg-sky-600 font-bold uppercase text-xs px-4 py-2 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
                    type="button"
                    >
                    <i className="fas fa-user px-2" ></i> login
                  </button>
                </NavLink>
                </li>
                <li className="flex items-center">
                  <RegisterDropDown />
                </li>
              </ul>
              )}
          </div>
        </div>
      </nav>
    </>
  )
}

export default Navbar