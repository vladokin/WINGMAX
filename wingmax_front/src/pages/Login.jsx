import Swal from 'sweetalert2'
import withReactContent from 'sweetalert2-react-content'
import { useDispatch, useSelector } from 'react-redux'
import { useNavigate, Link } from 'react-router-dom'
import React from 'react'
import { useEffect } from 'react'
import { login } from '../store/slices/accounts/loginSlice.js'
import Navbar from '../components/Navbar.jsx'


function Login() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const MySwal = withReactContent(Swal);
  const error = useSelector(state => state.login.error);
  const userInfo = useSelector(state => state.login.userInfo);
  const userName = userInfo && userInfo.username;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { email, password } = e.target.elements;
    await dispatch(login(email.value, password.value));
  };

  useEffect(() => {
    if (error) {
      MySwal.fire({
        icon: 'error',
        titleText: 'Login Error',
        text: 'Incorrect email or password',
        timer: 3000,
        timerProgressBar: true,
      });
    } else if (userName) {
      MySwal.fire({
        icon: 'success',
        titleText: 'Login Successful',
        text: 'Welcome back to Wingmax, ' + userName,
        timer: 6000,
        timerProgressBar: true,
      });
      navigate('/dashboard');
    }
  }, [error, userName, navigate]);

  useEffect(() => {
    if (JSON.parse(localStorage.getItem('userInfo'))){
      navigate('/dashboard');
    }
  }, [navigate]);
  
  return (
    <>
    <Navbar/>
      <div className="container mx-auto my-20 px-4 py-12 h-full">
        <div className="flex content-center items-center justify-center h-full">
          <div className="w-full lg:w-4/12 px-4">
            <div className="relative flex flex-col min-w-0 break-words w-full mb-6 shadow-lg rounded-lg bg-blueGray-200 border-0">
              <div className="rounded-t mb-0 px-6 py-6">
                <div className="text-center mb-3">
                  <h6 className="text-blueGray-500 text-sm font-bold">
                    Sign in
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
                      name='password'
                      required
                    />
                    <div className="w-1/2 text-sm pt-0 mt-0">
                    <Link to='/forgot-password'>
                    <small>Forgot password?</small>
                    </Link>
                    </div>
                  </div>
                  <div className="text-center mt-6">
                    <input
                      className="bg-blueGray-800 text-white active:bg-blueGray-600 text-sm font-bold uppercase px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 w-full ease-linear transition-all duration-150"
                        type="submit"
                        value="Sign in"
                    />
                  </div>
                </form>
              </div>
              <hr className="mt-6 border-b-2 border-blueGray-300" />
              <div className="flex-auto flex  px-4 lg:px-10 pb-6">
                <div className="text-center mt-6 w-1/2 text-sm ">
                  <Link to='/register-customer'>
                      <small>Customer Registration</small>
                  </Link>
                </div>
                <div className="text-center mt-6 w-1/2 text-sm ">
                  <Link to='/register-airline'>
                      <small>Airline Registration</small>
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

export default Login