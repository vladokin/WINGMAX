import axios from 'axios'
import { useNavigate } from 'react-router-dom'
import React from 'react'
import Navbar from '../components/Navbar'

function ForgotPassword() {
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    const { email } = e.target.elements
    const emailVal = email.value
    
    try {
      const response = await axios.post('/api/forgot-password', { emailVal }, { headers : { 'Content-Type': 'application/json' }})
      if (response.status === 200) {
        alert('Please check your email for password reset link! , Make sure to check your spam folder too!')
        navigate('/login')
      }
    } catch (error) {
      console.log(error)
      alert('Email not found!')
    }
  }
    
  return (
    <>
    <Navbar/>
      <div className="container self-center my-20 mx-auto px-4 py-12 h-full">
        <div className="flex content-center items-center justify-center h-full">
          <div className="w-full lg:w-4/12 px-4">
            <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
              <div className="rounded-t mb-0 px-6 py-6">
                <div className="text-center mb-3">
                  <h6 className="text-blueGray-500 text-sm font-bold">
                    Password Reset
                  </h6>
                </div>
              </div>
              <div className="flex-auto px-4 lg:px-10 ">
                <form onSubmit={ handleSubmit }>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    >
                      Email*
                    </label>
                    <input
                      type="email"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Email"
                      name='email'
                      required
                    />
                  </div>
                  <div className="text-center mt-6 mb-12 ">
                    <input
                      className="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                        type="submit"
                        value="Submit"
                    />
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default ForgotPassword