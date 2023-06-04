import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate, Link } from 'react-router-dom'
import React, { useEffect } from 'react'
import { registerAirline } from '../store/slices/accounts/registerAirlineSlice'
import Navbar from '../components/Navbar.jsx'


function RegisterAirline() {
  const navigate = useNavigate()
  const dispatch = useDispatch()
  const loading = useSelector(state => state.registerAirline.loading)
  const error = useSelector(state => state.registerAirline.error)
  const MySwal = withReactContent(Swal);

  const handleSubmit = async (e) => {
      e.preventDefault();
      const { iataCode, name, username, email, password1, password2 } = e.target.elements;
      await dispatch(registerAirline(iataCode.value, name.value, username.value, email.value, password1.value, password2.value));
      if (!error){
        MySwal.fire({
          icon: 'success',
          titleText:'Registration Successful',
          text: 'Welcome to Wingmax {user.first_name}, please check your email to verify your account ',  
          timer: 6000,
          timerProgressBar: true,
        })
        navigate('/login')
        }
      else {
        MySwal.fire({
          icon: 'error',
          titleText:'Registration Error',
          text: 'Please check your inputs and try again',
          timer: 3000,
          timerProgressBar: true,
        })
      }};
    

  useEffect(() => {
    if (JSON.parse(localStorage.getItem('userInfo'))){
      navigate('/dashboard');
    }
  }, [navigate]);

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
                    Airline Registration
                  </h6>
                </div>
              </div>
              <div className="flex-auto px-4 lg:px-10 ">
                <form onSubmit={ handleSubmit }>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    >
                      IATA Code*
                    </label>
                    <input
                      type="text"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="IATA Code"
                      name='iataCode'
                      required
                    />
                  </div>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    >
                      Name*
                    </label>
                    <input
                      type="text"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Name"
                      name='name'
                      required
                    />
                  </div>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    >
                      Username*
                    </label>
                    <input
                      type="text"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Username"
                      name='username'
                      required
                    />
                  </div>
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
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    >
                      Password*
                    </label>
                    <input
                      type="password"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Password"
                      name='password1'
                      required
                    />
                  </div>
                  <div className="relative w-full mb-3">
                    <label
                      className="block uppercase text-blueGray-600 text-xs font-bold mb-2"
                    >
                      Password Confirmation*
                    </label>
                    <input
                      type="password"
                      className="border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150"
                      placeholder="Password Confirmation"
                      name='password2'
                      required
                    />
                  </div>
                  <div className="text-center mt-6">
                    <input
                      className="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                        type="submit"
                        value="register"
                    />
                  </div>
                </form>
              </div>
              <hr className="mt-6 border-b-2 border-blueGray-300" />
              <div className="flex-auto  px-4 lg:px-10 pb-6">
                <div className="text-center mt-6 text-sm uppercase ">
                  <Link to='/login '>
                      <small>Have Account? SIGN IN</small>
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  )
}

export default RegisterAirline